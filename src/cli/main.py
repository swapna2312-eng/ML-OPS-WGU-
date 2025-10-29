import typer
from .workspace import WorkspaceDeployer
from .jobs import JobBuilder

def deploy_all():
    """Upload notebooks and create both jobs."""
    WorkspaceDeployer().deploy()
    jb = JobBuilder()
    jb.create_or_update_train_job()
    jb.create_or_update_infer_job()
    print("🚀 All jobs deployed!")

# Create the Typer app AFTER defining the function
app = typer.Typer(help="MLOps Takehome CLI")
app.command("deploy-all")(deploy_all)

if __name__ == "__main__":
    app()



