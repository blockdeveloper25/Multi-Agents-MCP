import asyncio

from dotenv import load_dotenv
from langchain_groq import ChatGroq

from mcp_use import MCPClient, MCPAgent
import os

async def run_memory_chat():
    
    load_dotenv()
    os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")
    
    config_file = "browser_mcp.json"
    
    print("initializing chat...")
    
    client = MCPClient.from_config_file(config_file)
    llm = ChatGroq(
        model="llama3-70b-8192",  # more stable with LangChain tools
        temperature=0.7
    )


    
    agent = MCPAgent(
        llm=llm,
        client=client,
        memory_enabled=True,
        max_steps=15
    )
    
    print("starting chat...")
    print("Type 'exit' to end the chat.")
    print("Type 'clear' to clear the memory.")
    
    try:
        while True:
            user_input = input("\nYou: ")
            
            if user_input.lower() == "exit":
                print("Exiting chat...")
                break
            elif user_input.lower() == "clear":
                agent.memory.clear()
                print("Memory cleared.")
                continue
            print("\nAssistant:", end="",flush=True)
            
            try:
                response = await agent.run(user_input)
                print(response)
           
            except Exception as e:
                print(f"\nError: {e}")
    finally:
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
