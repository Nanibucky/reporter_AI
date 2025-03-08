from crewai import Task
from tools import tool
from agents import news_researcher, news_writer, news_verifier

# Research task
research_task = Task(
    description=(
        "Identify the next big trend in {topic}. "
        "Focus on identifying pros and cons and the overall narrative. "
        "Your final report should clearly articulate key points, "
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3-paragraph report on the latest {topic} trends.',
    tools=[tool],
    agent=news_researcher,
)

# Writing task
write_task = Task(
    description=(
        "Compose an insightful article on {topic}. "
        "Focus on the latest trends and how they're impacting the industry. "
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output='A 4-paragraph article on {topic} advancements formatted as markdown.',
    tools=[tool],
    agent=news_writer,
    async_execution=False,
    output_file='reported_data.md'
)

# Verification task
verify_task = Task(
    description=(
        "Carefully verify the accuracy of the article about {topic}. "
        "Check all factual claims, statistics, and quotations for accuracy. "
        "Identify misleading statements or errors, and provide specific correction recommendations."
    ),
    expected_output='A verification report with fact-checking results and suggested corrections.',
    tools=[tool],
    agent=news_verifier,
    context=[]  
)
