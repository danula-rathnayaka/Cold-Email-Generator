import streamlit as st

# Set the title and layout
st.set_page_config(page_title="📧 Cold Mail Generator", layout="wide")
st.title("📧 Welcome to the Cold Mail Generator!")
st.markdown("""
    This tool helps you create **personalized cold emails** for job applications based on the job description from a given URL. 

    ### How It Works:
    1. **Enter the Job URL**: Provide the link to the job listing you want to apply for.
    2. **Generate Email**: Click the **'Generate Email'** button to create a tailored email.
    3. **Customize**: Review the generated email and make any necessary adjustments before sending.

    Ready to get started? Enter the job URL below!
""")

# Input field for the URL
url_input = st.text_input("Enter a Job URL:", value="https://jobs.nike.com/job/R-45600")

# Submit button
submit_button = st.button("Generate Email")

# Sample email text (this would be generated based on the job description in a real scenario)
sample_email = """
Subject: Application for [Job Title] Position
Dear [Hiring Manager's Name],
I hope this message finds you well. I recently came across the [Job Title] position at [Company Name] and was excited to apply. With my background in [Your Field/Skill] and experience in [Relevant Experience], I believe I would be a great fit for your team.
I am particularly drawn to this role because [Reason for Interest in the Job/Company]. I am eager to bring my skills in [Specific Skills] to [Company Name] and contribute to [Specific Goals or Projects].
Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to your team.
Best regards,
[Your Name]
[Your LinkedIn Profile or Contact Information]
"""

# Process the input when the button is clicked
if submit_button:
    st.subheader("Generated Email:")
    st.code(sample_email, language='markdown')