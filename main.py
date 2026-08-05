from constants import COUNTRY_MAPPING, VALID_FIELDS
from jobs import *


def menu() ->  str: 
    choose = input(
    """===== CSV Job Explorer =====

    1. Search Jobs
    2. Filter by Location
    3. Show Statistics
    4. Sort Jobs
    5. Export Results
    6. Reset 
    7. Exit

    Choose: """
    ).strip().lower()

    return choose


def main () -> None :
    jobs_df = job_reader()
    clean_country(jobs_df)
    result_jobs = jobs_df.copy()

    while True :
        choice  =  menu() # To Show the menu


        # Search Jobs
        if choice  in ["1" , "search jobs" , "search job"] :
            keyword = input("Enter the keyword that you will search by").strip()
            result_jobs  = job_searcher(result_jobs , keyword)
            print(f"Jobs searched successfully. , Found {len(result_jobs)}")


        # filter by location
        elif choice  in ["2" , "filter by location" , "filter location" , "location" , "filter"] :

            location = input("What country do you want to filter by").strip().lower()
            location = COUNTRY_MAPPING.get(location, location)
            result_jobs  = filter_by_location(result_jobs , location)
            print(f"Jobs filtered successfully. found {len(result_jobs)}")

        # Show Statistics
        elif choice  in ["3" , "statistics" , "show statistics"] :
            stats = show_statistics(result_jobs)
            print(f"""Total jobs : {stats["total_jobs"]}
            Total companies : {stats["total_companies"]}
            Top locations : """)
            print(stats["top_locations"])

        # Sort Jobs
        elif choice  in ["4" , "sort" , "sort jobs"] :

            by = input("""Sort by : 
            company_name,
            location,
             category,
            job_name""").strip().lower()
            if by not in VALID_FIELDS :
                print("Invalid Key")
                continue
            result_jobs  = sort_jobs(result_jobs , by)
            print(f"Jobs sorted successfully , found {len(result_jobs)}")

        # Export Jobs
        elif choice  in ["5" , "export" , "Export results"] :
            file_name = input("Type the file name").strip()
            save_to_csv(result_jobs , file_name)

        # Reset Jobs
        elif choice  in ["6" , "reset"] :
            result_jobs = jobs_df.copy()
            print("Results have been reset")

        # Exit
        elif choice  in ["7" , "exit"] :
            print("Good bye")
            break

        else :
            print("Invalid , please choose from the menu")
        
if __name__ == "__main__":
    main()