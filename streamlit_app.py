import streamlit

streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Bluberry Oatmeal')
streamlit.text('🥗 Kale, spinach & rocket smoothie')
streamlit.text('🐔 Hard boied- range free eggs')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

 
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
