import streamlit as st
import pandas as pd

# set layout of page/format it correctly
st.set_page_config(layout="wide")

# get col1, 2 as object instances
col1, col2 = st.columns(2)

# open column
with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Matt Halden")
    content = """
    Hey, I am Matt Halden.
    I like dogs.
    """
    st.info(content)

st.write("Below is our apps you can find")

# col 3, 4 will be the two columns under the first row!
col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df.iterrows():
        st.header(row["title"])

with col4:
    for index, row in df.iterrows():
        st.header(row["title"])