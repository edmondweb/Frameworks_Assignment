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

# Convert 'publish_time' to datetime
data_cleaned['publish_time'] = pd.to_datetime(data_cleaned['publish_time'], errors='coerce')

# Check for any invalid datetime values (these will be set to NaT)
invalid_dates = data_cleaned[data_cleaned['publish_time'].isna()]
# st.write("### Invalid Dates:")
# st.write(invalid_dates.head())

# Extract the year from 'publish_time' into a new column 'publish_year'
data_cleaned['publish_year'] = data_cleaned['publish_time'].dt.year

# Create a new column 'abstract_word_count' that counts the number of words in the abstract
data_cleaned['abstract_word_count'] = data_cleaned['abstract'].apply(lambda x: len(str(x).split()))

# Display cleaned data sample
st.write("### Cleaned Data Sample:")
st.write(data_cleaned.head())


# Part 3: Data Analysis and Visualization

# Count the number of papers by publication year
papers_by_year = data_cleaned.groupby('publish_year').size()
st.write("### Papers by Year:")
st.write(papers_by_year)

# Count the number of papers by journal
top_journals = data_cleaned['journal'].value_counts().head(10)
# st.write("### Top Journals Publishing COVID-19 Research:")
# st.write(top_journals)

# Function to clean and tokenize the titles
def clean_and_tokenize(title):
    # Remove non-alphanumeric characters and split into words
    words = re.findall(r'\w+', title.lower())
    return words

# Tokenize all titles and count the frequency of words
all_words = data_cleaned['title'].apply(clean_and_tokenize).sum()
word_counts = Counter(all_words)

# Display the most common words
# st.write("### Most Common Words in Titles:")
# st.write(word_counts.most_common(10))


# Create visualizations

# Plot the number of publications over time (by publication year)
st.subheader("Number of Publications Over Time")
plt.figure(figsize=(10, 6))
sns.countplot(data=data_cleaned, x='publish_year', palette='viridis')
plt.title('Number of Publications Over Time')
plt.xlabel('Publication Year')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
st.pyplot(plt)


# Create a bar chart for top publishing journals
st.subheader("Top Publishing Journals")
if not top_journals.empty:
    plt.figure(figsize=(10, 6))
    top_journals.plot(kind='bar', color='skyblue')
    plt.title('Top Journals Publishing COVID-19 Research')
    plt.xlabel('Journal')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write("No journals found for the selected year range.")


# Generate a Word Cloud of Paper Titles
st.subheader("Word Cloud of Paper Titles")
text = ' '.join(data_cleaned['title'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Paper Titles')
st.pyplot(plt)


# Plot distribution of paper counts by source
st.subheader("Distribution of Paper Counts by Source")
plt.figure(figsize=(10, 6))
sns.countplot(data=data_cleaned, x='source_x', palette='viridis')
plt.title('Distribution of Paper Counts by Source')
plt.xlabel('Source')
plt.ylabel('Number of Publications')
plt.xticks(rotation=45)
st.pyplot(plt)