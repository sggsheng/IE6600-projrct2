import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("The data of London")
st.write('For this project, I will show data from the 2011 Census for the Greater London area')
st.title('Variable Explanation')
st.write('MedianHP: Median House Price, PopulationDensity: Population Density (People/Hectare), WorkingAge: Percentage of the population who are of working age, ObesityRate: Percentage of the adult population who are obese, LifeExpectancy: Average Life Expectancy, Unemployed: Unemployment Rate, MedianHHIncome: Median Household Income, CarsPerHH: The mean number of cars per household, OwnershipRate: The proportion of residencies which are owned (as opposed to rented), Sales: The number of residencies sold in the last year')

file_path = 'LondonData.xlsx' 
data = pd.read_excel(file_path)

selected_columns = ['MedianHP','PopulationDensity', 'WorkingAge', 
                    'ObesityRate', 'LifeExpectancy', 'Unemployed', 
                    'MedianHHIncome', 'CarsPerHH', 'OwnershipRate', 'Sales']
filtered_data = data[selected_columns]

selected_column = st.selectbox("Now you can select the data you are interested in and observe its distribution", selected_columns)

if selected_column:
    st.write(f"### `Distribution of {selected_column}`")
    fig, ax = plt.subplots()
    filtered_data[selected_column].dropna().hist(ax=ax, bins=30)
    ax.set_title(f"{selected_column} ")
    ax.set_xlabel(selected_column)
    ax.set_ylabel("Density")
    st.pyplot(fig)

x_column = st.selectbox("Please select data for X-axis", selected_columns)
y_column = st.selectbox("Please select data for Y-axis", selected_columns)

if x_column and y_column:
    st.write(f"### `{x_column}` and `{y_column}` ")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.scatterplot(
        data=data, 
        x=x_column, 
        y=y_column, 
        hue=data['Inner'],
        palette='Set2',
        ax=ax
    )
    ax.set_title(f"{x_column} vs {y_column}")
    ax.set_xlabel(x_column)
    ax.set_ylabel(y_column)
    st.pyplot(fig)
    
    
st.title("Percentage of different Median House Hold Income in Inner and Outer London")
min_income = int(data['MedianHHIncome'].min())
max_income = int(data['MedianHHIncome'].max())
income_range = st.slider(
    "Select a range for Median House Hold Income",
    min_value=min_income,
    max_value=max_income,
    value=(min_income, max_income),
    step=1000
    )

filtered_data = data[(data['MedianHHIncome'] >= income_range[0]) & (data['MedianHHIncome'] <= income_range[1])]

if not filtered_data.empty:
    pie_data = filtered_data['Inner'].value_counts()

    fig, ax = plt.subplots()
    ax.pie(
        pie_data,
        labels=pie_data.index,
        autopct='%1.1f%%',
        startangle=90,
        wedgeprops={'edgecolor': 'black'}
    )
    #ax.set_title("Inner and Outer London")
    st.pyplot(fig)
else:
    st.warning("There is no data in the filter range, please adjust the slider")
    
    
st.title("Political parties and unemployment rate")
    
fig, ax = plt.subplots(figsize=(8, 6))
sns.boxplot(
    data=data,
    x='Political',
    y='Unemployed',
    palette='Set3',
    ax=ax
)
ax.set_title("Unemployed vs Political parties")
ax.set_xlabel("Political party")
ax.set_ylabel("Unemployment Rate")
st.pyplot(fig)
