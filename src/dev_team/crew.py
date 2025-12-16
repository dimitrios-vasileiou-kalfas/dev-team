"""
Legacy crew.py - DEPRECATED

This file is kept for backwards compatibility.
The project now uses a two-crew architecture:

- crews/strategy_crew.py - Competitor analysis + Product roadmap
- crews/development_crew.py - Architecture + Implementation + Testing

To run the new workflow:
    crewai run

Or use the orchestrator directly:
    python src/dev_team/orchestrator.py
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List


@CrewBase
class DevTeam():
    """
    DEPRECATED: Legacy DevTeam crew

    Please use:
    - StrategyCrew (crews/strategy_crew.py)
    - DevelopmentCrew (crews/development_crew.py)
    """

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor_analyst'], # type: ignore[index]
            verbose=True
        )

    @agent
    def product_manager(self) -> Agent:
        return Agent(
            config=self.agents_config['product_manager'], # type: ignore[index]
            verbose=True
        )

    @task
    def analyze_competitor(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_competitor'], # type: ignore[index]
        )

    @task
    def create_roadmap(self) -> Task:
        return Task(
            config=self.tasks_config['create_roadmap'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the legacy DevTeam crew (Strategy only)"""
        print("⚠️  WARNING: Using legacy DevTeam crew. Consider using StrategyCrew and DevelopmentCrew instead.")

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
