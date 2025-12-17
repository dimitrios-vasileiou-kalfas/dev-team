from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from dev_team.tools.custom_tool import FileReaderTool, DirectoryListTool, FindFilesTool


@CrewBase
class StrategyCrew:
    """
    Strategy & Planning Crew

    Agents:
    - Market Researcher: Analyzes user needs, reviews, market gaps
    - Competitor Analyst: Analyzes competitor plugin technically
    - Product Manager: Creates milestone-based roadmap

    Output: Analysis reports and product roadmap in outputs/analysis/
    """

    agents_config = '../config/agents.yaml'
    tasks_config = '../config/strategy_tasks.yaml'

    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['market_researcher'],
            verbose=True
        )

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor_analyst'],
            tools=[
                DirectoryListTool(),
                FileReaderTool(),
                FindFilesTool()
            ],
            verbose=True

        )

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'],
            verbose=True
        )

    @task
    def analyze_competitor(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_competitor']
        )

    @task
    def research_market(self) -> Task:
        return Task(
            config=self.tasks_config['research_market'],
            context=[self.analyze_competitor()]  # Uses competitor analysis as context
        )

    @task
    def create_roadmap(self) -> Task:
        return Task(
            config=self.tasks_config['create_roadmap'],
            context=[self.analyze_competitor(), self.research_market()]  # Uses both as context
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Strategy & Planning crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

