import argparse
import tempfile
import os
import logging
import pandas as pd
from azureml.core import Dataset, Workspace, Datastore
from azureml.data import TabularDataset, FileDataset
from azureml.core.run import _OfflineRun, Run

parser = argparse.ArgumentParser()
parser.add_argument("--input_dataset",
                    default="",
                    help="the input dataset name")
parser.add_argument("--output_folder",
                    default="outputs",
                    help="the folder name where you want to place outputs")
args, _ = parser.parse_known_args()

dataset_name1 = args.input_dataset
output_folder = args.output_folder


def get_registered_dataset(dataset_name):
    run = Run.get_context()
    dset = None
    mount_folder = ''

    if isinstance(run, _OfflineRun):
        ws = Workspace.from_config()
        dset = Dataset.get_by_name(ws, dataset_name)

        if isinstance(dset, FileDataset):
            mount_folder = tempfile.mkdtemp()
            ws = Workspace.from_config()
            dset = Dataset.get_by_name(ws, dataset_name)
            print('This is a file dataset and therefore mounting to ' +
                  mount_folder)
            mount_context = dset.mount(mount_folder)
            mount_context.start()
    else:
        ws = run.experiment.workspace
        print("dataset name " + dataset_name)
        dset = run.input_datasets[dataset_name]
        print(dset)
        if isinstance(dset, str):
            mount_folder = dset
            print(
                'This is a file dataset and therefore it has already been mounted to '
                + mount_folder)
            print('contents of folder')
            print(os.listdir(mount_folder))

    return dset, mount_folder


dataset, mount_folder = get_registered_dataset(dataset_name1)

# if the dataset is tabular type and you want to render it into pandas dataframe use:
# dataframe = dataset.to_pandas_dataframe()

# if the dataset is tabular and you want to render it into a spark dataframe use:
# dataframe = dataset.to_spark_dataframe()

# if you want to take (say) a 10% sample of a tabular dataset use:
# dataframe = dataset.take_sample(probability=0.10).to_pandas_dataframe()

# if you want to take the top n number of data points from a tabular dataset use:
# dataframe = dataset.take(100).to_pandas_dataframe()

# if using a file dataset then you can view the mounted files using:
# os.listdir(mount_folder)

os.makedirs(output_folder, exist_ok=True)

# below you should write your training sets (or any other data required for training) into the folder created above e.g.
# file_path = os.path.join(output_folder, 'training_data.csv')
# pd.to_csv(file_path)
