import argparse
import tempfile
import os
import logging
import sklearn
import pandas as pd
from azureml.core import Dataset, Workspace, Datastore
from azureml.data import TabularDataset, FileDataset
from azureml.core.run import _OfflineRun, Run

parser = argparse.ArgumentParser()
parser.add_argument("--training_data",
                    type=str,
                    default="../01-data-prep/outputs/training_data.csv",
                    help="file path for ")
parser.add_argument("--param1",
                    type=float,
                    default=1.00,
                    help="a parameter for an ML model")

args, _ = parser.parse_known_args()

training_data = args.training_data
output_folder = ".outputs"
param1 = args.param1

os.makedirs(output_folder, exist_ok=True)

# below you should write your training sets (or any other data required for training) into the folder created above e.g.
# model_path = os.path.join(output_folder, 'model.pkl')
# model.save('model.pkl')
