import os 
import sys
from src.exception import CustomException 
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    
        raw_data_path: str = os.path.join("artifacts", "data.csv")
        train_data_path: str = os.path.join("artifacts", "train.csv")
        test_data_path: str = os.path.join("artifacts", "test.csv")
        
class DataIngestion:
        def __init__(self):
                self.ingestion_config = DataIngestionConfig()
        
        def initiatite_data_ingestion(self):
                logging.info("Entered the data Ingestion method")

                try:
                        df=pd.read_csv('notebook\data\stud.csv')
                        logging.info("Dataset loaded successfully")
                        
                        os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

                        #save raw data
                        df.to_csv(self.ingestion_config.raw_data_path, index = False, header=True)

                        #split data
                        train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

                        #save test and train data

                        train_set.to_csv(self.ingestion_config.train_data_path, index= False, header= True)

                        test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

                        logging.info("data ingestion completed")

                        return(
                                self.ingestion_config.train_data_path,
                                self.ingestion_config.test_data_path
                        )
                        
                except Exception as e:
                        logging.error(f"error during data ingestion:{e}")

                        raise e
                
if __name__=="__main__":
        obj = DataIngestion()
        train_path, test_path = obj.initiatite_data_ingestion()
        print("Train path", train_path)
        print("Test path", test_path)
    

                    