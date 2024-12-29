import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text
from portfolio import Portfolio
from chains import Chain
import pandas as pd

def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Welcome to the Cold Mail Generator!")
    st.markdown("""
        This tool helps you create **personalized cold emails** for job applications based on the job description from a given URL. 
    
        ### How It Works:
        1. **Enter the Job URL**: Provide the link to the job listing you want to apply for.
        2. **Generate Email**: Click the **'Generate Email'** button to create a tailored email.
        3. **Customize**: Review the generated email and make any necessary adjustments before sending.
    
        Ready to get started? Enter the job URL below!
    """)

    url_input = st.text_input("Enter a Job URL:", value="https://jobs.nike.com/job/R-42713")

    submit_button = st.button("Generate Email")

    if submit_button:
        try:
            loader = WebBaseLoader(url_input)
            data = clean_text(loader.load().pop().page_content)
            jobs = llm.extract_jobs(data)

            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_email(job, links)

                st.subheader("Generated Email:")
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f'An Error Occored: {e}')

    for _ in range(3):
        st.write("")

    if 'portfolio_data' not in st.session_state:
        st.session_state.portfolio_data = portfolio.get_data()

    st.subheader("Current Techstack Data")
    st.table(st.session_state.portfolio_data)

    if st.button("Refresh Table"):
        st.session_state.portfolio_data = portfolio.get_data()

    for _ in range(3):
        st.write("")

    st.subheader("Add Techstack Data")
    with st.form("add_form"):
        techstacks = st.text_input("Techstacks")
        link = st.text_input("Link")
        submitted = st.form_submit_button("Add Entry")
        if submitted and techstacks and link:
            portfolio.add_data(techstacks, link)
            st.session_state.portfolio_data = portfolio.get_data()
            st.success("Entry added!")


if __name__ == "__main__":
    st.set_page_config(page_title="Cold Mail Generator", layout="wide", page_icon="📧")
    create_streamlit_app(Chain(), Portfolio(), clean_text)
