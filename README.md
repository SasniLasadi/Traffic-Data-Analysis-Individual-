# Traffic-Data-Processing-and-Visualization-System
This project is a Python-based traffic data analysis tool that processes CSV data collected from two road junctions. It validates user input, performs statistical analysis, displays processed outcomes, saves results to a file and generates a histogram visualization of hourly vehicle counts using Tkinter. 

## 📌 Project Overview
This project processes daily traffic datasets collected from two major junctions:
- Elm Avenue / Rabbit Road
- Hanley Highway / Westway

It performs:  
- Input validation for date-based file selection
- Detailed analysis of vehicle movements, types, and traffic patterns
- Automated summary generation
- Saving results to a text file
- Graphical histogram visualization using Tkinter
- Support for multiple CSV file processing

## 🛠️ Features
- **Input Validation**
  - Ensures day, month, and year inputs are within allowed ranges
  - Identifies leap years
  - Builds a valid CSV filename (e.g., traffic_data28112024.csv)
- **Traffic Data Analysis**
  - Reads CSV traffic datasets
  - Calculates data such as
    - Total vehicle count
    - Average bicycles per hour
    - Vehicles over the speed limit
    - Rain duration (hours)
    - Peak traffic hour at Hanley/Westway
- **Saving Results**
  - Automatically writes all outcomes into results.txt
  - Appends new results without deleting old ones
- **Histogram Visualisation**
  - A Tkinter GUI displays a two-colour histogram comparing hourly traffic:
    - Elm Avenue/Rabbit Road (Green)
    - Hanley Highway/Westway (Yellow)
- **Multi-File Handling**
  - Lets users load multiple CSV files
  - Supports multiple histogram displays
  - Fully validated date inputs for repeated processing
    
## 📂 Project Structure
- main.py                     
- results.txt                 
- traffic_dataDDMMYYYY.csv    
- README.md

## 🛠️ Technologies Used
- Python
