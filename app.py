import re
import streamlit as st

st.set_page_config(page_title="Make Password perfect",page_icon="",layout="centered")

#custom css

st.markdown("""
            <style>
            .main {text-align: center;}
            .stTextInput {width: 60% !important; margin: }
            .stButton button {width: 50%; background-color #4CAF50;color: white; font-size:18px}
            .stButton button:hover {background-color:#45a049;}
            </style>
            """, unsafe_allow_html=True)

st.title("Password Strength required please")
st.write("Enter your password below to check its strength")


def check_password_strength(password):
    score=0
    feedback=[]

    if len(password) >=8:
        score +=1
    else:
        feedback.append("Password should be 8 or more char")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]",password):
        score+=1
    else:
        feedback.append("password should include upper lower as well")
    if re.search(r"\d", password):
        score+=1
    else:
        feedback.append("Password should contain number as well")
    if re.search(r"[!@#$%^&*]",password):
        score+=1
    else:
        feedback.append("include special char as well ")
    #display password
    if score == 4:
        st.success("good one")
    elif score== 3:
        st.info("not good enough")
    else:
        st.error("week Password")
    
    if feedback:
        with st.expander("** not perfect"):
            for item in feedback:
                st.write(item)

password = st.text_input("type correct and strong pass", type="password", help="enter proper")

if st.button("stregth:"):
    if password:
        check_password_strength(password)
    else:
        st.warning("please enter proper ")






            
      



