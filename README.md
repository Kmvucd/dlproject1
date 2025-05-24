# dlproject1
This is the implementation of end to end deep learning project

## Workflows

- constants
- congif_entity
- components
- pipeline
- main

## How to setup

1. Creating virtual environment
conda create -n venv python=3.8 -y

2. Activate venv
conda activate venv

3. Run requirements file
pip install -r requirements.txt

4. Setup AWS CLI
Download it for windows and then install and usually it will be in ProgramFiles/Amazon. Need to create environment variables as user path.

5. In VS terminal, run aws --version, it will show version, else vs not recognizing CLI.

6. AWS Configuration
aws configure
Now, it will ask for access key and secret access key and region, download accesskeys from S3 bucket, and use them to configure my local to S3 bucket

7. Data Ingestion Flowchart
![alt text]({631906F3-B1BC-4845-9997-0E414DB08A9C}.png)

