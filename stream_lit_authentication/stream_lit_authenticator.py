
import pickle
from pathlib import Path

import streamlit_authenticator as sauth

names=["Sam","John"]
usernames=["ssam","jjohn"]
password=['Xx','xx']
hashed_passwords=stauth.Hasher(passwords).generate()

hashed_passwords=sauth.Hasher(passwords).generate()
file_path=Path(__file__).parent/ "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)
