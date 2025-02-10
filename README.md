# Interactive Application with Streamlit

## Description
This web application built with Streamlit allows users to upload CSV files, visualize data in tabular format, and create interactive charts using Plotly.

## Features
- **Simple Navigation:** Sidebar menu to navigate between the main page, data visualization section, and interactive charts.
- **Data Visualization:** Load and display the contents of CSV files along with descriptive statistics.
- **Interactive Charts:** Select data columns to generate interactive bar charts.

## Requirements

Before running the application, make sure you have the following dependencies installed:

- Python 3.7 or higher
- Streamlit
- Pandas
- Plotly

To install them, run:

```bash
pip install streamlit pandas plotly
```

## Running the Application
To start the application, run the following command in your terminal:

```bash
streamlit run your_file_name.py
```

Ensure that you are in the directory containing the application file.

## Live Application
You can access the live version of the application here:

[VisuApp - Interactive Data Visualization](https://visuapp-6oqdnysxugorteftsxmkty.streamlit.app/)

## Usage

### 1. Navigation
Use the sidebar to switch between the following sections:

- **Main Page:** Displays an introduction to the application.
- **Data Visualization:** Allows uploading a CSV file to display its contents and statistics.
- **Interactive Charts:** Enables selecting columns from the CSV file to create bar charts.

### 2. Data Visualization
- Click on "Choose a CSV file" and select a file to upload.
- The application will display the file's contents and descriptive statistics.

### 3. Interactive Charts
- Upload a CSV file.
- Select columns for the X and Y axes.
- Click "Create Chart" to generate an interactive bar chart.

## Project Structure

```
|-- .idea
|-- your_file_name.py
|-- README.md
```

## Contribution
If you want to contribute to this project, follow these steps:
1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a Pull Request.

## License
This project is licensed under the MIT License.




