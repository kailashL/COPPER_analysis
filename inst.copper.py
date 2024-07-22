import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'C:\Users\kailash\Downloads\Copper_Set.xlsx - Result 1 (1).csv'
data = pd.read_csv(file_path)

# Streamlit app
st.title('Industrial Copper Modeling')

# Display the dataset
st.header('Dataset')
st.write(data)

# Summary statistics
st.header('Summary Statistics')
st.write(data.describe(include='all'))

# Missing values
st.header('Missing Values')
st.write(data.isnull().sum())

# Filter by country
st.sidebar.header('Filter Options')
countries = data['country'].dropna().unique()
selected_country = st.sidebar.selectbox('Select country:', countries)
filtered_data = data[data['country'] == selected_country]

st.header(f'Data for country: {selected_country}')
st.write(filtered_data)

# Visualize distributions
st.header('Distributions of Key Columns')

# Histogram for thickness
st.subheader('Thickness Distribution')
fig, ax = plt.subplots()
ax.hist(data['thickness'].dropna(), bins=20, edgecolor='k')
ax.set_xlabel('Thickness')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Histogram for width
st.subheader('Width Distribution')
fig, ax = plt.subplots()
ax.hist(data['width'].dropna(), bins=20, edgecolor='k')
ax.set_xlabel('Width')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Histogram for selling_price
st.subheader('Selling Price Distribution')
fig, ax = plt.subplots()
ax.hist(data['selling_price'].dropna(), bins=20, edgecolor='k')
ax.set_xlabel('Selling Price')
ax.set_ylabel('Frequency')
st.pyplot(fig)

# Filter by item type
item_types = data['item type'].dropna().unique()
selected_item_type = st.sidebar.selectbox('Select item type:', item_types)
filtered_data_by_item_type = data[data['item type'] == selected_item_type]

st.header(f'Data for item type: {selected_item_type}')
st.write(filtered_data_by_item_type)




