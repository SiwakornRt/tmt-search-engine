import streamlit as st

from main import *

st.set_page_config(
    page_title="TMT Search Engine",
    page_icon=":stars:",
    # layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('TMT Search Engine :mag::sparkles:')
with st.form('my_form'):
    st.caption('Find drug information (EN) for product names and manufacturer.')
    text = st.text_input('Enter your query here:', placeholder='e.g. SARA 325 mg, BETADINE ,sodium chloride injection, etc.')
    st.form_submit_button('Search')


if text:
    # st.write('Your query is ', text)
    tokens = tokenize(text)
    # st.write('Tokenized query:', tokens)
    corrected_text = misspelled_correction(tokens)
    st.write('Corrected text query:', corrected_text)
    st.write('Query result:')
    best = find_similar_word(corrected_text)
    st.write(best)

    

