# 🧠 mlops_databricks_pipeline
   
### Author: **Aneesh Koka**

---

## 📘 Project Overview
This project implements a **complete MLOps pipeline** using **Databricks**, **MLflow**, and **GitHub Actions**.  
It automates every stage of the machine-learning lifecycle — from model training to deployment — with reproducibility and CI/CD built in.

### 🔹 Core Objectives
- Train and register an ML model on Databricks using MLflow  
- Perform batch inference from the registered model  
- Automatically deploy notebooks and jobs via the Databricks SDK  
- Enable continuous deployment to production with GitHub Actions  

---

## ⚙️ System Architecture
mlops_takehome/
├── notebooks/
│ ├── train_classification.py # Trains and logs model to MLflow
│ └── inference_batch.py # Loads registered model and performs inference
├── src/cli/
│ ├── config.py # Loads Databricks credentials and environment variables
│ ├── workspace.py # Handles notebook uploads to Databricks workspace
│ ├── jobs.py # Creates & configures Databricks Jobs programmatically
│ └── main.py # CLI entrypoint
├── mlops_cli.py # Top-level CLI runner for local deployment
├── requirements.txt
└── .github/workflows/deploy.yml # GitHub Actions workflow for CI/CD to production


---

## 🧩 Local Setup Instructions

### 1️⃣ Clone Repository and Set Up Virtual Environment
```bash
git clone https://github.com/Anee-Ark/mlops_databricks_pipeline.git
cd mlops_databricks_pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 2️⃣ Configure Databricks Credentials
Generate a **Personal Access Token** in Databricks → *User Settings → Developer → Access Tokens*  
Then export your environment variables:

```bash
export DATABRICKS_HOST="https://dbc-011d092b-b40f.cloud.databricks.com"
export DATABRICKS_TOKEN="dapiXXXXXXXXXXXX"
export ENV=dev

### 3️⃣ Run the CLI Locally (Dev Deployment)

Once your environment variables are set, you can deploy your notebooks and create Databricks Jobs locally for the **development environment** by running:

```bash
python mlops_cli.py

✅ What this command does

Uploads both notebooks to your Databricks workspace under:
/Shared/mlops/dev

Creates two scheduled Databricks jobs:

mlops_dev_train → Runs the training notebook every 30 days

mlops_dev_infer → Runs the inference notebook daily

🧠 Verify the deployment in Databricks

After successful execution:

1. Navigate to Workspace → Shared → mlops → dev
You should see:
```bash
train_classification.py
inference_batch.py

2. Navigate to Workflows → Jobs
You should see two jobs created automatically:

mlops_dev_train

mlops_dev_infer

## 🚀 CI/CD Automation (GitHub Actions)

To enable continuous deployment to production, the project includes a fully automated **GitHub Actions workflow** that runs every time you push to the `main` branch.  
This workflow deploys your notebooks and jobs to the **production** environment on Databricks.

---

### GitHub Secrets Setup

Before running the workflow, you need to add your Databricks credentials as GitHub Actions secrets.

1. Go to your GitHub repo → **Settings → Secrets and variables → Actions**
2. Click **“New repository secret”** for each of the following:

| Secret Name | Example Value |
|--------------|----------------|
| `DATABRICKS_HOST` | `https://dbc-011d092b-b40f.cloud.databricks.com` |
| `DATABRICKS_TOKEN` | `dapiXXXXXXXXXXXX` |
| `ENV` | `prod` |

These secrets will be automatically injected into the workflow environment.

---


### Deployment Triggers

Automatically runs on every push to main

Manually triggered via “Run workflow” button in GitHub Actions tab

When executed, it deploys to:

/Shared/mlops/prod/

and creates:

mlops_prod_train

mlops_prod_infer

### 4️⃣ Production Deployment Output

When the workflow runs successfully (either automatically or manually), it will:

✅ Upload your production notebooks to:
/Shared/mlops/prod/


