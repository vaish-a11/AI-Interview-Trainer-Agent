import streamlit as st

st.set_page_config(
    page_title="AI Interview Trainer Agent",
    page_icon="🤖"
)

st.title("🤖 AI Interview Trainer Agent")

st.write("""
This application helps users prepare for interviews by generating
technical and HR interview questions and providing interview guidance.
""")

role = st.text_input("Enter Job Role", placeholder="Example: Python Developer")

if st.button("Generate Interview Questions"):

    if role:

        st.subheader("Technical Interview Questions")

        st.write("1. Explain Object-Oriented Programming concepts.")
        st.write("2. What is inheritance and how is it used?")
        st.write("3. Explain polymorphism with an example.")
        st.write("4. What is exception handling?")
        st.write("5. Describe your recent project experience.")

        st.subheader("HR Interview Questions")

        st.write("1. Tell me about yourself.")
        st.write("2. Why do you want this role?")
        st.write("3. What are your strengths and weaknesses?")
        st.write("4. How do you handle pressure?")
        st.write("5. Where do you see yourself in five years?")

        st.subheader("Interview Tips")

        st.write("• Practice answering questions confidently.")
        st.write("• Highlight your project experience.")
        st.write("• Explain your technical skills clearly.")
        st.write("• Maintain good communication skills.")
        st.write("• Be honest and professional.")

    else:
        st.warning("Please enter a job role.")