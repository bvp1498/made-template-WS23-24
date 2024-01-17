# Analysis Report: Cancer Incidence Analysis between Brazil and Indian Cities

## Overview

This project offers a thorough examination of the variations in cancer occurrence rates among several cities in Brazil and India. The aim is to discern trends, patterns, and possible elements that influence the disparities seen in cancer rates across genders in these areas.

## Technologies Used
- **Python**: The project employs the Python programming language for data analysis and the creation of visualizations.
- **Pandas**: This library is utilized for the manipulation and analysis of data.
- **Matplotlib and Seaborn**: These tools are applied to generate visualizations that help in comprehending the data trends.
- **sqlalchemy**:  This is a Python SQL toolkit and Object-Relational Mapping (ORM) library, offering a comprehensive range of enterprise-level persistence patterns.
- **subprocess**: This module is used for initiating new processes, managing their input/output/error streams, and retrieving their exit statuses.
- **Kaggle API**: Employed to retrieve the dataset for analysis.

## Kaggle Authentication
To access the dataset from Kaggle, follow these steps:

1. Go to [Kaggle Account Settings](https://www.kaggle.com/settings).
2. Download your Kaggle API key as a `kaggle.json` file.
3. Place the `kaggle.json` file inside the `/project/` directory.

**Filepath:** `/project/kaggle.json`

```json
{
  "username": "bh******8",
  "key": "40a*******************50a"
}
```

## Set Execute Permissions for the Pipeline Script
Before running the analysis pipeline, ensure that the pipeline script has execute permissions. Run the following command:

```bash
chmod +x ./project/pipeline.sh
```

## Run the Analysis Pipeline
Navigate to the project directory and execute the pipeline script:

```bash
cd project && ./pipeline.sh
```

## Set Execute Permissions for the Test Pipeline Script
If you want to run the test pipeline, grant execute permissions to the test script:

```bash
chmod +x ./project/test.sh
```

## Run the Test Pipeline
Navigate to the project directory and execute the test script:

```bash
cd project && ./test.sh
```

## Analysis Report
Explore the detailed analysis report [here](https://github.com/bvp1498/made-template-WS23-24/blob/main/project/report.ipynb).

The objective of this report is to examine data on cancer occurrences in Brazil and several cities in India, investigating patterns, spread, and possible connections across genders in both areas.
