from pathlib import Path
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from architecture_crew.tools.custom_tool import FileReaderTool, DirectoryListTool, FindFilesTool, FileWriterTool



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
        # Use local symlink to shared outputs (no path traversal)
        # architecture_crew/outputs -> ../outputs/architecture (symlink)
        # This avoids Pydantic's path traversal validation errors
        self.outputs_dir = Path("outputs")

    @agent
    def software_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['software_architect'],
            tools=[
                FileReaderTool(),
                DirectoryListTool(),
                FindFilesTool(),
                FileWriterTool()
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
            context=[self.read_strategy_outputs(), self.design_high_level_architecture(), self.define_folder_structure()]
            # Note: output_file removed - this task creates multiple files via write_file tool
        )

    @task
    def create_frontend_specs(self) -> Task:
        return Task(
            config=self.tasks_config['create_frontend_specs'],
            context=[self.read_strategy_outputs(), self.design_high_level_architecture(), self.define_folder_structure(), self.create_backend_specs()]
            # Note: output_file removed - this task creates multiple files in specs/frontend/
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

