
import pandas as pd
import os
from glob import glob

# Define the paths for the datasets
dataset1_path = 'dataset1/'  # Path for the Indian Cities Cancer Dataset
dataset2_path = 'dataset2/data.csv'  # Path for the Breast Cancer Prediction Dataset


DATASET_DICT = {
 "Breast_Cancer_Wisconsin_DataSet":= [
    "Chennai_2012_2016 - Sheet1.csv",
    "Delhi_2012_2014 - Sheet1.csv",
    "Hyderabad_District_2014_2016 - Sheet1.csv",
    "Kolkata_2012_2015 - Sheet1.csv",
    "Kollam_2012_2016 - Sheet1.csv",
    "Mumbai_2012_2015 - Sheet1.csv",
    "Patiala_District_2012_2016 - Sheet1.csv",
    "Thiruvanathapuram_2012_2016 - Sheet1.csv"
]

"Cancer_Dataset_From_Major_Indian_Cities": = "data.csv"
}

def authenticate_kaggle():
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()

    return kaggle_api

def download_dataset(kaggle_api):
    """
    Download a datasets in current directory and unzip it
    :param kaggle_api:
    :return:
    """
    for key, val in DATASET_DICT.items():
        kaggle_api.dataset_download_files(val['dataset_path'], path='./', unzip=True)

    return

def get_and_preprocess_breast_cancer_wisconsin_dataframe():
   
    # create crude oil dataframe from csv
    breast_cancer_wisconsin_dataset_df = pd.read_csv(DATASET_DICT["Breast_Cancer_Wisconsin_DataSet"]["file_name"])

    # preprocess the crude-oil dataset
    breast_cancer_wisconsin_dataset_df['date'] = pd.to_datetime(breast_cancer_wisconsin_dataset_df['date']).dt.date

    return breast_cancer_wisconsin_dataset_df

def get_and_preprocess_cancer_dataset_from_major_indian_cities_dataframe():

    # create crude oil dataframe from csv
    cancer_dataset_from_major_indian_cities_df = pd.read_csv(DATASET_DICT["Cancer_Dataset_From_Major_Indian_Cities"]["file_name"])

    # preprocess the crude-oil dataset
    cancer_dataset_from_major_indian_cities_df['Date'] = pd.to_datetime(cancer_dataset_from_major_indian_cities_df['Date'], format='%d-%m-%Y')

    return cancer_dataset_from_major_indian_cities_df

def dump_dataset_to_db(dataframe, db_name, datatype):

    db_engine = create_engine(f"sqlite:///data/{db_name}.sqlite")
    dataframe.to_sql(db_name, db_engine, index=False, if_exists='replace', dtype=datatype)
    return


def main():
   
    kaggle_api = authenticate_kaggle()

    # download dataset in local storage
    download_dataset(kaggle_api)

    
    breast_cancer_wisconsin_dataset_df = get_and_preprocess_breast_cancer_wisconsin_dataframe()

    
    cancer_dataset_from_major_indian_cities_df = get_and_preprocess_cancer_dataset_from_major_indian_cities_dataframe()

    # insert crude oil data into sqlite database
    dump_dataset_to_db(dataframe=breast_cancer_wisconsin_dataset_df, db_name=DATASET_DICT['Breast_Cancer_Wisconsin_DataSet']['database_name'],
                       datatype=DATASET_DICT['Breast_Cancer_Wisconsin_DataSet']['sqlalchemy_datatype'])

    # insert gold price data into sqlite database
    dump_dataset_to_db(dataframe=cancer_dataset_from_major_indian_cities_df, db_name=DATASET_DICT['Cancer_Dataset_From_Major_Indian_Cities']['database_name'],
                       datatype=DATASET_DICT['Cancer_Dataset_From_Major_Indian_Cities']['sqlalchemy_datatype'])


if __name__ == "__main__":
    main()
