@echo off
cd /d "%~dp0"

echo Stopping the patient management system...
docker compose stop

echo.
echo The application has been stopped.
echo Patient data has not been deleted.
pause