@echo off
SET SRCDIR=%~dp0
SET SRCDIR=%SRCDIR:~0,-1%

powershell.exe -ExecutionPolicy bypass -File "%SRCDIR%\install_vs_extensions.ps1"