# Author: W.H.Sasni Lasadi
# Date: 28-11-2024
# Student ID: 20240745

# Task A: Input Validation
def task_A():
    def validate_date_input():
        # Loop until valid input is entered
        while True:
            try:
                # Prompt for the day and validate range
                DD = int(input("Enter a day: "))
                if DD < 1 or DD > 31:
                    print("Out of range - values must be in the range 1 and 31")
                    continue

                # Prompt for the month and validate range
                MM = int(input('Enter a month: '))
                if MM < 1 or MM > 12:
                    print("Out of range - values must be in the range 1 and 12")
                    continue
                
                # Prompt for the year and validate range
                YYYY = int(input('Enter a year: '))
                if YYYY < 2000 or YYYY > 2024:
                    print("Out of range - values must be in the range 2000 and 2024")
                    continue
                
                # Return validated date
                return DD, MM, YYYY
        
            except ValueError:
                print("Integer required")

    # Get returned values from the function
    DD, MM, YYYY = validate_date_input()

    # Check leap years
    def is_leap_year(YYYY):
        return(YYYY % 4 == 0)

    # Check the validation logic 
    if 1 <= DD <= 31 and 1 <= MM <= 12 and 2000 <= YYYY <= 2024:
        # Chech maximum days for each month
        if MM in [1,3,5,7,8,10,12]:    # Months with 31 days
            max_days = 31
        elif MM in [4,6,9,11]:    # Months with 30 days
            max_days = 30    
        elif MM == 2:    # February
            max_days = 29 if is_leap_year(YYYY) else 28
        else:
            max_days = 0    # Invalid month
            
        # Check if the day is valid:
        if 1 <= DD <= max_days:
            date = f"{DD}/{MM}/{YYYY}"
            print(f"Valid date entered, date is: {date}")
        else:
            print("Invalid data")
    else:
        pass
    file_name = f"traffic_data{DD:02d}{MM:02d}{YYYY}.csv"
    return file_name

def validate_continue_input():
    # Loop until valid input is entered
    while True:
        # Prompt for the user to decide quit or not
        user_input = input("Do you want to load another data set? Y or N: ")
        if user_input == "Y":
            print("Loading new dataset...")
            return "y"
        
        elif user_input == "N":
            print("End of run")
            return "n"
        else:
            print("Invalid input, please enter Y or N")


# Task B: Processed Outcomes
import csv
from collections import defaultdict
from datetime import datetime, timedelta

