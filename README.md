# Hotel Booking Data Analysis Platform

This project is a data analysis platform designed to interact with hotel booking data. It leverages machine learning and natural language processing to generate insights, SQL queries, and visualizations based on user input. The platform integrates with Streamlit for a user-friendly interface and FastAPI for API-based interactions.

---

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Setup Instructions](#setup-instructions)
4. [Environment Variables](#environment-variables)
5. [Usage](#usage)
6. [API Endpoints](#api-endpoints)
7. [Key Components](#key-components)
8. [Dependencies](#dependencies)

---

## Features

- **Natural Language Querying**: Ask questions about your data in plain English.
- **SQL Generation**: Automatically generates SQL queries based on user input.
- **Data Visualization**: Creates charts and visualizations using Plotly.
- **Streamlit Interface**: Interactive web-based interface for data exploration.
- **FastAPI Integration**: API endpoints for programmatic access to the platform.
- **Caching**: Optimized performance with caching for frequently used operations.

---

## Project Structure
. ├── .env # Environment variables 
    ├── analysis.py # Analytics-related logic 
    ├── api.py # FastAPI server implementation 
    ├── app.py # Streamlit application 
    ├── chroma.sqlite3 # Database file 
    ├── hotel_bookings.csv # Sample dataset 
    ├── requirements.txt # Python dependencies 
    ├── temp.py # Temporary scripts (if any) 
    ├── vanna_calls.py # Streamlit helper functions 
    ├── vanna_core.py # Core logic for Vanna AI 
    └── pycache/ # Compiled Python files

---

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>

2. **Install Dependencies:** Ensure you have Python 3.11 installed, then run:
    pip install -r requirements.txt

3. **Set Up Environment Variables:** Create a **.env** file in the root directory with the required variables (see Environment Variables).

4. **Run the Streamlit App:**
streamlit run app.py

5. **Run the FastAPI Server:**
uvicorn api:app --reload

## Environment Variables
The .env file should contain the following variables:
host="localhost"          # Database host
user="root"               # Database username
password="your_password"  # Database password
port=3306                 # Database port
API_KEY="your_api_key"    # API key for Google Gemini
dbname="hotel"            # Database name
model="gemini-2.0-flash"  # Model name for Google Gemini


## Usage
### Streamlit Interface
1. Launch the Streamlit app using the command:
streamlit run app.py

2. Use the interface to ask questions about your data, view SQL queries, and generate visualizations.

## FastAPI Endpoints
Start the FastAPI server:
uvicorn api:app --reload

**vanna_core.py**
Implements the MyVanna class, which integrates with ChromaDB and Google Gemini for data querying and analysis.

**vanna_calls.py**
Contains helper functions for Streamlit, such as generating SQL, running queries, and creating visualizations.

**api.py**
FastAPI implementation for exposing the platform's functionality via RESTful endpoints.

**app.py**
Streamlit application for interactive data exploration and visualization.

## Dependencies
The project requires the following Python libraries:

streamlit
fastapi
pydantic
pandas
plotly
python-dotenv
google-generativeai
chroma-db

Install all dependencies using:
pip install -r [requirements.txt]

## Notes
Ensure that the database (chroma.sqlite3) and sample dataset (hotel_bookings.csv) are properly configured before running the application.
The platform uses caching extensively to improve performance. If you encounter stale data, consider clearing the cache.

## License
This project is licensed under the MIT License. See the LICENSE file for details. 
