import os
import streamlit as st
from groq import Groq

GROQ_API_KEY="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"

client = Groq(api_key=GROQ_API_KEY)

# Function to generate study plan and tips using Groq API
def get_study_plan(subject, days, hours_per_day):
    # Create the message for the Groq API
    user_message = f"Create a personalized study plan for {subject} in {days} days, studying {hours_per_day} hours per day. Provide tips, resources, and productivity advice."

    # Make the API request to Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-8b-8192",  # Choose the model based on your need
    )

    # Return the response content
    return chat_completion.choices[0].message.content

# Streamlit App Layout
st.title("Personalized Study Assistant Chatbot")

# User Input Fields
subject = st.text_input("Enter the subject/topic you are studying:")
days = st.number_input("Enter the number of days you have to prepare:", min_value=1, step=1)
hours_per_day = st.number_input("Enter the number of hours you can dedicate per day:", min_value=1, step=1)

# Button to Generate Study Plan
if st.button("Generate Study Plan"):
    if subject and days and hours_per_day:
        study_plan = get_study_plan(subject, days, hours_per_day)
        st.subheader("Your Personalized Study Plan:")
        st.write(study_plan)  # Display the study plan
    else:
        st.error("Please fill out all the fields!")

# Optional: User can ask additional questions
user_query = st.text_input("Ask for more tips or resources:")
if user_query:
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": user_query}],
        model="llama3-8b-8192",
    )
    response = chat_completion.choices[0].message.content
    st.write(response)

# Instructions and additional info
st.sidebar.markdown("### How to Use:")
st.sidebar.write("""
- Enter the subject or topic you're studying.
- Specify the number of days you have until your exam or deadline.
- Indicate how many hours you can dedicate each day to studying.
- Click on "Generate Study Plan" to receive personalized study advice.
- You can also ask for additional tips or resources in the input below.
""")
