import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon=":lock:" )

st.title("🔐Password Strength Checker")
st.markdown(""""
## welcome to the ultimate password strength checker!👋
use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a **strong password** 🔒  """)   

password = st.text_input("Enter your password here", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score += 1
    else :
        feedback.append("❌Password should be al least 8 characters long.")

        if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
            score += 1
        else:
            feedback.append("❌Password should contain both uppercase and lowercase characters.")

            if re.search(r'\d', password):
                score += 1
            else:
                feedback.append("❌Password should contain at least one digit.")

                if re.search(r'[!@#$%&*]', password):
                    score += 1
                else:
                    feedback.append("❌Password should cotain at least one special character.(!@#$%&*)")
                    if score == 4:
                        feedback.append("✅Your password is strong and secure!🎉")
                    elif score == 3:
                        feedback.append("🟡Y our password is good, but it could be stronger")
                    else:
                        feedback.append("🔴Your password is weak. please make it stronger.")

                        if feedback:
                            st.markdown("## Improvement suggestions")
                            for tip in feedback:
                                st.write(tip)
else:
    st.info("Please enter a password to get started.")
