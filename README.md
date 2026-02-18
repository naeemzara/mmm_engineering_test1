# mmm_engineering_test1
**MMM Engineering_QC and Testing **

**Introduction** 
Marketing Mix Modeling is used by marketers and advertisers to measure advertising effectiveness, reallocate spends across media channels and use in forecasting and optimization for ROI maximization. Taking a Bayesian approach to MMM allows advertisers to integrate prior information into modeling to account for uncertainty with model and parameters. Medis saturation, adstock and lags are built into the model. 

**My Project Overview**
This project is a python module- based utility design including structure, core logic, code and tests to implement an mmm engineering solution for product teams. 

**MMM Quality Checks Utility**
Reusable python utility for validating MMM outputs against product defined thresholds.

**Features** 
Schema validation (defensive)
configurable threshold system (product aligned)
flag generation for unexpected output 
aggregate issue indicator 
pytest coverage for happy, edge and failure cases 
clear module seperation 
production safe error handling 
no hard coded values 
clean documentation 

**Setup Instructions**
Clone this repository.

**Install dependencies:**
pip install -e
pip install -r pyproject.toml

**Usage**
'''python 
import pandas as pd 
import pytest 
from quality import apply_quality_checks

df= pd.read_csv("MMM_dummy_outputs.csv") 
#first save the file on your chosen folder as a csv file or use assert function to ensure a csv file is used. provide complete filepath
result = apply_quality_checks.df
print(result.head())

**Running tests** 
pytest 

**Deploy**
yaml

**Pushing to GitHub**
1. Initialize Git
Navigate to the my_project directory and initialize Git:

'''cd test1
git init
'''

