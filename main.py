import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text
from portfolio import Portfolio
from chains import Chain

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
            print(e)

if __name__ == "__main__":
    st.set_page_config(page_title="Cold Mail Generator", layout="wide", page_icon="📧")
    create_streamlit_app(Chain(), Portfolio(), clean_text)
