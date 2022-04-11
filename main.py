from tkinter.tix import INTEGER
from turtle import onclick
import streamlit as st
import pandas as pd
import numpy as np

# static count variable that updates on refresh

st.title('Testing this bitch')

if 'count' not in st.session_state:
    st.session_state.count = 0

def increment_counter():
    st.session_state.count += 1

st.button('Increment', on_click=increment_counter)

st.write('Count = ', st.session_state.count)