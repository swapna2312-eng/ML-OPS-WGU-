from databricks.sdk import WorkspaceClient
from databricks.sdk.service import jobs
from .config import Config

class JobBuilder:
    """Creates Databricks Jobs (training + inference) under /Shared/mlops/<env>."""
    
    def __init__(self):
        cfg = Config()
        self.w = WorkspaceClient(host=cfg.host, token=cfg.token)
        self.env = cfg.env
        self.folder = f"/Shared/mlops/{self.env}"
    
    def create_or_update_train_job(self):
        job_name = f"mlops_{self.env}_train"
        
        self.w.jobs.create(
            name=job_name,
            schedule=jobs.CronSchedule(
                quartz_cron_expression="0 0 1 * * ?",
                timezone_id="UTC"
            ),
            tasks=[
                jobs.Task(
                    task_key="train",
                    notebook_task=jobs.NotebookTask(
                        notebook_path=f"{self.folder}/train_classification.py"
                    ),
                    # Remove new_cluster - will use serverless compute
                )
            ],
        )
        print(f"✅ Created training job: {job_name}")
    
    def create_or_update_infer_job(self):
        job_name = f"mlops_{self.env}_infer"
        
        self.w.jobs.create(
            name=job_name,
            schedule=jobs.CronSchedule(
                quartz_cron_expression="0 0 * * * ?",
                timezone_id="UTC"
            ),
            tasks=[
                jobs.Task(
                    task_key="inference",
                    notebook_task=jobs.NotebookTask(
                        notebook_path=f"{self.folder}/inference_batch.py"
                    ),
                    # Remove new_cluster - will use serverless compute
                )
            ],
        )
        print(f"✅ Created inference job: {job_name}")
