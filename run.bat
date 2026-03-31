@echo off

if not exist .venv (
  echo Please run the install.bat first.

  pause
  exit
)

.venv\Scripts\python.exe main.py

pause
