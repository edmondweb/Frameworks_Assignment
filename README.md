CORD-19 Data Explorer
=====================

This is a simple Streamlit app that allows users to explore the CORD-19 COVID-19 research dataset. The app provides interactive data visualizations, allowing users to filter and explore trends in COVID-19 research papers over time.

**Note**: The dataset used in this app has been truncated to only **1,000 rows** due to the large size of the original file (approximately **1.5GB**). This was done to make the app more manageable while still providing valuable insights.

## Features

* **Interactive Year Range Slider**: Allows users to select a year range to filter the dataset.

* **Visualizations**:
  
  * Number of publications over time.
  
  * Top journals publishing COVID-19 research papers.
  
  * Word cloud of most frequent terms in paper titles.

* **Sample Data**: Displays a sample of the dataset (title, year, and journal).

* **Dynamic Data Filtering**: Visualizations are updated based on the selected year range.

Requirements
------------

To run this app, you need Python 3.7+ and the following packages:

* `pandas`

* `matplotlib`

* `seaborn`

* `wordcloud`

* `streamlit`

You can install these dependencies using `pip`:

```bash
pip install pandas matplotlib seaborn wordcloud streamlit
```

Installation and Setup
----------------------

### 1. Download the Dataset

* Download the CORD-19 dataset from [Kaggle](https://www.kaggle.com/datasets/allen-institute-for-ai/CORD-19-research-challenge?select=metadata.csv)

* Extract the dataset and locate the `metadata.csv` file.

* **Note**: Due to the large file size (~1.5GB), this app uses a truncated version of the dataset, containing only **1,000 rows**. You can create a truncated version of the dataset by sampling 1,000 rows or using any relevant subset of the data for faster performance.

### 2. Clone or Download This Repository

Clone the repository or download the project folder to your local machine.

```bash
git clone https://github.com/edmondweb/Frameworks_Assignment.git
```

### 3. Place the Dataset

Place the `metadata.csv` file in the root directory of the project (or modify the `file_path` in the Streamlit app to point to the correct location).

### 4. Run the App

Once all dependencies are installed and the dataset is in place, run the following command to start the app:

```bash
streamlit run app.py
```

This will open the Streamlit app in your browser, where you can interact with the visualizations and explore the data.

## Usage

* **Select Year Range**: Use the slider to select a range of years (e.g., 2020 to 2021) and explore the corresponding data.

* **Explore Visualizations**:
  
  * The **Number of Publications Over Time** graph shows how research output has evolved over the selected years.
  
  * The **Top Journals Publishing COVID-19 Research** bar chart highlights the leading journals in COVID-19 research.
  
  * The **Word Cloud** shows the most frequent words from the titles of research papers.

* **Data Preview**: A table displaying a sample of the research papers filtered by the selected year range, including title, year, and journal.

File Structure
--------------

```bash
.
├── frame.ipynb      # Data preprocessing file.
├── app.py           # Main Streamlit app script
├── metadata.csv    # CORD-19 research dataset (metadata file)
└── README.md       # This README file
```

Contributing
------------

If you'd like to contribute to this project, feel free to fork the repository and submit pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License - see the LICENSE
