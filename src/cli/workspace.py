import base64
from databricks.sdk import WorkspaceClient
from databricks.sdk.service import workspace as ws
from .config import Config


class WorkspaceDeployer:
    """
    Handles uploading notebooks to the Databricks workspace.
    Creates a structured folder under /Shared/mlops/<env>.
    """

    def __init__(self):
        cfg = Config()
        self.w = WorkspaceClient(host=cfg.host, token=cfg.token)
        self.env = cfg.env
        self.folder = f"/Shared/mlops/{self.env}"

    def deploy(self):
        print(f"📂 Creating/Updating workspace folder: {self.folder}")
        self.w.workspace.mkdirs(self.folder)

        notebooks = ["train_classification.py", "inference_batch.py"]
        for nb in notebooks:
            local_path = f"notebooks/{nb}"
            target_path = f"{self.folder}/{nb}"

            with open(local_path, "r", encoding="utf-8") as f:
                raw_content = f.read()
                encoded_content = base64.b64encode(raw_content.encode("utf-8")).decode("utf-8")

            self.w.workspace.import_(
                path=target_path,
                format=ws.ImportFormat.SOURCE,
                language=ws.Language.PYTHON,
                content=encoded_content,
                overwrite=True
            )

            print(f"✅ Uploaded {nb} → {target_path}")

        print("🚀 All notebooks uploaded successfully!")

