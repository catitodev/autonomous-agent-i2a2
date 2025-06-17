#!/bin/bash

echo "🚀 Configurando Autonomous Agent I2A2..."

# Criar ambiente virtual
echo "📦 Criando ambiente virtual..."
python -m venv venv

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source venv/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

# Copiar arquivo de configuração
echo "⚙️ Configurando variáveis de ambiente..."
cp .env.example .env

echo "✅ Setup concluído!"
echo ""
echo "📋 Próximos passos:"
echo "1. Edite o arquivo .env com suas chaves de API"
echo "2. Execute: source venv/bin/activate"
echo "3. Execute: streamlit run app.py"
echo ""
echo "🌐 A aplicação estará disponível em: http://localhost:8501"
