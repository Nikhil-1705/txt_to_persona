from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, FileWriterTool
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 


@CrewBase
class Txtpersona():
	"""Txtpersona crew"""


	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def Reader(self) -> Agent:
		return Agent(
			config=self.agents_config['Reader'],
			tools=[FileReadTool(file_path=os.getenv("USERS_FILE_PATH"))],
			verbose=True
		)

	@agent
	def formatter_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['formatter_agent'],
			tools = [],
			llm = "gpt-4o",
			verbose=True
		)
	@agent
	def evaluator_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['evaluator_agent'],
			tools = [],
			verbose=True
		)
	@agent
	def merger_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['merger_agent'],
			tools = [],
			verbose=True
		)
	@agent
	def file_writer_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer_agent'],
			tools = [FileWriterTool()],
			verbose=True
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def read_user_data(self) -> Task:
		return Task(
			config=self.tasks_config['read_user_data'],
		)
  
	@task
	def format_user_persona(self) -> Task:
		return Task(
			config=self.tasks_config['format_user_persona'],
		)
	@task
	def evaluate_completeness(self) -> Task:
		return Task(
			config=self.tasks_config['evaluate_completeness'],
		)
	@task
	def merge_persona_evaluation(self) -> Task:
		return Task(
			config=self.tasks_config['merge_persona_evaluation'],
		)
	@task
	def file_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_write_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Txtpersona crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
