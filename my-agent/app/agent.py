
from google.adk.agents import Agent, SequentialAgent
from google.adk.apps.app import App



root_agent = SequentialAgent(
    name="root_agent",
    model="gemini-3-pro-preview",
    instruction="You are a helpful AI assistant designed to provide accurate and useful information.",
    sub_agents=[sub_agent1, sub_agent2],  # Assume sub_agent1 and sub_agent2 are defined elsewhere
)
app = App(root_agent=root_agent, name="app")
