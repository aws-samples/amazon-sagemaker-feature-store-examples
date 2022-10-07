import subprocess
import sys
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'sagemaker'])

from sagemaker.feature_store.feature_group import FeatureGroup
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from datetime import datetime, timezone, date
import pandas as pd
import sagemaker
import argparse
import logging
import boto3
import time
import os

logger = logging.getLogger('__name__')
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


label_encoder = LabelEncoder()
min_max_scaler = MinMaxScaler()

import pandas as pd
import numpy as np

def choose_persona(row):
    if row['Id'] > 3:
        return 0
    else:
        return 1

def apply_transforms(df: pd.DataFrame) -> pd.DataFrame:
    df['Persona'] = df.apply(lambda row : choose_persona(row), axis=1) 
    df['NewFeature1'] = df['Persona'] * np.random.rand() + (2* df['ZipCode'])
    return df

def get_file_paths(directory):
    file_paths = [] 
    for root, directories, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith('.csv'):
                file_path = os.path.join(root, file_name)
                file_paths.append(file_path)  
    return file_paths

def ingest_data(args: argparse.Namespace) -> None:
    boto_session = boto3.session.Session(region_name=args.region_name)
    sagemaker_session = sagemaker.Session(boto_session=boto_session)

    files = get_file_paths('/opt/ml/processing/input/')
    logger.info(f'Files: {files}')
    if len(files) > 0:
        df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)
        df = apply_transforms(df)
        logger.info(f'Ingesting a total of [{df.shape[0]}] rows from {len(files)} files')
        logger.info(f'first few rows:\n{df.head()}')
        logger.info(f'Ingesting into feature group [{args.feature_group_name}] using {args.num_processes} processes and {args.num_workers} workers')
        fg = FeatureGroup(name=args.feature_group_name, sagemaker_session=sagemaker_session)
        fg.ingest(data_frame=df, max_processes=args.num_processes, max_workers=args.num_workers, wait=True)
        logger.info('fg.ingest() finished')
    else:
        logger.info(f'No files to ingest. Exiting successfully.')
    return
    
def parse_args() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_processes', type=int, default=1)
    parser.add_argument('--num_workers', type=int, default=1)
    parser.add_argument('--feature_group_name', type=str)
    parser.add_argument('--region_name', type=str)
    args, _ = parser.parse_known_args()
    return args


if __name__ == '__main__':
    logger.info('BATCH INGESTION - STARTED')
    args = parse_args()
    ingest_data(args)
    logger.info('BATCH INGESTION - COMPLETED')
