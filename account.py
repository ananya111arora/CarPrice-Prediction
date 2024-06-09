import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('price-prediction-f6ed9-7f690b17b82f.json')
firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome to Prediction :violet[World]')
    
    
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
   






    def f():
        try:
            user = auth.get_user_by_email(email)
            #print(user.uid)
            st.write('Login Successfull')
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            
           # global Usernm
           # Usernm=(userinfo['username'])
            
            st.session_state.signedout = True
            st.session_state.signout = True    

        except:
            st.warning('Login Failed')
    def t():
        st.session_state.signout = False
        st.session_state.signedout = False   
        st.session_state.username = ''






    if "signedout"  not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False   
    if  not st.session_state["signedout"]:
        choice = st.selectbox('Login/Signup',['Login', 'Sign Up'])
        if choice == 'Login':
           email = st.text_input('Email Address')
           password = st.text_input('Password', type='password')

           st.button('Login', on_click=f)
        else:
         
           email = st.text_input('Email Address')
           password = st.text_input('Password', type = 'password')
           username = st.text_input('Enter your unique username')

           if st.button('create my account'):
              user = auth.create_user(email = email, password = password, uid = username)  # Corrected function call
              st.success('Account created successfully')
              st.markdown('Please Login using your email and password')
              st.balloons()

 

    if st.session_state.signout:
        st.text('Name '+st.session_state.username)
        st.text('Email id: '+st.session_state.useremail)
        st.button('Sign out', on_click=t) 
   

def ap():
        st.write('posts')
