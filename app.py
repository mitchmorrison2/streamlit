import sys
from streamlit import cli as stcli
import streamlit as st
import pandas as pd
import numpy as np
from tinydb import TinyDB, Query

db = TinyDB('./.db.json')

comments = db.table('comments')

def main():
    global comments
    st.title('testing Streamlit')
    if 'counter' not in st.session_state:
        st.session_state['counter'] = 0


    increment = st.button('Click me to increment')
    if increment:
        st.session_state['counter'] += 1
    st.write(st.session_state['counter'])

    userName = st.text_input('Enter your name', 'Type here')
    txt = st.text_input('Enter your comment and username')
    if st.button('Submit'):
        comments.insert({'username': userName, 'comment': txt})

    st.write("Comments:")
    print("comments:", comments.all())
    for i in range(len(comments.all())):
        st.write(comments.all()[i]['username'], ": ", comments.all()[i]['comment'])

if __name__ == '__main__':
    # Start the streamlit app
    if st._is_running_with_streamlit:
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
