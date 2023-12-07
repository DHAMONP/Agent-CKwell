from app_secrets import OPENAI_API_KEY
import os
import streamlit as st
import pandas as pd
from sql_execution import execute_sf_query
from langchain import OpenAI
from langchain.prompts import load_prompt
from pathlib import Path


def main():
    #setup env variable
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    #project root directory
    current_dir = Path(__file__)
    root_dir = [p for p in current_dir.parents if p.parts[-1]=='ai_sql_assistant-main'][0]
    #frontend
    st.title("GenAI")
    prompt = st.text_input("Your Request")

    prompt_template = load_prompt(f"{root_dir}/prompts/tpch_prompt.yaml")
    final_prompt = prompt_template.format(input=prompt)

    llm = OpenAI(temperature=0)
    #apikey = st.secrets.OPENAI_API_KEY
    if prompt:
        response = llm(prompt=final_prompt)
        with st.expander(label="SQL Query",expanded=False):
            st.write(response)
        output = execute_sf_query(response)
        st.write(output)

      
    

if __name__ == "__main__":
    main()



