import mlflow
import dagshub
import json
from mlflow import MlflowClient

import dagshub

import dagshub
dagshub.init(repo_owner='Naman12769', repo_name='uber-demand-prediction', mlflow=True)

# set the mlflow tracking uri
mlflow.set_tracking_uri("https://dagshub.com/Naman12769/uber-demand-prediction.mlflow")


def load_model_information(file_path):
    with open(file_path) as f:
        run_info = json.load(f)
        
    return run_info

registered_model_name="uber_demand_prediction_model"
stage="Staging"

client=MlflowClient()

latest_version=client.get_latest_versions(name=registered_model_name,stages=[stage])

latest_model_version_staging=latest_version[0].version
promote_stage="Production"
model_version_prod=client.transition_model_version_stage(name=registered_model_name,version=latest_model_version_staging,stage=promote_stage,archive_existing_versions=True)

production_version=model_version_prod.version
new_stage=model_version_prod.current_stage

print(f"The model is moved to the {new_stage} stage having version number {production_version}")