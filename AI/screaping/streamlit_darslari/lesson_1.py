from inspect import markcoroutinefunction
import json
import streamlit as st

st.title("Salom! Men streamlit web app man.")
st.subheader("Salom men subheader man.")
st.header("Salom men header man.")
st.text("Salom men text man.")
# st.markdown("")


st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
...     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
...     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
...             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.markdown(''' :yellow[sariq rang] :blue[ko'k rang]  :red[qizil rang] __ :rainbow[rainbow rang] ''')


json={"a":"1,2,3", "b": "4, 5, 6"}
st.json(json)

code="""
print("hello world")
def funct():
    return 0; """
st.code(code, language="python")