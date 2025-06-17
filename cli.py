#!/usr/bin/env python3
import asyncio
import sys
from src.agents.coordinator import AgentCoordinator

async def main():
    if len(sys.argv) < 2:
        print("Uso: python cli.py 'Sua pergunta aqui'")
        sys.exit(1)

    question = " ".join(sys.argv[1:])

    print("Inicializando Agente Autônomo...")
    agent = AgentCoordinator()

    print(f"Pergunta: {question}")
    print("Processando...")

    response = await agent.process_message(question)

    if response["success"]:
        print(f"Resposta: {response['response']}")
        if response.get("tools_used"):
            print(f"Ferramentas utilizadas: {', '.join(response['tools_used'])}")
    else:
        print(f"Erro: {response.get('error', 'Erro desconhecido')}")

if __name__ == "__main__":
    asyncio.run(main())