def process_csv_data(file_path):
    try:
        with open(file_path,"r") as file:
            data = csv.reader(file)
            # Skip the header row
            next(data)
            content = list(data)
            
            # Initialize counters
            total_vehicles = 0
            total_trucks = 0
            total_electric_vehicles = 0
            total_two_wheeled = 0
            total_busses_leaving_Elm_Avenue_Rabbit_Road_junction_heading_north = 0
            total_vehicles_passing_through_both_junctions_without_turning_left_or_right = 0
            percentage_of_all_vehicles_recorded_that_are_Trucks = 0
            average_of_Bicycles_per_hour = 0
            total_vehicles_recorded_over_the_speed_limit = 0
            total_vehicles_through_only_Elm_Avenue_Rabbit_Road_junction = 0
            total_vehicles_through_only_Hanley_Highway_Westway_junction = 0
            percentage_of_vehicles_through_Elm_Avenue_Rabbit_Road_Scooters = 0
            number_of_vehicles_in_the_peak_hour_on_Hanley_Highway_Westway = 0
            time_of_the_peak_traffic_hour_on_Hanley_Highway_Westway = 0
            rain_hours=[]
            totalRainTime=timedelta(0)
            total_hours_of_rain = 0
            peak_hour_vehicles = 0
            peak_times = 0
            hourly_vehicles = defaultdict(int)

            try:
                # Get the total number of vehicles
                total_vehicles = sum(1 for row in content)
                
                # Get the total number of trucks passing through all junctions
                total_trucks = sum(1 for row in content if row[8] == "Truck")
                
                # Get the total number of electric vehicles passing through all junctions
                total_electric_vehicles = sum(1 for row in content if row[9] == "True")
                    
                # Get the number of 'two wheeled' vehicles through all junctions
                total_two_wheeled = sum(1 for row in content if row[8] in ["Bicycle", "Motorcycle", "Scooter"])
                
                # Get the total number of busses leaving Elm Avenue/Rabbit Road junction heading north
                total_busses_leaving_Elm_Avenue_Rabbit_Road_junction_heading_north = sum(1 for row in content if row[8] == "Buss" and row[0] == "Elm Avenue/Rabbit Road" and row[4] == "N")
                
                # Get the total number of vehicles passing through both junctions without turning left or right
                total_vehicles_passing_through_both_junctions_without_turning_left_or_right = sum(1 for row in content if row[3] == row[4])
                
                # Get the percentage of all vehicles recorded that are Trucks
                percentage_of_all_vehicles_recorded_that_are_Trucks = f"{round((total_trucks/total_vehicles)*100)}%"
                
                # Get the average number Bicycles per hour
                total_bicycles = sum(1 for row in content if row[8] == "Bicycle")
                average_of_Bicycles_per_hour = int(total_bicycles/24)
                
                # Get the total number of vehicles recorded as over the speed limit 
                total_vehicles_recorded_over_the_speed_limit = sum(1 for row in content if int(row[6]) < int(row[7]))
                
                # Get the total number of vehicles recorded through only Elm Avenue/Rabbit Road junction
                total_vehicles_through_only_Elm_Avenue_Rabbit_Road_junction = sum(1 for row in content if row[0] == "Elm Avenue/Rabbit Road")
                
                # Get the total number of vehicles recorded through only Hanley Highway/Westway junction
                total_vehicles_through_only_Hanley_Highway_Westway_junction = sum(1 for row in content if row[0] == "Hanley Highway/Westway")
                
                # Get the percentage of vehicles through Elm Avenue/Rabbit Road that are Scooters
                scooters_through_Elm_Avenue_Rabbit_Road = sum(1 for row in content if row[8] == "Scooter" and row[0] == "Elm Avenue/Rabbit Road")
                percentage_of_vehicles_through_Elm_Avenue_Rabbit_Road_Scooters = f"{round((scooters_through_Elm_Avenue_Rabbit_Road/total_vehicles_through_only_Elm_Avenue_Rabbit_Road_junction)*100)}%"
                
                #Check if the weather condition
                for row in content:
                    if row[5] in ["Light Rain","Heavy Rain"]:
                        if previousWeatherStatus == "null":
                            rain_hours.append({"start":row[2],"end":row[2]})
                        else:
                            rain_hours[-1].update({"end":row[2]})
                        previousWeatherStatus = "heavy rain"
                    else:
                        previousWeatherStatus="null"

                #caculate rain hours
                for dict in rain_hours:
                    startTime = datetime.strptime(dict["start"], "%H:%M:%S")
                    endTime = datetime.strptime(dict["end"], "%H:%M:%S")

                    rainTime = endTime - startTime
                    totalRainTime += rainTime
                total_hours_of_rain = totalRainTime.seconds // 3600

                #add hourly vechicle count into dict
                for row in content:
                    if row[0] == "Hanley Highway/Westway":
                        hour = row[2].split(":")[0]
                        hourly_vehicles[hour] += 1

                #Peak hour calculations
                peak_hour_vehicles=max(hourly_vehicles.values())
                time_of_the_peak_traffic_hour_on_Hanley_Highway_Westway=[f"Between {hour}:00 and {int(hour)+1}:00"for hour,count in hourly_vehicles.items() if count==peak_hour_vehicles]
                
                    
                # Print the outcomes
                outcomes = [
                "***************************",
                f"Data file selected is {file_path}",
                "***************************",
                f"The total number of vehicles recorded for this date is {total_vehicles}",
                f"The total number of trucks recorded for this date is {total_trucks}",
                f"The total number of electric vehicles for this date is {total_electric_vehicles}",
                f"The total number of two-wheeled vehicles for this date is {total_two_wheeled}",
                f"The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {total_busses_leaving_Elm_Avenue_Rabbit_Road_junction_heading_north}",
                f"The total number of Vehicles through both junctions not turning left or right is {total_vehicles_passing_through_both_junctions_without_turning_left_or_right}",
                f"The percentage of total vehicles recorded that are trucks for this date is {percentage_of_all_vehicles_recorded_that_are_Trucks}",
                f"The average number of Bikes per hour is {average_of_Bicycles_per_hour}",
                f"The total number of Vehicles recorded as over the speed limit for this date is {total_vehicles_recorded_over_the_speed_limit}",
                f"The total number of vehicles recorded through Elm Avenue/Rabbit Road junction is {total_vehicles_through_only_Elm_Avenue_Rabbit_Road_junction}",
                f"The total number of vehicles recorded through Hanley Highway/Westway junction is {total_vehicles_through_only_Hanley_Highway_Westway_junction}",
                f"{percentage_of_vehicles_through_Elm_Avenue_Rabbit_Road_Scooters} of vehicles recorded through Elm Avenue/Rabbit Road are scooters",
                f"The highest number of vehicles in an hour on Hanley Highway/Westway is {peak_hour_vehicles}",
                f"The most vehicles through Hanley Highway/Westway were recorded between {time_of_the_peak_traffic_hour_on_Hanley_Highway_Westway}",
                f"The number of hours of rain for this date is {total_hours_of_rain}",
                    ]
                
                # Return outcomes
                return outcomes

            except (ValueError, IndexError) as e:
                print(f"Skipping invalid row Error: {e}")
   
    except FileNotFoundError:
        print("File does not exist.")
       
