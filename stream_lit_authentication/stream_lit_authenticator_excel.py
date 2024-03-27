
import pickle
from pathlib import path
import pandas as pd

import plotly.express as px
import streamlit as st
import streamlit_authenticator as suath

st.set_page_config(page_title="Sales Dashboard",layout="wide")

## user authentication

names=["Sam","John"]
usernames=["ssam","jjohn"]
password=['Xx','xx']
hashed_passwords=stauth.Hasher(passwords).generate()

hashed_passwords=sauth.Hasher(passwords).generate()
file_path=Path(__file__).parent/ "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)

authenticator=st.Authenticate(names,usernames,hashed_passwords,"sales_dashboards","abcdef",cookie_expiry_days=30)

name,authentication_status,username=authenticator.login("Login","main")

if authentication_status==False:
    st.error("Username/password is incorrect")
if authentication_status==None:
    st.warning("Please enter the username and password")
if authentication_status:
    
    @st.cache
    def get_data():
        df=pd.read_excel(io="super_market_sales.xlsx",engine="openpyxl",sheet_name="Sales")
        df["hour"]=pd.to_datetime(df["Time"],format="%H:%M:%S").dt.hour
    df=get_data()
    authenticator.logout("Logout","sidebar")
    st.sidebar.title("Welcome {name}")
    st.sidebar.header("Please filter here")
    
    st.sidebar.header("Please filter here")
    city=st.sidebar.multiselect("Select the city",options=df["City"].unique(),default=df["City"].unique())
    
    
    