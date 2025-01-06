import streamlit as st
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
    st.caption('Search')
    text = st.text_input('Enter your query here:', placeholder='e.g. ')
    st.form_submit_button('Search')

if text:
    st.write('Your query is ', text)

lst = [1, 2, 3]
if st.button('Click me!'):
    for i in lst:
        st.write(i)
        st.divider()
    

