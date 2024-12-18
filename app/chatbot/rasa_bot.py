import logging
from rasa.core.agent import Agent

agent = Agent.load("models")

async def process_message(message: str):
    try:
        responses = await agent.handle_text(message)
        logging.info(f"Rasa response: {responses}")
        if responses:
            return responses[0].get("text", "No response available.")
        return "No response from Rasa."
    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return "Sorry, I could not process your request."
