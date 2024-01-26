import sys # Import the sys module for command-line argument handling

def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file:
            cat_entries = 0
            other_cats_doused = 0
            total_time_in_house = 0
            visit_length = []


            for line in file:  # Loop through each line in the log file
                if line.strip() == 'END':  # Stop processing if 'END' is encountered
                    break

                cat_name, entry_time, exit_time = line.strip().split(',')  # Split the line into cat name, entry, and exit times

                duration = int(exit_time) - int(entry_time)

                # Track visits and duration for 'OURS' cat

                if cat_name == 'OURS':
                    cat_entries += 1  # Increment the counter for 'OURS' cat visits
                    total_time_in_house += duration
                    visit_length.append(duration)
                else:
                    other_cats_doused += 1  # Increment the counter for visits by other cats

            # Calculate average visit duration

            avg_duration = total_time_in_house / cat_entries if cat_entries > 0 else 0

             # Print the results of the log file analysis

            print("\nLog File Analysis")
            print("==================")
            print(f"Cat Visits: {cat_entries}")
            print(f"Other Cats: {other_cats_doused}")
            print(f"\nTotal Time in House: {format_duration(total_time_in_house)}")
            print(f"\nAverage Visit Length: {format_duration(avg_duration)}")
            print(f"Longest Visit: {format_duration(max(visit_length))}")
            print(f"Shortest Visit: {format_duration(min(visit_length))}")

    except FileNotFoundError:  # Handle the case where the log file is not found
        print(f'Cannot open "{file_path}"!')
    except Exception as e:  # Handle other exceptions that might occur
        print(f'An error occurred: {e}')

def format_duration(minutes):
    hours, minutes = divmod(minutes, 60)  # Convert total minutes into hours and remaining minutes
    if hours > 0:
        return f"{int(hours)} Hours, {int(minutes)} Minutes"
    else:
        return f"{int(minutes)} Minutes"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        log_file_path = sys.argv[1]  # Retrieve the log file path from the command line argument
        analyze_cat_shelter_log(log_file_path)  # Call the analyze_cat_shelter_log function with the file path
