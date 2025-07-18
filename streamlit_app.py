# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f":cup_with_straw: Customize your Smoothie :cup_with_straw: {st.__version__}")
st.write(
  """Choose the fruits you want in your smoothie).
  """
)

cnx = st.connection("snowflake")
session = cnx.session()
name_on_order = st.text_input("Name on Smoothie : ")
st.write("Name on your Smoothie will be: ", name_on_order)

my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('choose upto 5 ingrediants:', my_dataframe, max_selections = 5)

if ingredients_list:
  
    ingredients_string =''

    for fruit_chosen in ingredients_list:
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)

   # my_insert_stmt = """ insert into smoothies.public.orders(ingredients)
    #        values ('""" + ingredients_string + """')"""

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients, name_on_order)
            values ('""" + ingredients_string + """','"""+name_on_order+"""')"""

    #st.write(my_insert_stmt)
    #st.stop()

 #   if ingredients_string:
       # session.sql(my_insert_stmt).collect()
        #st.success('Your Smoothie is ordered!', icon="✅")

    time_to_insert = st.button('Submit Order')
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")
