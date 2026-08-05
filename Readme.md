# CSV Job Explorer 📊

A simple command-line application built with Python to explore job listings stored in a CSV file. The project allows users to search, filter, sort, analyze, and export job data through an interactive menu.

## Features
* Search jobs by any keyword.
* Filter jobs by location.
* Display useful statistics:

  * Total number of jobs.
  * Total number of companies.
  * Top 5 locations.
* Sort jobs by:

  * Company name
  * Job title
  * Category
  * Location
* Clean and normalize location data before filtering.
* Export the current results to a new CSV file.
* Reset the current results back to the original dataset.

## Technologies Used

* Python 3
* pathlib
* Pandas

## Project Structure

```text
.
├── main.py # CLI interface
├── jobs.py # Data processing functions
├── constants.py # Constants and mappings
├── python_jobs.csv
├── requirements.txt
└── README.md
```

## Example Menu

```text
===== CSV Job Explorer =====

1. Search Jobs
2. Filter by Location
3. Show Statistics
4. Sort Jobs
5. Export Results
6. Reset
7. Exit
```

## What I Learned

This project helped me practice:

* Reading and writing CSV files.
* Organizing code into reusable functions.
* Searching and filtering data.
* Organizing data with pandas
* Cleaning and normalizing data.
* Building an interactive command-line application.
* Separating project logic into multiple modules.
* Working with Pandas DataFrames.

## Future Improvements

* Support searching within specific fields.
* Improve statistics and reporting.
* Add colored terminal output.
* Add unit tests.
* Export results to Excel.
* Support ascending/descending sorting.

## Installation

```bash
git clone https://github.com/vjoe1/csv-job-explorer

cd CSV-Job-Explorer

pip install -r requirements.txt

python main.py
```

## License

This project is for learning and educational purposes.
