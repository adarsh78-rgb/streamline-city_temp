# Simply DATA Web App

## Overview
Simply DATA is a web application built using Streamlit that allows users to upload CSV files, preview the data, filter it based on selected columns and values, and visualize the data through line charts. This app is designed to provide a simple and intuitive interface for data exploration and visualization.

## Features
- **CSV File Upload**: Users can upload CSV files for analysis.
- **Data Preview**: Displays the first six rows of the uploaded dataset.
- **Data Summary**: Provides a statistical summary of the dataset.
- **Data Filtering**: Users can filter the dataset based on selected columns and unique values.
- **Data Visualization**: Users can create line charts by selecting x-axis and y-axis columns.

## Requirements
To run this application, you need to have the following Python packages installed:
- Streamlit
- Pandas
- Matplotlib

You can install the required packages using pip:
```bash
pip install streamlit pandas matplotlib
```

## How to Run the App
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/simply-data.git
   cd simply-data
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```
3. Open your web browser and go to `http://localhost:8501` to access the app.

## Usage
- Click on the "Choose csv file" button to upload your CSV file.
- After uploading, you can preview the data and view its summary.
- Use the filter options to narrow down the data based on specific criteria.
- Select the columns for the x-axis and y-axis to plot the data.
- Click the "Plot" button to generate the line chart.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.


## Acknowledgments
- Thanks to the Streamlit community for providing an excellent framework for building web applications.
- Thanks to the contributors and users who help improve this project.
