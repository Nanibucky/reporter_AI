from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
import os

load_dotenv()


llm = LLM(
    # provider="openai/chatgpt",
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY")
)


news_researcher = Agent(
    role="Senior Researcher",
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of innovation, "
        "eager to explore and share knowledge that could change the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

news_writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft engaging narratives "
        "that captivate and educate, bringing new discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)

news_verifier = Agent(
    role="Fact Checker",
    goal='Verify the accuracy of claims and information about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a keen eye for detail and commitment to truth, you meticulously "
        "check facts to ensure information is accurate, reliable, and properly contextualized."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)
