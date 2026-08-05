from pathlib import Path

import pandas as pd

from constants import COUNTRY_MAPPING


# Reading the csv file
def job_reader() -> pd.DataFrame:
    file_path = Path(__file__).parent / "python_jobs.csv"
    df = pd.read_csv(file_path , index_col='job_link')
    return df.fillna("")


# Searching by keyword
def job_searcher(df : pd.DataFrame, keyword : str) -> pd.DataFrame:

    filt = (df["job_name"].str.contains(keyword , case=False , na=False) 
            | df["description"].str.contains(keyword , case=False , na=False) 
            | df["requirements"].str.contains(keyword, case=False , na=False))    

    return df[filt]


# Filtering by Location
def filter_by_location(df : pd.DataFrame , location : str) -> pd.DataFrame:
    location_filt = df["country"].str.contains(location , case=False , na=False) 

    return df[location_filt]


# Cleaning Country to extract the country from location (Hamburg, Germany) --> germany 
def clean_country(df : pd.DataFrame)-> None:
    df["country"] = (
        df["location"].str.split(',').fillna("").str[-1]
        .str.lower().str.strip()
        .replace(COUNTRY_MAPPING)
        
    )

# Showing some important stats
def show_statistics(df : pd.DataFrame ) -> dict:
    
    return {
        "total_jobs": len(df),
        "total_companies": df["company_name"].nunique() ,
        "top_locations": df["country"].value_counts().head(5) ,
        "top_categories" : df["category"].value_counts().head(5)
        }


# Sorting the jobs by specific column
def sort_jobs(df : pd.DataFrame , by : str ) -> pd.DataFrame:
    return df.sort_values(by=by)


# Saving the results to csv file
def save_to_csv(df: pd.DataFrame , filename : str ) -> None:

    if df.empty :
        print("No jobs found")
        return
    elif not filename.endswith(".csv"):
        filename += ".csv"
    file_path = Path(__file__).parent / filename
    df.to_csv(file_path, index=False)

    print(f"{filename} created successfully.") 

