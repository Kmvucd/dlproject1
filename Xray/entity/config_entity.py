import os
import sys
from dataclasses import dataclass
from torch import device
from Xray.constant.training_pipeline import *


@dataclass

class DataIngestionConfig:
    def __init__(self):
        self.S3_data_folder: str = S3_DATA_FOLDER
        self.bucket_name: str = BUCKET_NAME
        self.artifact: str = os.path.join(ARTIFACT_DIR, TIMESTAMP)
        self.data_path: str=os.path.join(
            self.artifact, "data_ingestion", 
            self.S3_data_folder)
        self.train_data_path: str = os.path.join(self.data_path, "train")
        self.test_data_path: str = os.path.join(self.data_path, "test")
