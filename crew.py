from crewai import Crew
from tasks import research_task, write_task, verify_task
from dotenv import load_dotenv
load_dotenv()


def task_callback(output):
    return output 

verify_task.context = [write_task]


research_write_crew = Crew(
    agents=[research_task.agent, write_task.agent, verify_task.agent],
    tasks=[research_task, write_task, verify_task],
    verbose=True,
    process="sequential",
    task_callback=task_callback,
)

if __name__ == "__main__":
    article_result = research_write_crew.kickoff(inputs={'topic': 'How AI changes Gym activities?'})
    print("\n\n=== Final Result ===\n\n")
    print(article_result)
