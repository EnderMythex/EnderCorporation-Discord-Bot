@echo off

echo ............................................ © EnderMytex Script Copyright ...................................
echo .                                                                                                             .
echo .   Credit : EnderMythex / Chat GPT-4                                                                         .
echo .                                                                                                             .
echo .   FR : Ce script necessite une autorisations de la part de EnderMythex avant d etre modifie ou publie.      .
echo .   EN : This script requires authorization from EnderMythex before being modified or published.              .
echo .                                                                                                             .
echo .                                                                                                             .
echo . Online : %date% %time%                                                        BUILD V0.0.1         .
echo ...............................................................................................................
echo '

echo [SERVER] Server Local Host is starting please wait...

timeout 1

cls

echo ............................................ © EnderMytex Script Copyright ...................................
echo .                                                                                                             .
echo .   Credit : EnderMythex / Chat GPT-4                                                                         .
echo .                                                                                                             .
echo .   FR : Ce script necessite une autorisations de la part de EnderMythex avant d etre modifie ou publie.      .
echo .   EN : This script requires authorization from EnderMythex before being modified or published.              .
echo .                                                                                                             .
echo .                                                                                                             .
echo . Online : %date% %time%                                                        BUILD V0.0.1         .
echo ...............................................................................................................
echo '

echo [SERVER] EnderCorporations Start system is starting please wait...

timeout 2

setlocal enabledelayedexpansion
set ndc=0
title Chargement...
:boucle
set /a alea=%random%%%5+1
set /a total=total+alea
if %total% gtr 100 (
set /a total=total-alea
goto boucle
)
if %ndc% geq 20 goto val2
if "%valeurs%" neq "" (set valeurs=%valeurs%;%alea%) else (set valeurs=%alea%)
goto next
:val2
set valeurs2=%valeurs2%;%alea%
:next
set /a ndc=ndc+1
if %total% neq 100 goto boucle
rem ----------------------
rem CHANGEMENT DE FONCTION
rem ----------------------
for /l %%a in (1 1 %ndc%) do (set largeur=Ä!largeur!)
for /l %%a in (1 1 %ndc%) do (set "espace= !espace!")
set space=%espace:~15%
:loading
set /a n=n+1
if %n% gtr 20 goto lotfor
for /f "tokens=%n% delims=;" %%n in ("%valeurs%") do (set nvaleur=%%n)
goto zap
:lotfor
set /a m=n-20
for /f "tokens=%m% delims=;" %%m in ("%valeurs2%") do (set nvaleur=%%m)
:zap
set /a load=%load%+%nvaleur%
if "%compteur%"=="1" goto jump
if %load% geq 10 (
set "space=%space:~1%"
set compteur=1
)
:jump
if %load%==100 (set "space=%space:~1%") 
set progress=%progress%Û
set espace=%espace:~1%
echo  Chargement...%space%%load%%%
rem %largeur% = ndc
echo Ú%largeur%¿
echo ³%progress%%espace%³
echo À%largeur%Ù
if %n% neq %ndc% (
ping localhost -n 1 > nul
cls
goto loading
)
echo.
echo.

cls

"C:\Users\RTK-g\Desktop\EnderComServerBot\start_system.py"