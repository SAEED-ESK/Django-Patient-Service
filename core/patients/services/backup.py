
import os
import subprocess
import tempfile

from pathlib import Path
from datetime import datetime

from django.conf import settings


def create_database_backup():
    """
    Create a PostgreSQL database backup and return its content
    along with a timestamped filename.
    """
    database = settings.DATABASES["default"]

    env = get_postgres_env(database)

    filename = (
        f"patient_service_backup_"
        f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql"
    )

    command = [
        "pg_dump",
        "--host", database["HOST"],
        "--port", str(database["PORT"]),
        "--username", database["USER"],
        "--dbname", database["NAME"],
        "--no-owner",
        "--no-acl",
        "--format", "plain",
    ]

    result = subprocess.run(
        command,
        env=env,
        capture_output=True,
        check=False,
        timeout=300,
    )

    if result.returncode != 0:
        error_message = result.stderr.decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Database backup failed: {error_message}"
        )

    return filename, result.stdout


def create_emergency_backup():
    """
    Save an emergency database backup to the mounted backups directory
    before attempting a database restore.
    """
    backup_dir = Path("/backups")
    backup_dir.mkdir(parents=True, exist_ok=True)

    filename, backup_content = create_database_backup()
    backup_path = backup_dir / f"emergency_{filename}"

    with backup_path.open("xb") as backup_file:
        backup_file.write(backup_content)

    return backup_path

def restore_database_backup(uploaded_file):
    """
    Restore a PostgreSQL SQL dump after creating an emergency backup.
    """
    if not uploaded_file.name.lower().endswith(".sql"):
        raise ValueError("Only .sql backup files are supported.")

    max_size = 100 * 1024 * 1024

    if uploaded_file.size > max_size:
        raise ValueError("Backup file exceeds the 100 MB limit.")

    with tempfile.NamedTemporaryFile(
        mode="wb",
        suffix=".sql",
        delete=False,
    ) as temp_file:
        temp_path = Path(temp_file.name)

        for chunk in uploaded_file.chunks():
            temp_file.write(chunk)

    try:
        with temp_path.open("rb") as backup_file:
            header = backup_file.read(4096)

        if b"PostgreSQL database dump" not in header:
            raise ValueError(
                "The uploaded file is not a recognized PostgreSQL SQL dump."
            )

        # Keep an emergency copy before replacing the database.
        create_emergency_backup()

        database = settings.DATABASES["default"]
        env = get_postgres_env(database)

        restore_sql = (
            "DROP SCHEMA public CASCADE;\n"
            "CREATE SCHEMA public;\n"
        )

        with tempfile.NamedTemporaryFile(
            mode="wb",
            suffix=".sql",
            delete=False,
        ) as combined_file:
            combined_path = Path(combined_file.name)
            combined_file.write(restore_sql.encode("utf-8"))

            with temp_path.open("rb") as source:
                for chunk in iter(lambda: source.read(1024 * 1024), b""):
                    combined_file.write(chunk)

        try:
            command = [
                "psql",
                "--host", database["HOST"],
                "--port", str(database["PORT"]),
                "--username", database["USER"],
                "--dbname", database["NAME"],
                "--set", "ON_ERROR_STOP=1",
                "--single-transaction",
                "--file", str(combined_path),
            ]

            result = subprocess.run(
                command,
                env=env,
                capture_output=True,
                check=False,
                timeout=600,
            )

            if result.returncode != 0:
                error_message = result.stderr.decode(
                    "utf-8",
                    errors="replace",
                )
                raise RuntimeError(
                    f"Database restore failed: {error_message}"
                )

            return True

        finally:
            combined_path.unlink(missing_ok=True)

    finally:
        temp_path.unlink(missing_ok=True)


def get_postgres_env(database):
    """
    Build the environment used by PostgreSQL command-line tools.
    """
    env = os.environ.copy()
    env["PGPASSWORD"] = database["PASSWORD"]
    return env