✅ Create two scheduled Databricks jobs:
- **`mlops_prod_train`** → runs the training notebook every 30 days  
- **`mlops_prod_infer`** → runs the inference notebook daily  

---

### 🧠 Verification Steps

After the GitHub Actions workflow completes (green ✅ in the **Actions** tab):

1. Open your Databricks workspace.  
2. Navigate to:
Workspace → Shared → mlops → prod
You should see:
train_classification.py
inference_batch.py

3. Navigate to:
Workflows → Jobs


You’ll find two new jobs:
- `mlops_prod_train`
- `mlops_prod_infer`

This confirms your **production CI/CD pipeline** is fully functional and synchronized with GitHub.

---

### 🧾 CI/CD Highlights

| Capability | Description |
|-------------|--------------|
| **Continuous Deployment** | Every push to `main` automatically updates production notebooks and jobs. |
| **Environment Promotion** | Uses `ENV=prod` to separate dev and production environments. |
| **Secure Authentication** | Leverages GitHub Secrets for Databricks credentials (no hardcoded tokens). |
| **Reusability** | Reuses the same CLI (`mlops_cli.py`) for both local and CI/CD deployments. |
| **Zero Manual Steps** | End-to-end automation from GitHub → Databricks. |

---

### 📈 Validation Evidence

✅ **Development deployment:**  
- `/Shared/mlops/dev` created via local CLI (`ENV=dev`)  

✅ **Production deployment (CI/CD):**  
- `/Shared/mlops/prod` created automatically via GitHub Actions  

✅ **Deployed notebooks:**  
- `train_classification.py`  
- `inference_batch.py`  

✅ **Jobs created:**  
- `mlops_dev_train`  
- `mlops_dev_infer`  
- `mlops_prod_train`  
- `mlops_prod_infer`

✅ **MLflow integration:**  
- Model registered as `iris_rf_model`  
- Accuracy: 1.0 (RandomForestClassifier)  
- Versioned in MLflow Model Registry  

---

### 🧾 Deliverables Summary (Rubric Alignment)

| Requirement | Implemented | Evidence |
|--------------|-------------|-----------|
| **Notebook Training & Inference** | ✅ | `notebooks/` folder |
| **Model Registry Integration (MLflow)** | ✅ | `train_classification.py` |
| **CLI Automation (Databricks SDK)** | ✅ | `mlops_cli.py` + `src/cli` modules |
| **Job Creation via API** | ✅ | Verified in Databricks Workflows |
| **CI/CD Workflow (GitHub Actions)** | ✅ | `.github/workflows/deploy.yml` |
| **Environment-based Deployment (dev/prod)** | ✅ | `ENV` variable toggle |
| **Code Quality & Config Management** | ✅ | Modular design, OOP structure |

---

### 🧠 Key Learnings & Reflection

This project demonstrates **end-to-end MLOps automation** using Databricks and GitHub Actions:

- **Reproducibility:** All experiments logged with MLflow  
- **Scalability:** Jobs and workspaces created programmatically via Databricks SDK  
- **Maintainability:** Clean environment separation (`dev` vs `prod`)  
- **Automation:** CI/CD ensures continuous deployment without manual intervention  

Through this take-home, I reinforced my understanding of **MLOps orchestration**, **cloud automation**, and **model lifecycle management**.

---

### 🏁 Final Status

✅ Local (Dev) deployment — working  
✅ Production (Prod) CI/CD deployment — working  
✅ Databricks Jobs visible in both environments  
✅ MLflow Model Registry integrated  
✅ Repository ready for submission 🎯  

---

### 👤 Author

**Aneesh Koka**  
AI Engineer & MLOps Practitioner  
📧 Email: `koka.a@northeastern.edu`  
🔗 GitHub: [Anee-Ark/mlops_databricks_pipeline](https://github.com/Anee-Ark/mlops_databricks_pipeline)

