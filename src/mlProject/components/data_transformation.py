import os
import pandas as pd
from src.mlProject import logger
from sklearn.model_selection import train_test_split
from src.mlProject.entity.config_entity import DataTransformationConfig
from sklearn.preprocessing import LabelEncoder, StandardScaler


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        
        data = pd.read_csv(self.config.data_path)
        logger.info("Data loaded successfully.")

        # Separate numerical and categorical features
        num_cols = data.select_dtypes(include=['int64', 'float64']).columns
        cat_cols = data.select_dtypes(include=['object']).columns

        # Label encode categorical features
        label_encoders = {}
        for col in cat_cols:
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col].astype(str))
            label_encoders[col] = le
            logger.info(f"Encoded column: {col}")

        # Standard scaling of numerical features
        scaler = StandardScaler()
        data[num_cols] = scaler.fit_transform(data[num_cols])
        logger.info("Numerical features scaled.")

        # Split the data
        train, test = train_test_split(data, test_size=0.2, random_state=42)

        # Save train and test sets
        os.makedirs(self.config.root_dir, exist_ok=True)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info("Data split into train and test sets.")
        logger.info(f"Train shape: {train.shape}")
        logger.info(f"Test shape: {test.shape}")

        print("Train shape:", train.shape)
        print("Test shape:", test.shape)

    


