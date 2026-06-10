from crewai import Agent, Crew, Process, Task, LLM
from crewai_tools import SerperDevTool

from phoenix.otel import register
from dotenv import load_dotenv
import os

load_dotenv()

tracer_provider = register(project_name="crewai-tracing-quickstart", auto_instrument=True)

search_tool = SerperDevTool()

llm = LLM(model="groq/llama-3.3-70b-versatile")

researcher = Agent(
    role="Financial Research Analyst",
    goal="Gather up-to-date financial data, trends, and news for the target companies or markets",
    backstory="""
        You are a Senior Financial Research Analyst.
    """,
    verbose=True,
    allow_delegation=False,
    max_iter=1,
    tools=[search_tool],
    llm=llm
)

writer = Agent(
    role="Financial Report Writer",
    goal="Compile and summarize financial research into clear, actionable insights",
    backstory="""
        You are an experienced financial content writer.
    """,
    verbose=True,
    allow_delegation=False,
    max_iter=1,
    llm=llm
)

task1 = Task(
    description="""
        Research: {tickers}
        Focus on: {focus}
    """,
    expected_output="Detailed financial research summary with web search findings",
    agent=researcher,
)

task2 = Task(
    description="Write a report based on the research above.",
    expected_output="A polished financial analysis report",
    agent=writer,
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=True,
    process=Process.sequential,
)

user_inputs = {
    "tickers": "TSLA",
    "focus": "financial analysis and market outlook"
}

result = crew.kickoff(inputs=user_inputs)