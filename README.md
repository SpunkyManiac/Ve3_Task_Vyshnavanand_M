# Data Analysis Web Application

## Overview

This project is a Django-based web application that allows users to upload CSV files and perform basic data analysis. The application processes the uploaded data, handles missing values based on user preferences, and provides various statistical summaries and visualizations.

## Features

- File Upload: Users can upload CSV files for analysis.
- Missing Value Handling: Users can choose how to handle missing values:
  - Remove rows with missing values
  - Fill missing values with the mean
  - Fill missing values with the median
- Data Processing:
  - Display the first few rows of the data
  - Provide summary statistics
  - Show the count of missing values per column
  - Generate histograms for numerical columns

## Software Configuration

-Requirements
    -Python 3.6+
    -Django 3.2+
    -pandas 1.2+
    -numpy 1.20+
    -matplotlib 3.4+
    -seaborn 0.11+


## Setup

1. Clone the Repository:
   
   git clone <repository-url>
   cd <repository-directory>
   

2. Install Dependencies:
   Make sure you have Python and pip installed. Then, install the required packages:
   
   pip install -r requirements.txt
   

3. Run Migrations:
   Apply the database migrations:
   
   python manage.py migrate
   

4. Run the Server:
   Start the Django development server:
   
   python manage.py runserver
   

5. Access the Application:
   Open your web browser and navigate to `http://127.0.0.1:8000/` to use the application.

## Usage

1. Upload CSV:
   - Go to the upload page.
   - Choose a CSV file from your computer.
   - Select a strategy for handling missing values.
   - Click the "Upload" button.

2. View Results:
   - After uploading the file, the application will display the first few rows of the data, summary statistics, missing values, and histograms for numerical columns.

## Project Structure

- `data_analysis/`: Main application directory.
  - `templates/`: HTML templates.
  - `forms.py`: Form definitions.
  - `views.py`: View functions.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.


This README provides an overview of the project, setup instructions, usage guidelines, and contribution information. Feel free to customize it further based on your project's specific needs.