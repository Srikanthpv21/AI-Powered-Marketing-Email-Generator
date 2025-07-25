import streamlit as st

st.set_page_config(page_title="AI Email Personalizer", layout="centered")

st.title("📧 AI-Powered Marketing Email Generator")
st.subheader("Personalize emails in seconds!")

# Input form
with st.form("email_form"):
    name = st.text_input("Recipient Name", "Ramesh")
    company = st.text_input("Company Name", "AgroTech")
    product = st.text_input("Your Product", "SmartIrrigator")
    goal = st.text_input("Recipient's Goal", "Improve water efficiency")
    sender = st.text_input("Your Name", "Srikanth P V")

    submitted = st.form_submit_button("Generate Email")

# Output email
if submitted:
    email = f"""
Hi {name},

I hope you're doing well. I came across {company} and was really impressed by your focus on {goal}. 

I wanted to introduce you to **{product}**, an AI-powered solution designed to help companies like yours achieve results faster and more efficiently.

Would you be open to a quick demo or chat?

Best regards,  
{sender}
"""
    st.success("✅ Generated Email:")
    st.code(email, language="markdown")
