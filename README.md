# Identifying Key Markers in At-Risk Heart Disease Patients

In this project, we will look at a heart failure dataset with 12 data points for each patient. These data points, along with whether a patient ended up dying, will be looked at in both an AutoML and HyperDrive run to identify which characteristics are the most important in determining if someone is the most at-risk for heart failure. By the end of this project, we will have completed the AutoML and HyperDrive runs, determined which has superior accuracy in determining heart failure, and created a web service endpoint for requests.

## Project Set Up and Installation
I encountered some issues with deprecated packages that weren't imported properly. Before starting, I did a pip install -upgrade for the azureml-core package.

## Dataset

### Overview
The data is a pull from Kaggle that includes approximately 300 patients' medical records across 12 different data points. These data points include:
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
For the AutoML run, we chose a classification task in order to label each patient as someone who was predicted to be dead or alive. The column we were looking to predict was the "DEATH_EVENT" column and was called out as the "label_column_name". We set featurization to "auto", the primary metric to "accuracy", training data to the heart data set that was uploaded, the compute cluster as the cluster that was automatically set up for us, and the timeout for 20 minutes. We also set cross-validations to 5, concurrent iterations to 4, and named the error logging file.

### Results
The AutoML run lasted for 12 minutes and 31 seconds. It iterated 61 times and found that the best algorithm was the VotingEnsemble. The voting ensemble was able to predict the patients being alive or dead correctly 88.97% of the time. The parameters for the run were -C and -max-iters. We could have run more iterations to find a better algorithm.

![AutoML Run Details](https://github.com/gbnuhg/udacity_ml_nano_capstone/assets/132493261/864c46a9-0c1b-4602-b462-fbb36ba6da61)
![AutoML Best Run](https://github.com/gbnuhg/udacity_ml_nano_capstone/assets/132493261/7d576868-b482-457e-9976-26f643ad0462)

## Hyperparameter Tuning
I chose a classification model for my HyperDrive run to predict whether someone died of heart failure or not. Random sampling was used with a parameter space of {--C:[loguniform,[-3,3]], --max-iters:[choice,[[100,200,300,400]]]}. I set up a Bandit early termination policy and created the environment for the run from my accompanying conda dependencies.

### Results
The best iteration with this HyperDrive run was a prediction of 88.33% accuracy - lower than that of the AutoML run. The parameters of this run were: --C = 0.109382 and --max_iter = 200. To improve, we could have included more options for the different parameter sampling and completed more iterations.

![HyperDrive Run Details](https://github.com/gbnuhg/udacity_ml_nano_capstone/assets/132493261/2a70742b-70a9-43af-93f0-a3f79e858e93)
![HyperDrive Best Run](https://github.com/gbnuhg/udacity_ml_nano_capstone/assets/132493261/241f3aa8-0699-46b5-b372-b2b86eeb77ec)

## Model Deployment
Since the AutoML run was superior, we deployed it instead of the HyperDrive run. We downloaded a template score file and named it score_new.py since the score.py file I created was running into issues. With that and the environment from the best run, we created an inference configuration. The deployment config was created with the ACI Webservice where we enabled authentication. We then deployed the model and named it "service". We pulled the scoring URL and key from the deployment and added it to the endpoint.py file.

Once deployed, we created an endpoint.py script with test data to use against the endpoint. When calling that endpoint.py file, the model predicted that both of the patients had died.
![Endpoint](https://github.com/gbnuhg/udacity_ml_nano_capstone/assets/132493261/e52238fe-a7b5-47f2-8d9a-2c6bd4416b33)

## Screen Recording
The screencast can be found at the following link: https://youtu.be/p9Al-zsuA5o
