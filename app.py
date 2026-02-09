import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI Business Analyst", layout="wide")

st.title("📊 AI Business Analyst")
st.markdown("Ask questions about your business database using natural language.")

question = st.text_input("Enter your question")

if st.button("Analyze"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Analyzing..."):

            response = requests.get(
                "http://127.0.0.1:8000/ask",
                params={"question": question}
            )

            data = response.json()

            if "error" in data:
                st.error(data["error"])
            else:
                st.subheader("🧠 Generated SQL")
                st.code(data["generated_sql"], language="sql")

                st.subheader("📈 Query Result")

                df = pd.DataFrame(data["result"])
                st.dataframe(df, use_container_width=True)

                # Auto simple chart if numeric column exists
                numeric_cols = df.select_dtypes(include="number").columns

                if len(numeric_cols) > 0:
                    st.subheader("📊 Visualization")
                    st.bar_chart(df.set_index(df.columns[0]))

                st.subheader("💡 Business Insight")
                st.success(data["insight"])