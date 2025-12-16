from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class DevelopmentCrew:
    """
    Development & QA Crew

    Agents:
    - Software Architect: Designs architecture following SOLID principles
    - WordPress Backend Developer: Implements PHP backend (includes/, src/)
    - React Frontend Developer: Implements admin UI (admin-react/)
    - Code Reviewer: Reviews code for bugs, security, best practices
    - QA Engineer: Runs tests and validates integration

    Output: Working plugin code in outputs/plugin/
    """

    agents_config = '../config/agents.yaml'
    tasks_config = '../config/development_tasks.yaml'

    @agent
    def software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['software_architect'],
            verbose=True
        )

    @agent
    def wordpress_backend_dev(self) -> Agent:
        return Agent(
            config=self.agents_config['wordpress_backend_dev'],
            verbose=True
        )

    @agent
    def react_frontend_dev(self) -> Agent:
        return Agent(
            config=self.agents_config['react_frontend_dev'],
            verbose=True
        )

    @agent
    def code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['code_reviewer'],
            verbose=True
        )

    @agent
    def qa_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['qa_engineer'],
            verbose=True
        )

    @task
    def design_architecture(self) -> Task:
        return Task(
            config=self.tasks_config['design_architecture']
        )

    @task
    def implement_backend(self) -> Task:
        return Task(
            config=self.tasks_config['implement_backend']
        )

    @task
    def implement_frontend(self) -> Task:
        return Task(
            config=self.tasks_config['implement_frontend']
        )

    @task
    def review_code(self) -> Task:
        return Task(
            config=self.tasks_config['review_code']
        )

    @task
    def run_qa_tests(self) -> Task:
        return Task(
            config=self.tasks_config['run_qa_tests']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Development & QA crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

