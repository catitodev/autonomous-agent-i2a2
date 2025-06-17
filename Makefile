# Autonomous Agent I2A2 Makefile

.PHONY: install run test clean docker-build docker-run

# Instalar dependências
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Executar aplicação Streamlit
run:
	streamlit run app.py

# Executar API
api:
	python api/main.py

# Executar CLI
cli:
	python cli.py "$(MESSAGE)"

# Executar testes
test:
	pytest tests/ -v

# Executar testes com cobertura
test-cov:
	pytest tests/ --cov=src --cov-report=html

# Limpar arquivos temporários
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf .pytest_cache
	rm -rf htmlcov
	rm -f agent_memory.db

# Build Docker
docker-build:
	docker build -t autonomous-agent-i2a2 .

# Run Docker
docker-run:
	docker-compose up -d

# Stop Docker
docker-stop:
	docker-compose down

# Formatar código
format:
	black src/ tests/ frontend/
	flake8 src/ tests/ frontend/

# Setup completo
setup:
	chmod +x setup.sh
	./setup.sh

# Deploy
deploy:
	echo "Deploying to production..."
	# Adicionar comandos de deploy
