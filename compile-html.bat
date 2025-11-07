@echo off
set PATH=%PATH%;C:\Users\btuno\AppData\Local\Programs\MiKTeX\miktex\bin\x64


setlocal
title Compilation LaTeX → HTML et PDF (TeX4ht)

echo ===========================================================
echo   Compilation LaTeX → HTML et PDF du fichier : %~n1.tex
echo ===========================================================

:: Vérifie la présence d'un argument
if "%~1"=="" (
  echo Usage : compile-html nom_fichier_sans_extension
  echo Exemple : compile-html site5
  pause
  exit /b
)

set TEXFILE=%~n1

:: [1/4] Nettoyage
echo [1/4] Nettoyage des fichiers temporaires...
del "%TEXFILE%.aux" "%TEXFILE%.log" "%TEXFILE%.dvi" "%TEXFILE%.lg" "%TEXFILE%.tmp" "%TEXFILE%.xref" "%TEXFILE%.idv" "%TEXFILE%.4ct" "%TEXFILE%.4tc" "%TEXFILE%.css" "%TEXFILE%.toc" "%TEXFILE%.out" >nul 2>&1
echo.

:: [2/4] Choix du moteur
echo [2/4] Choisissez le moteur de compilation :
echo     1 = pdfLaTeX  (par defaut)
echo     2 = XeLaTeX   (meilleur pour UTF-8 et TikZ)
set /p choice=Votre choix [1/2] : 

if "%choice%"=="2" (
  set ENGINE=xelatex
) else (
  set ENGINE=pdftex
)
echo.
echo Moteur choisi : %ENGINE%
echo.

:: [3/4] Compilation HTML
echo [3/4] Compilation LaTeX → HTML (TeX4ht)...
htlatex "%TEXFILE%.tex" "xhtml,mathjax,charset=utf-8" " -cunihtf -utf8" --engine=%ENGINE%
echo.

if exist "%TEXFILE%.html" (
  echo ✅ HTML genere avec succes : %TEXFILE%.html
) else (
  echo ⚠️  Erreur : aucun fichier HTML genere.
)

:: [4/4] Proposition de compilation PDF
echo.
echo Souhaitez-vous aussi generer le PDF correspondant ? (O/N)
set /p genpdf=
if /I "%genpdf%"=="O" (
  echo.
  echo Compilation PDF en cours...
  %ENGINE% "%TEXFILE%.tex"
  if exist "%TEXFILE%.pdf" (
    echo ✅ PDF genere : %TEXFILE%.pdf
  ) else (
    echo ❌ Erreur : aucun PDF genere.
  )
)
echo.

:: Proposition d’ouverture du HTML
if exist "%TEXFILE%.html" (
  echo Ouvrir le fichier HTML ? (O/N)
  set /p rep=
  if /I "%rep%"=="O" start "" "%TEXFILE%.html"
)

echo.
echo ===========================================================
echo   Compilation terminee.
echo ===========================================================

set TEXFILE=%~n1
:: [1/4] Nettoyage
echo [1/4] Nettoyage des fichiers temporaires...
del "%TEXFILE%.aux" "%TEXFILE%.log" "%TEXFILE%.dvi" "%TEXFILE%.lg" "%TEXFILE%.tmp" "%TEXFILE%.xref" "%TEXFILE%.idv" "%TEXFILE%.4ct" "%TEXFILE%.4tc" "%TEXFILE%.css" "%TEXFILE%.toc" "%TEXFILE%.out" >nul 2>&1
echo.
pause
endlocal
