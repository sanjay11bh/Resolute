import os
from src.mlProject import logger
from src.mlProject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self , config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self)-> bool:
        """
        Validate all columns in the dataset against the schema
        """
        try:
            validation_status = None
            # Read the data            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)
            # Check if all columns are present in the data

            all_schema= self.config.all_schema.keys()
            
            for col in all_cols:
                if col not in all_schema :
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status : {validation_status}\n")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status : {validation_status}\n")
                
                return validation_status
        except Exception as e:
            raise e
