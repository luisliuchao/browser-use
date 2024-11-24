from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio

async def main():
    agent = Agent(
        task="Find a one-way flight from Bali to Oman on 12 January 2025 on Google Flights. Return me the cheapest option.",
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )
    result = await agent.run()
    print(result)
    
if __name__ == "__main__":
    asyncio.run(main())
