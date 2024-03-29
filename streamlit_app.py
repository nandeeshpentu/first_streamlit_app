import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinch & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Avocado'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page
streamlit.dataframe(fruits_to_show)

streamlit.write('The user entered ', fruit_choice)
import requests
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
 fruit_choice = streamlit.text_input('What fruit would you like information about?')
 if not fruit_choice:
   streamlit.error("Please Select a Fruit Get Information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
 streamlit.dataframe(back_from_function)
import snowflake.connector
my_cur = my_cnx.cursor()
streamlit.header("The fruit load list contains:")
#Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
return my_cur.fetchall()
#Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_data_rows = get_fruit_load_list()
streamlit.dataframe(my_data_rows)
