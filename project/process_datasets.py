
import pandas as pd
import os
from glob import glob

# Define the paths for the datasets
dataset1_path = 'dataset1/'  # Path for the Indian Cities Cancer Dataset
dataset2_path = 'dataset2/data.csv'  # Path for the Breast Cancer Prediction Dataset

# Function to read and combine Indian Cities Cancer Dataset
def read_and_combine_dataset1(path):
    all_files = glob(os.path.join(path, "*.csv"))
    df_list = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        df['City'] = os.path.basename(filename).split('_')[0]  # Extract city name from filename
        df_list.append(df)
    combined_df = pd.concat(df_list, axis=0, ignore_index=True)
    return combined_df

# Function to read Breast Cancer Prediction Dataset
def read_dataset2(path):
    return pd.read_csv(path)

# Function to clean and transform datasets
def clean_transform_datasets(df1, df2):
    # Basic cleaning and transformation can be added here
    # For example, handling missing values, renaming columns, etc.
    
    return df1, df2

# Main execution
def main():
    # Read and combine the datasets
    dataset1 = read_and_combine_dataset1(dataset1_path)
    dataset2 = read_dataset2(dataset2_path)

    # Clean and transform the datasets
    dataset1_clean, dataset2_clean = clean_transform_datasets(dataset1, dataset2)

    # Save the cleaned datasets
    dataset1_clean.to_csv('/data/combined_indian_cities_cancer_dataset.csv', index=False)
    dataset2_clean.to_csv('/data/breast_cancer_prediction_dataset.csv', index=False)


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
