#!/bin/bash
# install-linux-mac.sh
# Script de instalação para Linux/Mac

echo ""
echo "=================================================="
echo "Assistente de Analise de Texto com IA"
echo "Instalador Linux/Mac"
echo "=================================================="
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "Erro: Python 3 não encontrado!"
    echo "Instale com: sudo apt install python3 (Linux) ou brew install python (Mac)"
    exit 1
fi

echo "[✓] Python encontrado"
python3 --version

# Cria ambiente virtual
echo ""
echo "Deseja criar um ambiente virtual? (s/n)"
read -p "Escolha: " create_venv

if [ "$create_venv" = "s" ]; then
    echo ""
    echo "[+] Criando ambiente virtual..."
    python3 -m venv venv
    echo "[✓] Ambiente criado em ./venv"
    
    echo ""
    echo "[+] Ativando ambiente virtual..."
    source venv/bin/activate
    echo "[✓] Ambiente ativado"
fi

# Instala dependências opcionais
echo ""
echo "Deseja instalar dependências opcionais? (s/n)"
read -p "Escolha: " install_deps

if [ "$install_deps" = "s" ]; then
    echo ""
    echo "[+] Instalando dependências..."
    pip install -r requirements.txt
    echo "[✓] Dependências instaladas"
fi

echo ""
echo "=================================================="
echo "Instalação concluída!"
echo "=================================================="
echo ""
echo "Como usar:"
echo "  1. Interface interativa:"
echo "     python3 main.py"
echo ""
echo "  2. Exemplos:"
echo "     python3 examples.py"
echo ""
echo "  3. Como módulo:"
echo "     from src.analyzer import TextAnalyzer"
echo "     analyzer = TextAnalyzer()"
echo ""
