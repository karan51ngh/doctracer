import streamlit as st
import os

st.set_page_config(
    page_title="My Portfolio",
    # page_icon="pics/icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
li = []


def func(path, tar):

    dir_list = os.listdir(path)
    temp = False
    for i in dir_list:
        pathx = path
        pathx = pathx+'/'+i
        if os.path.isdir(pathx):
            temp = temp or func(pathx, tar)
        if os.path.isfile(pathx):
            if i == tar:
                st.success("FOUND!")
                st.info("Location of the file:"+pathx)
                li.append(pathx)
                return True
            else:
                continue
    return temp
# path=st.text_input("enter the location of the root folder",value='/home/osboxes/defenceForces/army/1.officers')
# tar=st.text_input("enter the name of the file",value='ltKaran.txt')
# path = st.text_input("enter the location of the root folder")
# tar = st.text_input("enter the name of the file")


with st.form("my_form2"):
    path = st.text_input(
        'Enter the location of the directory you want to explore')
    tar = st.text_input('Enter the name of the file you want to search')
    submitted = st.form_submit_button("Submit")
    if submitted:
        flag = func(path, tar)
        if not flag:
            st.warning("File not found!")


# flag = func(path,tar,print=st.write)
