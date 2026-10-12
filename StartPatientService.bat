@echo off
setlocal
cd /d "%~dp0"
title Patient Management System

echo ========================================
echo      Patient Management System
echo ========================================
echo.

where docker >nul 2>&1
if errorlevel 1 (
    echo ERROR: Docker is not installed or not in PATH.
    pause
    exit /b 1
)

docker info >nul 2>&1
if errorlevel 1 (
    echo Starting Docker Desktop...

    if exist "%ProgramFiles%\Docker\Docker\Docker Desktop.exe" (
        start "" "%ProgramFiles%\Docker\Docker\Docker Desktop.exe"
    ) else (
        echo Please start Docker Desktop manually.
        pause
        exit /b 1
    )

    echo Waiting for Docker to start...

    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
      "$ready = $false; for ($i = 0; $i -lt 40; $i++) { docker info *> $null; if ($LASTEXITCODE -eq 0) { $ready = $true; break }; Start-Sleep -Seconds 3 }; if (-not $ready) { exit 1 }"

    if errorlevel 1 (
        echo Docker did not start in time.
        echo Open Docker Desktop and try again.
        pause
        exit /b 1
    )
)

echo.
echo Starting the application...
echo The first startup may take several minutes.
echo.

docker compose up --build -d

if errorlevel 1 (
    echo.
    echo ERROR: Application startup failed.
    pause
    exit /b 1
)

echo.
echo Opening the application...
timeout /t 5 /nobreak >nul
start "" "http://localhost:8000/"

echo.
echo Startup command completed.
echo Address: http://localhost:8000/
echo.
pause