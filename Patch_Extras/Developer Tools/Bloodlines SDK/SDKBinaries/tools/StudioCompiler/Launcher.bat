@echo off
title StudioCompiler :: SDK mode
setlocal EnableExtensions
set "PATH=%SystemRoot%\System32;%SystemRoot%;%SystemRoot%\System32\Wbem"
set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"

set "SMCHome=%~dp0"
set "SMCRegPath=HKCU\Software\CFApps\StudioCompiler"
set "ShowWarning=%~dp0\ShowWarning.exe"

pushd "%~dp0\..\..\.."
if not exist "SDKContent\ModelSrc\" md "SDKContent\ModelSrc"
if not exist "SDKContent\MaterialSrc\" md "SDKContent\MaterialSrc"
if not defined ModDir  set "ModDir=%CD%\Vampire"
if not defined GameDir set "GameDir=%CD%\SDKContent\VpkContent"

if exist "SDKBinaries\GameCfg.ini" (
for /f "usebackq delims== tokens=1,*" %%a in ("SDKBinaries\GameCfg.ini") do (
	if /i "%%~a"=="ModDir" (if exist "%%~b\*" (set "%%~a=%%~b") )
	if /i "%%~a"=="GameDir" (if exist "%%~b\*" (set "%%~a=%%~b") )
))
set "VProject=%GameDir%"

:fix_regpaths
reg>nul add "%SMCRegPath%\StudioCompiler" /v "TabSelect"     /t REG_DWORD /d "0" /f
reg>nul add "%SMCRegPath%\StudioCompiler" /v "SDKDirectory"  /t REG_SZ /d "%CD%\SdkBinaries" /f
reg>nul add "%SMCRegPath%\StudioCompiler" /v "GameDirectory" /t REG_SZ /d "%ModDir%" /f
reg>nul add "%SMCRegPath%\StudioCompiler" /v "Shader"        /t REG_SZ /d "VertexLitGeneric" /f

:copy_reqfiles
for %%f in ("%SMCHome%\CopyFiles\*") do (
if not exist "SDKBinaries\%%~nxf" (
	copy /y "%%~f" "SDKBinaries\%%~nxf"> nul
))

:show_warning
if exist "%SMCHome%\ShowWarning.ini" (
	call "%ShowWarning%" "The modeling features of the SDK are in Alpha state.\r\nKeep in mind these usage limitations:\r\n\r\n1. The model should contain max 10000 polys and 25000 vertexes;\r\n2. Only static prop models are supported - no characters or weapons;\r\n3. Models must be single-boned and have only 1 frame per sequence;\r\n4. Collision physics models may crash the game - compile model as\r\n\042prop_static\042 or turn collisions off when pasting model on the map!" "Important Info - Please read!" OK Warning
	del /f /q "%SMCHome%\ShowWarning.ini"> nul
)

:run_program
start "smc" "%SMCHome%\StudioCompiler.exe"
exit
