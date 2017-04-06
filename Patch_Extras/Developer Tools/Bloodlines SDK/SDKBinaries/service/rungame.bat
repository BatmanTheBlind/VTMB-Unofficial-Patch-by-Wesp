@echo off
setlocal ENABLEEXTENSIONS
pushd "%~dp0\.."
set "PATH=%CD%;%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
title Run Game Script
if "%~1"=="" exit

:: Command line for launch
set CMDLine=-dev

:: Check required files
if not exist "GameCfg.ini" (
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] RunGame Error: Missing "%cd%\GameCfg.ini" file.
)

:: Read game config data
for /f "usebackq delims== tokens=1,*" %%a in ("GameCfg.ini") do (
	if /i "%%~a"=="GameExe"    (set "%%~a=%%~b")
	if /i "%%~a"=="GameExeDir" (set "%%~a=%%~b")
	if /i "%%~a"=="ModDir"    (set "%%~a=%%~nb")
	if /i "%%~a"=="ModDir" (set "VProject=%%~b")
)

:: Check obtained paths
for %%p in (GameExe GameExeDir ModDir VProject) do if not defined %%p (
	echo>>"..\..\..\sdk_errors.log" [%date% %time%] RunGame Error: Could not get '%%p' path. SDK resetting required.
)

:: Launch game
pushd "%GameExeDir%"
start "game" "%GameExe%" -game %ModDir% %CMDLine%
exit
