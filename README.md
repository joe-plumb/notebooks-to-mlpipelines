# Template for creating an AzureML Pipeline from a series of notebooks

Notebooks are great in the 'experimental phase' of a data science project - they allow you to quickly iterate over data for EDA and model building thanks to their interactive nature (REPL). However, notebooks can be cumbersome when it comes to industrializing our data science project, specifically:

* to run in an unattended mode on a schedule - particularly if a project has data prep, training and deployment phases.
* to ensure code conforms to standards (like PEP8)
* difficulty in code versioning (e.g. diff). 

Conversely, Azure Machine Learning pipelines help us to industrialize code but they do not execute in an interactive way as they are submitted to the AzureML execution service. Users that require an interactive experience (notebooks) in the initial phases of a project will often find that they need to re-factor their notebooks to run in an AzureML pipeline. Typical, re-factoring exercises include:

* converting notebooks to a python script (.py file)
* using `argparse` for parameters
* dealing with input datasets to the pipeline (file dataset) or direct method (tabular)
* handling data between pipeline steps

The purpose of this repo is to provide a template so that a user can get the best of both worlds. Users of this template can use notebooks in an AzureML Compute Instance to develop data prep and training processes in an interactive fashion, but then move those notebooks into a pipeline without having to re-factor. We do this by providing:

*  a set of data prep and training notebooks that:
    * Include the code for accessing data in such a way that it automatically uses the right approach for compute instance (interactive notebooks) or training cluster (unattended run in a pipeline). This means that no re-coding needs to take place when putting notebooks into a pipeline.
    * makes use of `argparse` such that users can set default parameters in interactive mode on a compute instance but are placeholders for the pipeline.
* a 'build pipeline' notebook that:
    * converts the notebooks in a pipeline into scripts
    * formats the scripts using yapf
    * runs linting on the scripts to catch trivial errors before we submit a pipeline
    * constructs a 2-step pipeline (data prep and training) - in due course we will update this template to include a model deployment step.
* a directory structure suitable for pipelines

### A note on folder structure

The repo folder structure is as follows:

```
notebooks-to-pipelines
│   README.md
│
└───notebooks
│   └───01-data-prep
│       │   data_prep.ipynb
│   └───02-train
│       │   training.ipynb
│
└───pipeline
│   └───scripts
│       └───01-data-prep
│           │   data_prep.py
│       └───02-train
│           │   training.py
│   ipynb_to_py.tpl
│   build_pipline.ipynb
│   conda_dependencies.yml
```

It should be noted that the scripts folder is auto-populated when using the  build_pipline notebook since we convert the data_prep and training notebooks into scripts using `nbconvert`. The workflow of this template is as follows:

### Step 1: Populate the Notebooks

In the notebooks folder we have created 2 templates:

* __01-data-prep/data_prep.ipynb__ put all of your data preparation steps in there. We seperate data prep from training because when we come to run things in a pipeline we get the benefit of modularization.

* __02-train/training.ipynb__ put your model training code in here

### Step 2: Run the pipeline/build_pipeline.ipynb notebook

Follow the pipeline/build_pipeline.ipynb notebook.


