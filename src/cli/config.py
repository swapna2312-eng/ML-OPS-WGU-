import os
from dataclasses import dataclass

@dataclass
class Config:
    host: str = os.getenv("DATABRICKS_HOST")
    token: str = os.getenv("DATABRICKS_TOKEN")
    env: str = os.getenv("ENV", "dev")

