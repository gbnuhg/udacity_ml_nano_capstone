*NOTE:* This file is a template that you can use to create the README for your project. The *TODO* comments below will highlight the information you should be sure to include.

# Identifying Key Markers in At-Risk Heart Disease Patients

In this project we will be looking at a heart failure dataset with 12 data points for each patient. These datapoints, along with whether a patient ended up dying, will be looked at in both an AutoML and HyperDrive run to identify which characteristics are the most important in determining if someone is the most at-risk for heart failure. By the end of this project, we will have completed the AutoML and HyperDrive runs, determined which has superior accuracy in determining heart failure, and created an webservice endpoint for requests.

## Project Set Up and Installation
I encountered some issues with deprecated packages that weren't imported properly. Before starting, I did a pip install -upgrade for the azureml-core package.

## Dataset

### Overview
The data is a pull from Kaggle that includes approximately 300 patients medical records across 12 different data points. These datapoints include:
- age
- anaemia
- creatinine_phosphokinase
- diabetes
- ejection_fraction
- high_blood_pressure
- platelets
- serum_creatinine
- serum_sodium
- sex
- smoking
- time

The data also includes whether or not the patient died, labeled "DEATH_EVENT". This will be the data point that we will attempt to predict.

### Task
We will be attempting to predict the "DEATH_EVENT" column through a classification model. We will be using this model on both an AutoML and HyperDrive run.

### Access
The data was uploaded as a Tabular dataset to ml.azure.com. It can also be found within this GitHub repo if you are looking to replicate any of my findings.

## Automated ML
For the AutoML run, we chose a classification task in order to label each patient as someone who was predicted to be dead or alive. The column we were looking to predict was the "DEATH_EVENT" column and was called out as the "label_column_name". We set featurization to "auto", the primary metric to "accuracy", training data to the heart data set that was uploaded, the compute cluster as the cluster that was automatically set up for us, and the timeout for 20 mintues. We also set cross validations to 5, concurrent iterations to 4, and named the error logging file.

### Results
The AutoML run lasted for 12 minutes and 31 seconds. It iterated 61 times and found that the best algorithm was the VotingEnsemble. The voting ensemble was able to predict the patients being alive or dead correctly 88.97% of the time. The parameters for the run were -C and -max-iters. We could have ran more iterations to find a better algorithm.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
I chose a classification model for my HyperDrive run to predict whether someone died of heart failure or not. Random sampling was used with a parameter space of {--C:[loguniform,[-3,3]], --max-iters:[choice,[[100,200,300,400]]]}. I set up a Bandit early termination policy and created the environment for the run from my accompanying conda dependencies.

### Results
The best iteration with this HyperDrive run was a prediction of 88.33% accuracy - lower than that of the AutoML run. The parameters of this run were: --C = 0.109382 and --max_iter = 200. To improve, we could have include more options for the different parameter sampling and to compelte more iterations.

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.
Since the AutoML run was superior, we deployed it instead of the HyperDrive run. We downloaded a template score file and named it score_new.py since the score.py file I created was running into issues. With that and the environment from the best run, we created an inference configuration. The deployment config was created with the ACI Webservice where we enabled authentication. We then deployed the model and named it service.

Once deployed, we created an endpoint.py script with test data to use against the endpoint. When calling that endpoint.py file, the model predicted that both of the patients had died.

## Screen Recording
The screencast can be found at the following link: https://youtu.be/p9Al-zsuA5o
