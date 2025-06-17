
import streamlit as st
import time
import random
from datetime import datetime
import json

# Configuração da página
st.set_page_config(
    page_title="Sistema de Agentes Autônomos I2A2",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado para deixar bonito
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .agent-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        text-align: center;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .success-message {
        background: #d4edda;
        border-color: #28a745;
    }
    .info-message {
        background: #d1ecf1;
        border-color: #17a2b8;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown("""
<div class="main-header">
    <h1>🤖 Sistema de Agentes Autônomos I2A2</h1>
    <p>Demonstração Interativa - Inteligência Artificial Avançada</p>
</div>
""", unsafe_allow_html=True)

# Sidebar com informações
with st.sidebar:
    st.markdown("### 📊 Status do Sistema")
    st.success("🟢 Sistema Online")
    st.info(f"⏰ {datetime.now().strftime('%H:%M:%S')}")

    st.markdown("### 🎯 Funcionalidades")
    st.markdown("""
    - ✅ Agentes Autônomos
    - ✅ Processamento de Linguagem Natural
    - ✅ Análise de Dados
    - ✅ Tomada de Decisões
    - ✅ Interface Interativa
    """)

    st.markdown("### 🔧 Tecnologias")
    st.markdown("""
    - Python 3.9+
    - Streamlit
    - OpenAI GPT
    - LangChain
    - Docker
    """)

# Tabs principais
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Dashboard", "🤖 Agentes", "💬 Chat", "📈 Métricas"])

with tab1:
    st.markdown("## 🏠 Dashboard do Sistema")

    # Métricas em colunas
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>5</h3>
            <p>Agentes Ativos</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>127</h3>
            <p>Tarefas Processadas</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>98.5%</h3>
            <p>Taxa de Sucesso</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>24/7</h3>
            <p>Disponibilidade</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Gráfico de atividade
    st.markdown("### 📊 Atividade dos Agentes")

    import pandas as pd
    import numpy as np

    # Dados simulados para o gráfico
    dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
    data = {
        'Data': dates,
        'Tarefas Processadas': np.random.randint(10, 50, 30),
        'Agentes Ativos': np.random.randint(3, 8, 30),
        'Taxa de Sucesso': np.random.uniform(85, 100, 30)
    }
    df = pd.DataFrame(data)

    col1, col2 = st.columns(2)
    with col1:
        st.line_chart(df.set_index('Data')['Tarefas Processadas'])
    with col2:
        st.bar_chart(df.set_index('Data')['Agentes Ativos'])

with tab2:
    st.markdown("## 🤖 Gerenciamento de Agentes")

    # Lista de agentes
    agentes = [
        {"nome": "Agente Coordenador", "status": "Ativo", "especialidade": "Coordenação e Delegação", "tarefas": 45},
        {"nome": "Agente Analista", "status": "Ativo", "especialidade": "Análise de Dados", "tarefas": 32},
        {"nome": "Agente Pesquisador", "status": "Ativo", "especialidade": "Busca e Pesquisa", "tarefas": 28},
        {"nome": "Agente Executor", "status": "Ativo", "especialidade": "Execução de Tarefas", "tarefas": 22},
        {"nome": "Agente Monitor", "status": "Standby", "especialidade": "Monitoramento", "tarefas": 0}
    ]

    for agente in agentes:
        status_color = "🟢" if agente["status"] == "Ativo" else "🟡"
        st.markdown(f"""
        <div class="agent-card">
            <h4>{status_color} {agente['nome']}</h4>
            <p><strong>Especialidade:</strong> {agente['especialidade']}</p>
            <p><strong>Status:</strong> {agente['status']} | <strong>Tarefas Processadas:</strong> {agente['tarefas']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Botão para criar novo agente
    if st.button("➕ Criar Novo Agente", type="primary"):
        st.success("✅ Novo agente criado com sucesso!")
        st.balloons()

with tab3:
    st.markdown("## 💬 Chat com Agentes")

    # Inicializar histórico do chat
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Olá! Sou o Sistema de Agentes Autônomos I2A2. Como posso ajudá-lo hoje?"}
        ]

    # Mostrar histórico do chat
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input do usuário
    if prompt := st.chat_input("Digite sua mensagem..."):
        # Adicionar mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Simular resposta do agente
        with st.chat_message("assistant"):
            with st.spinner("Agentes processando..."):
                time.sleep(2)  # Simular processamento

                # Respostas inteligentes baseadas na entrada
                if "análise" in prompt.lower() or "analisar" in prompt.lower():
                    response = f"🔍 **Agente Analista ativado!**\n\nAnalisando: '{prompt}'\n\n✅ Análise concluída:\n- Dados processados com sucesso\n- Padrões identificados\n- Relatório gerado\n\n📊 Resultado: Análise positiva com 94% de confiança."
                elif "pesquisa" in prompt.lower() or "buscar" in prompt.lower():
                    response = f"🔎 **Agente Pesquisador ativado!**\n\nPesquisando: '{prompt}'\n\n✅ Pesquisa concluída:\n- 127 fontes consultadas\n- Informações relevantes encontradas\n- Dados validados\n\n📚 Resultado: Pesquisa bem-sucedida!"
                elif "executar" in prompt.lower() or "fazer" in prompt.lower():
                    response = f"⚡ **Agente Executor ativado!**\n\nExecutando: '{prompt}'\n\n✅ Execução concluída:\n- Tarefa processada\n- Ações realizadas\n- Status: Sucesso\n\n🎯 Resultado: Tarefa executada com êxito!"
                else:
                    response = f"🤖 **Agente Coordenador respondendo:**\n\nProcessando: '{prompt}'\n\n✅ Resposta gerada:\n- Solicitação compreendida\n- Agentes especializados consultados\n- Resposta otimizada\n\n💡 Como posso ajudar mais?"

                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

with tab4:
    st.markdown("## 📈 Métricas e Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🎯 Performance dos Agentes")
        performance_data = {
            'Agente': ['Coordenador', 'Analista', 'Pesquisador', 'Executor', 'Monitor'],
            'Eficiência': [95, 92, 88, 90, 85],
            'Velocidade': [90, 95, 85, 92, 88]
        }
        df_performance = pd.DataFrame(performance_data)
        st.bar_chart(df_performance.set_index('Agente'))

    with col2:
        st.markdown("### ⏱️ Tempo de Resposta")
        tempo_data = {
            'Hora': [f"{i:02d}:00" for i in range(24)],
            'Tempo Médio (ms)': np.random.randint(100, 500, 24)
        }
        df_tempo = pd.DataFrame(tempo_data)
        st.line_chart(df_tempo.set_index('Hora'))

    # Métricas detalhadas
    st.markdown("### 📊 Métricas Detalhadas")

    metrics_col1, metrics_col2, metrics_col3 = st.columns(3)

    with metrics_col1:
        st.metric("Uptime", "99.9%", "0.1%")
        st.metric("Latência Média", "245ms", "-12ms")

    with metrics_col2:
        st.metric("Throughput", "1.2K req/min", "150 req/min")
        st.metric("Erro Rate", "0.1%", "-0.05%")

    with metrics_col3:
        st.metric("CPU Usage", "45%", "-5%")
        st.metric("Memory Usage", "2.1GB", "0.2GB")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🤖 Sistema de Agentes Autônomos I2A2 | Desenvolvido para Demonstração</p>
    <p>⚡ Powered by Streamlit | 🐳 Docker Ready | 🚀 Production Ready</p>
</div>
""", unsafe_allow_html=True)
