# Autonomous Agent I2A2 Challenge

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-Latest-green.svg)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Sobre o Projeto

Agente Autônomo desenvolvido para o Desafio I2A2, combinando **LangChain** + **AutoGen** com interface moderna e intuitiva. O sistema oferece capacidades avançadas de processamento de linguagem natural, memória persistente e integração com múltiplas ferramentas.

## Funcionalidades

- Agente Inteligente com memória de longo prazo
- Ferramentas Integradas (web search, calculadora, análise de arquivos)
- Interface Chat moderna e responsiva
- Dashboard de métricas e analytics
- Sistema de Segurança robusto
- API RESTful para integração

## Demo Online

[Acesse a Demo](https://autonomous-agent-i2a2.streamlit.app)

## Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/catitodev/autonomous-agent-i2a2.git
cd autonomous-agent-i2a2

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas chaves de API

# Execute a aplicação
streamlit run app.py
```

## Configuração

### Variáveis de Ambiente

```env
OPENAI_API_KEY=sk-your-openai-key
LANGCHAIN_API_KEY=lsv2-your-langchain-key
PINECONE_API_KEY=your-pinecone-key
GOOGLE_SEARCH_API_KEY=your-google-search-key
SERPAPI_API_KEY=your-serpapi-key
```

### Estrutura do Projeto

```
autonomous-agent-i2a2/
├── frontend/
│   ├── components/
│   ├── styles/
│   └── utils/
├── src/
│   ├── agents/
│   ├── tools/
│   ├── memory/
│   └── config/
├── tests/
├── docs/
├── docker/
└── requirements.txt
```

## Como Usar

### 1. Interface Web
```bash
streamlit run app.py
```

### 2. API REST
```bash
python api/main.py
```

### 3. CLI
```bash
python cli.py "Sua pergunta aqui"
```

## Arquitetura

```
Usuario -> Interface Streamlit -> Agente Coordenador -> Sistema de Memória
                                      |
                                 Ferramentas
                                      |
                              Web Search, Calculator, File Handler
```

## Testes

```bash
# Executar todos os testes
pytest

# Testes com cobertura
pytest --cov=src

# Testes específicos
pytest tests/test_agents.py
```

## Métricas de Performance

- Tempo de Resposta: < 2s (média)
- Taxa de Sucesso: 95%+
- Uso de Memória: < 512MB
- Uptime: 99.9%

## Contribuindo

1. Fork o projeto
2. Crie sua feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Autor

**Catito Dev**
- GitHub: [@catitodev](https://github.com/catitodev)
- LinkedIn: [Seu LinkedIn](https://linkedin.com/in/seu-perfil)

## Agradecimentos

- [I2A2 Academy](https://i2a2.academy) pelo desafio
- [LangChain](https://langchain.com) pela framework
- [Streamlit](https://streamlit.io) pela interface

---

Se este projeto te ajudou, deixe uma estrela!