def display_outcomes(outcomes):
    for i in range(len(outcomes)):
        print(outcomes[i])
        

# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    try:
        with open(file_name, "a") as file:
            for outcome in outcomes:
                file.write(outcome + "\n")
            file.write("\n")
        print(f"Results successfully saved to {file_name}")
        
    except IOError as e:
        print(f"Error writing to file {file_name}: {e}")
          
while True:
    file_path = task_A()
    outcomes=process_csv_data(file_path)
    if outcomes:
        display_outcomes(outcomes)
        save_results_to_file(outcomes)
    
    # Get returned values from the function
    status=validate_continue_input()
    if status == "n":
        break
 
# Task D: Histogram Display
import tkinter as tk
from collections import defaultdict

class HistogramApp:
    def __init__(self, traffic_data, date):
        self.traffic_data = traffic_data
        self.date = date
        self.root = tk.Tk()
        self.root.title(f"Traffic Data Histogram - {self.date}")
        self.canvas = tk.Canvas(self.root, width=1300, height=600, bg="white")
        self.canvas.pack()

    def draw_histogram(self):
        hourly_data = defaultdict(lambda: [0, 0])  # [Elm Ave Count, Hanley Hwy Count]

        for row in self.traffic_data:
            junction, time_of_day = row[0], row[2]
            hour = int(time_of_day.split(":")[0])
            if junction == "Elm Avenue/Rabbit Road":
                hourly_data[hour][0] += 1
            elif junction == "Hanley Highway/Westway":
                hourly_data[hour][1] += 1

        bar_width = 20
        max_count = max(
            max(counts[0], counts[1]) for counts in hourly_data.values()
        )
        scale_factor = 400 / max_count if max_count > 0 else 1

        # Draw the x-axis and y-axis
        self.canvas.create_line(40, 450, 1300, 450, width=2)  # x-axis
        self.canvas.create_line(40, 450, 40, 50, width=2)     # y-axis
        '''
        # Add labels to the y-axis (vehicle counts)
        for i in range(0, max_count + 1, max(1, max_count // 10)):
            y_position = 450 - i * scale_factor
            self.canvas.create_line(35, y_position, 45, y_position, width=1)
            self.canvas.create_text(25, y_position, text=str(i), anchor="e", font=("Arial", 10))
        '''
        # Draw bars and labels for each hour
        for hour in range(24):
            counts = hourly_data[hour]
            x_start = 50 + hour * (2 * bar_width + 10)
            x_mid = x_start + bar_width
            x_end = x_mid + bar_width

            # Draw bars for Elm Avenue/Rabbit Road
            self.canvas.create_rectangle(
                x_start, 450 - counts[0] * scale_factor, x_mid, 450, fill="#AFE1AF"
            )
            self.canvas.create_text(
                (x_start + x_mid) / 2, 450 - counts[0] * scale_factor - 10,
                text=str(counts[0]), fill="#000000", font=("Arial", 8)
            )

            # Draw bars for Hanley Highway/Westway
            self.canvas.create_rectangle(
                x_mid, 450 - counts[1] * scale_factor, x_end, 450, fill="#FFFFC5"
            )
            self.canvas.create_text(
                (x_mid + x_end) / 2, 450 - counts[1] * scale_factor - 10,
                text=str(counts[1]), fill="#000000", font=("Arial", 8)
            )

            # Draw hour labels on the x-axis
            self.canvas.create_text(
                (x_start + x_end) / 2, 460, text=f"{hour}:00", anchor="n", font=("Arial", 8)
            )

        # Add axis labels and histogram title
        self.canvas.create_text(
            400, 15, text=f"Histogram of Vehical Frequency per Hour ({self.date})", font=("Arial", 15, "bold"), anchor="w"
        )
        self.canvas.create_text(
            700, 500, text="Time (hours)", font=("Arial", 12), anchor="w"
        )
        self.canvas.create_text(
            20, 250, text="Vehicle Count", font=("Arial", 12), anchor="center", angle=90
        )
        self.canvas.create_rectangle(
            50, 45, 75, 70, fill="#AFE1AF", outline="#000000", width=2
        )
        self.canvas.create_text(
            80, 57.5, text="Elm Avenue/Rabbit Road", font=("Arial", 10), fill="#000000", anchor="w"
        )
        self.canvas.create_rectangle(
            50, 75, 75, 100, fill="#FFFFC5", outline="#000000", width=2
        )
        self.canvas.create_text(
            80, 87.5, text="Hanley Highway/Westway", font=("Arial", 10), fill="#000000", anchor="w"
        )

    def run(self):
        self.draw_histogram()
        self.root.mainloop()

# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        self.current_data = None

    def load_csv_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()[1:]  # Skip header
                self.current_data = [line.strip().split(",") for line in lines]
            return True
        except FileNotFoundError:
            print("Error: File not found.")
            return False

    def process_data_and_display_histogram(self, date):
        if self.current_data:
            app = HistogramApp(self.current_data, date)
            app.run()

    def handle_user_interaction(self):
        while True:
            # Step 1: Ask if the user wants to load another histogram
            user_choice = input("Do you want to load the histogram? (Y/N): ").strip().upper()
        
            if user_choice == "Y":
                # Step 2: Collect the date, month, and year as separate inputs
                while True:
                    try:
                        DD = int(input("Enter the day (DD): "))
                        if DD < 1 or DD > 31:
                            print("Out of range - values must be in the range 1 and 31")
                            continue

                        MM = int(input("Enter the month (MM): "))
                        if MM < 1 or MM > 12:
                            print("Out of range - values must be in the range 1 and 12")
                            continue

                        YYYY = int(input("Enter the year (YYYY): "))
                        if YYYY < 2000 or YYYY > 2024:
                            print("Out of range - values must be in the range 2000 and 2024")
                            continue

                        # Combine inputs into the desired filename format
                        file_path = f"traffic_data{DD:02d}{MM:02d}{YYYY}.csv"
                        
                        # Check leap years
                        def is_leap_year(YYYY):
                            return(YYYY % 4 == 0)

                        # Check the validation logic 
                        if 1 <= DD <= 31 and 1 <= MM <= 12 and 2000 <= YYYY <= 2024:
                            # Chech maximum days for each month
                            if MM in [1,3,5,7,8,10,12]:    # Months with 31 days
                                max_days = 31
                            elif MM in [4,6,9,11]:    # Months with 30 days
                                max_days = 30    
                            elif MM == 2:    # February
                                max_days = 29 if is_leap_year(YYYY) else 28
                            else:
                                max_days = 0    # Invalid month
                                
                            # Check if the day is valid:
                            if 1 <= DD <= max_days:
                                date = f"{DD}/{MM}/{YYYY}"
                            
                            else:
                                print("Invalid data check day, month and year")
                        else:
                            pass
                    
                        if self.load_csv_file(file_path):
                            self.process_data_and_display_histogram(f"{DD:02d}/{MM:02d}/{YYYY}")
                            break
                        
                        else:
                            print("File not found or failed to process. Please try again.")

                    except ValueError:
                        print("Integer required")
                        
            # Exit from the programme           
            elif user_choice == "N":
                        print("Exiting program.")
                        break
                    
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

if __name__ == "__main__":
    processor = MultiCSVProcessor()
    processor.handle_user_interaction()
    
    
