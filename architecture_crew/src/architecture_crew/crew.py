from pathlib import Path
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from architecture_crew.tools.custom_tool import FileReaderTool, DirectoryListTool, FindFilesTool


@CrewBase
class ArchitectureCrew:
    """
    Architecture Crew - System Design & Specifications

    Agent:
    - Software Architect: Designs system architecture and creates detailed specifications

    Inputs:
    - Strategy crew outputs (technical-analysis.md, market-research.md, product-roadmap.md, plugin-metadata.json)
    - Skeleton plugin (for understanding conventions)

    Outputs:
    - High-level architecture document
    - Complete folder structure (JSON)
    - Per-class backend specifications
    - Per-component frontend specifications
    - Database schema design
    - API contracts
    """

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        super().__init__()
        # Compute project root dynamically based on this file's location
        # crew.py is at: architecture_crew/src/architecture_crew/crew.py
        # Go up 3 levels to reach dev-team root
        self.project_root = Path(__file__).parent.parent.parent.parent
        self.outputs_dir = self.project_root / "outputs" / "architecture"

    @agent
    def software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['software_architect'],
            tools=[
                FileReaderTool(),
                DirectoryListTool(),
                FindFilesTool()
            ],
            verbose=True
        )

    @task
    def read_strategy_outputs(self) -> Task:
        return Task(
            config=self.tasks_config['read_strategy_outputs'],
            output_file=str(self.outputs_dir / "strategy-summary.md")
        )

    @task
    def design_high_level_architecture(self) -> Task:
        return Task(
            config=self.tasks_config['design_high_level_architecture'],
            context=[self.read_strategy_outputs()],
            output_file=str(self.outputs_dir / "high-level-architecture.md")
        )

    @task
    def define_folder_structure(self) -> Task:
        return Task(
            config=self.tasks_config['define_folder_structure'],
            context=[self.read_strategy_outputs(), self.design_high_level_architecture()],
            output_file=str(self.outputs_dir / "folder-structure.json")
        )

    @task
    def create_backend_specs(self) -> Task:
        return Task(
            config=self.tasks_config['create_backend_specs'],
            context=[self.read_strategy_outputs(), self.design_high_level_architecture(), self.define_folder_structure()],
            output_file=str(self.outputs_dir / "specs" / "backend")
        )

    @task
    def create_frontend_specs(self) -> Task:
        return Task(
            config=self.tasks_config['create_frontend_specs'],
            context=[self.read_strategy_outputs(), self.design_high_level_architecture(), self.define_folder_structure(), self.create_backend_specs()],
            output_file=str(self.outputs_dir / "specs" / "frontend")
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Architecture crew with sequential execution"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

