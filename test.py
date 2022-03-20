import pyrebase
import streamlit as sto
from datetime import datetime


constfirebaseConfig = {
  apiKey: "AIzaSyAROyZWfOBwKpWayFED_sQr0B4goq9_tFM",
  authDomain: "login-page-fa6fd.firebaseapp.com",
  databaseURL: "https://login-page-fa6fd-default-rtdb.firebaseio.com",
  projectId: "login-page-fa6fd",
  storageBucket: "login-page-fa6fd.appspot.com",
  messagingSenderId: "685432298169",
  appId: "1:685432298169:web:1e926aafe661e9e1eb1968",
  measurementId: "G-9FX4G0GB6W"
};


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

data = firebase.database()
storage = firebase.storage()

sto.sidebar.title("My Research Application")

choice = sto.sidebar.selectbox('SignIn/SignUp', ['Login', 'Sign Up'])


Username = sto.sidebar.text_input('Enter your username')

Password = sto.sidebar.text_input('Enter your passowrd', type = 'password')

EmailAddress = sto.sidebar.text_input('Enter your email address')


if choice == 'Sign Up':
   handle = sto.sidebar.text_input("Enter your Username", value = Default)
   handle = sto.sidebar.text_input("Re-enter your password", value = Default)
   submit = sto.sidebar.button("Continue")

if choice == 'Submit':
    user = auth.create_user_with_Username_EmailAddress_and_Password(Username,EmailAddress,Password)
    sto.success("Your account is created")
    sto.cars


    user = auth.sign_in_with_Username_and_Password()

    data.child(user[localId]).child("Handle").set(handle)
    data.child(user[localId]).child("ID").set(user['localId'])
    sto.title('Welcome' + handle)
    sto.info('Login via login dropdown menu selected')
    if choice == 'Login':
        login = st.sidebar.checkbox('Login')
        if login:
            user = auth.sign_in_with_Username_EmailAddress_and_Password(Username,EmailAddress,Password)
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}<style>', unsafe_allow_ht)