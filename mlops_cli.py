import typer
from src.cli.workspace import WorkspaceDeployer
from src.cli.jobs import JobBuilder

app = typer.Typer(help="MLOps Takehome CLI")

@app.command(name="deploy-all")
def deploy_all():
    """Upload notebooks and create both jobs."""
    WorkspaceDeployer().deploy()
    jb = JobBuilder()
    jb.create_or_update_train_job()
    jb.create_or_update_infer_job()
    print("🚀 All jobs deployed!")

if __name__ == "__main__":
    app()

