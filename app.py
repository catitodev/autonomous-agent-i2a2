import streamlit as st
import os
from dotenv import load_dotenv
from src.agents.coordinator import AgentCoordinator
from src.memory.manager import MemoryManager
from src.config.settings import Settings
from frontend.components.chat import ChatInterface
from frontend.components.sidebar import Sidebar
from frontend.components.metrics import MetricsPanel
from frontend.styles.custom_css import load_custom_css

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Autonomous Agent I2A2",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_custom_css()

def main():
    # Header
    st.markdown('''
    <div class="main-header">
        <h1>🤖 Autonomous Agent I2A2</h1>
        <p>Agente Inteligente com Capacidades Avançadas</p>
    </div>
    ''', unsafe_allow_html=True)

    # Initialize components
    if 'agent' not in st.session_state:
        st.session_state.agent = AgentCoordinator()
        st.session_state.memory = MemoryManager()
        st.session_state.messages = []

    # Layout
    col1, col2 = st.columns([3, 1])

    with col1:
        # Main chat interface
        ChatInterface(st.session_state.agent, st.session_state.messages)

    with col2:
        # Sidebar with controls and metrics
        Sidebar()
        MetricsPanel()

if __name__ == "__main__":
    main()
