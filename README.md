# 🏢 Census Data Standardization and Analysis Pipeline

Welcome to the Census Data Standardization and Analysis Pipeline project! This project aims to clean, standardize, process, and analyze census data to ensure uniformity, accuracy, and accessibility. The ultimate goal is to provide insightful visualizations that can aid in understanding the census data more effectively.

## 🚀 Project Overview
![Capstone Project-1](https://github.com/user-attachments/assets/592fe444-8493-464d-bd4c-7102627b422c)


The Census Data Standardization and Analysis Pipeline involves several key steps:
1. **Data Cleaning**: Renaming columns for consistency.
2. **Data Standardization**: Standardizing state/UT names and handling new state formations.
3. **Missing Data Processing**: Identifying and filling missing data.
4. **Data Storage**: Saving the cleaned data to MongoDB and uploading it to an SQL database.
5. **Data Analysis**: Running SQL queries to derive meaningful insights.
6. **Visualization**: Using Streamlit to create interactive and informative visualizations.

## 🛠️ Technologies Used
![Capstone Project-1 (2)](https://github.com/user-attachments/assets/152faed9-1b5d-461d-abbe-16db85ad06f1)

- **Python**: The primary programming language for data processing and analysis.
- **SQL**: For relational database operations.
- **MongoDB**: To store the cleaned data in a NoSQL database.
- **Streamlit**: To create interactive visualizations.
- **Pandas**: For data manipulation and analysis.

## 📁 Project Structure

![Capstone Project-1 (3)](https://github.com/user-attachments/assets/aadcbbce-fa4f-47de-8eba-e26cc1f1e0b9)


## 📜 Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- MongoDB
- MySQL
- Streamlit

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/soumyasankar99/census_data_pipeline.git
   cd census_data_pipeline

2.**Install the required Python packages**:
pip install -r requirements.txt

3.**Run the main script**:
python main.py

## 📊 Features

### Data Cleaning
- Column Renaming: Standardizes the column names for consistency across datasets.
### Data Standardization
- State/UT Name Standardization: Formats state and UT names to have consistent capitalization.
- New State/UT Formation: Handles new state formations (e.g., Telangana and Ladakh).
- Missing Data Processing
- Filling Missing Data: Uses logical deductions to fill in missing data.
- Missing Data Report: Generates a report on the percentage of missing data before and after   processing.

#### Data Storage
- MongoDB Integration: Saves the cleaned data to a MongoDB collection.
- SQL Database Upload: Uploads the data to an SQL database with appropriate table structures.

### Data Analysis
- SQL Queries: Runs a set of predefined queries to analyze the data.
- Streamlit Visualization: Displays the query results using interactive Streamlit dashboards.

## 🔍 Example Queries

- Total population of each district
- Number of literate males and females in each district
Percentage of workers in each district
Households with access to various amenities



## 🧪 Testing

### To run the tests:
python -m unittest discover -s tests

## 🎨 Visualization

### Streamlit is used for visualizing the results of the analysis. Run the following command to start the Streamlit app:

streamlit run scripts/visualization.py

## 👥 Contributing
We welcome contributions! Please read our Contributing Guidelines for more details.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for more information.

## 📧 Contact
Have questions or suggestions? Feel free to reach out at soumyasankar99@gmail.com.



⭐️ If you like this project, please give it a star! ⭐️

