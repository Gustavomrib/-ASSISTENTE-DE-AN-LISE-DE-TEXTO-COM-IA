@echo off
REM install-windows.bat
REM Script de instalação para Windows

echo.
echo ===================================================
echo Assistente de Analise de Texto com IA
echo Instalador Windows
echo ===================================================
echo.

REM Verifica se Python está instalado
python --version > nul 2>&1
if errorlevel 1 (
    echo Erro: Python nao encontrado!
    echo Baixe em: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [✓] Python encontrado
python --version

REM Cria ambiente virtual (opcional)
echo.
echo Deseja criar um ambiente virtual? (s/n)
set /p create_venv="Escolha: "

if /i "%create_venv%"=="s" (
    echo.
    echo [+] Criando ambiente virtual...
    python -m venv venv
    echo [✓] Ambiente criado em ./venv
    
    echo.
    echo [+] Ativando ambiente virtual...
    call venv\Scripts\activate.bat
    echo [✓] Ambiente ativado
)

REM Instala dependências opcionais
echo.
echo Deseja instalar dependencias opcionais? (s/n)
set /p install_deps="Escolha: "

if /i "%install_deps%"=="s" (
    echo.
    echo [+] Instalando dependencias...
    pip install -r requirements.txt
    echo [✓] Dependencias instaladas
)

echo.
echo ===================================================
echo Instalacao concluida!
echo ===================================================
echo.
echo Como usar:
echo   1. Interface interativa:
echo      python main.py
echo.
echo   2. Exemplos:
echo      python examples.py
echo.
echo   3. Como modulo:
echo      from src.analyzer import TextAnalyzer
echo      analyzer = TextAnalyzer()
echo.
pause
