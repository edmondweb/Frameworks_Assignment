import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
from collections import Counter

# Load the CORD-19 dataset
data = pd.read_csv('metadata.csv')

# Clean the data
data['publish_time'] = pd.to_datetime(data['publish_time'], errors='coerce')
data['publish_year'] = data['publish_time'].dt.year
data['abstract_word_count'] = data['abstract'].apply(lambda x: len(str(x).split()))
data_cleaned = data.dropna(subset=['title', 'abstract'])

# Set up the Streamlit app
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers")

# Interactive slider to select year range
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
st.write(f"Showing data for years: {year_range[0]} to {year_range[1]}")

# Filter data based on the selected year range
filtered_data = data_cleaned[(data_cleaned['publish_year'] >= year_range[0]) & (data_cleaned['publish_year'] <= year_range[1])]

# Show a sample of the data
st.subheader("Sample of Data")
st.write(filtered_data[['title', 'publish_year', 'journal']].head())

# Plot the number of publications over time for the selected year range
st.subheader("Number of Publications Over Time")
plt.figure(figsize=(10, 6))
sns.countplot(data=filtered_data, x='publish_year', palette='viridis')
plt.title('Number of Publications Over Time')
plt.xlabel('Publication Year')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
st.pyplot(plt)

# Show top journals for the selected year range
st.subheader("Top Journals Publishing COVID-19 Research")
top_journals = filtered_data['journal'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_journals.plot(kind='bar', color='skyblue')
plt.title('Top Journals Publishing COVID-19 Research')
plt.xlabel('Journal')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
st.pyplot(plt)

# Generate a word cloud of paper titles
st.subheader("Word Cloud of Paper Titles")
text = ' '.join(filtered_data['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
st.pyplot(plt)