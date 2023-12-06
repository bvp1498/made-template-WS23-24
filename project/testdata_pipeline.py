import pandas as pd
import pytest
from sqlalchemy import create_engine, inspect
import data_collector as dc


@pytest.mark.dependency()
def test_get_datasets():
    ds1 = dc.get_and_preprocess_breast_cancer_wisconsin_dataframe()
    assert isinstance(ds1, pd.DataFrame)

    ds2 = dc.get_and_preprocess_cancer_dataset_from_major_indian_cities_dataframe()
    assert isinstance(ds2, pd.DataFrame)


@pytest.mark.dependency()
def test_data_collector_pipeline():
    data_dict = dc.DATASET_DICT
    dc.data_collector()

    co_db_engine = create_engine(f"sqlite:///data/{data_dict['Breast_Cancer_Wisconsin_DataSet']['database_name']}.sqlite")
    inspector = inspect(co_db_engine)
    tables = inspector.get_table_names()

    assert len(tables) == 1
    assert data_dict['Breast_Cancer_Wisconsin_DataSet']['database_name'] in tables

    gp_db_engine = create_engine(f"sqlite:///data/{data_dict['Cancer_Dataset_From_Major_Indian_Cities']['database_name']}.sqlite")
    inspector = inspect(gp_db_engine)
    tables = inspector.get_table_names()

    assert len(tables) == 1
    assert data_dict['Cancer_Dataset_From_Major_Indian_Cities']['database_name'] in tables
