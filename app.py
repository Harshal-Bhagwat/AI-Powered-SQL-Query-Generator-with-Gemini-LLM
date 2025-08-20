import streamlit as st
import google.generativeai as genai
from api_key import API_KEY

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash-lite')

def main():
    st.set_page_config(page_title="AI SQL Query Generator by Harshal Bhagwat", page_icon=":robot:")
    st.markdown(
        """
            <div style="text-align: center;">
                <h1>AI-Powered SQL Query Generator with Gemini LLM🌐🤖</h1>
                <h3>Generate SQL Queries from Natural Language Prompts</h3>
                <h4>With Explanation also!!!</h4>
                <p>
                    This tool allows you to generate SQL queries based on your prompts.
                </p>
            </div>
        """,
        unsafe_allow_html=True
    )
    
    input=st.text_area("Enter your query in Human Language")
    
    Submit = st.button("Generate SQL Query")
    if Submit:
        with st.spinner("Generating SQL query..."):
            template = """
            Create a SQL query snippet using the below text:
            ```
                {input}
            ```
            I just want a SQL Query.
            """
            prompt = template.format(input=input)
            response = model.generate_content(prompt)
            sql_query = response.text

            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")

            expected_output = """
            Expected Output of this SQL query:
            ```
                {sql_query}
            ``` 
            Provide sample Tabular Response with no explanation.
            """
            prompt = expected_output.format(sql_query=sql_query)
            response = model.generate_content(prompt)
            exp_response = response.text

            explanation = """
            Explain this SQL Query:
            ```
                {sql_query}
            ```
            Please Provide with simplest of explanation.
            """
            prompt = explanation.format(sql_query=sql_query)
            response = model.generate_content(prompt)
            explain_response = response.text

            with st.container():
                st.success("SQL Query Generated Successfully! ")
                st.code(sql_query, language="sql")

                st.success("Expected Output of this SQL Query will be:")
                st.markdown(exp_response)

                st.success("Explanation of this SQL Query:")
                st.markdown(explain_response)

main()


