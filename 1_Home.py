from app_secrets import OPENAI_API_KEY
import os
import streamlit as st
from sql_execution import execute_sf_query
from langchain.llms.openai import OpenAI
from langchain.prompts import load_prompt
from pathlib import Path
from PIL import Image

def write_to_training_file(file_path,prompt,sql):
     try:
          with (open(file_path,'w')) as file:
               file.write("\n prompt : {}".format(prompt))
               file.write("\n sql : {}".format(sql))
               file.write("\n lable : 1 \n\n")
               file.close()
               return "success"
     except:
          print("problem in opening file")
          return "problem in openeing file"

#setup env variable
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
#project root directory
current_dir = Path(__file__)
root_dir = [p for p in current_dir.parents if p.parts[-1]=='ai_sql_assistant-main'][0]
#frontend

header_html = """
    <div style="background-image: url('https://example.com/your-background-image.jpg'); 
                background-size: cover; background-position: center; 
                padding: 20px; border-radius: 10px; text-align: center; color: black;">
        <h1>GenAI</h1>
        <p>
            <a href='#'>Home</a> |
            <a href='#section1'>Section1</a>
        </p>
    </div>
"""

# Display the HTML header in Streamlit
#st.markdown(header_html, unsafe_allow_html=True)

st.set_page_config(
    page_title="GenAI Demo",
    page_icon=""
)
#st.sidebar.success("Select a page above")

tab_titles=[
    "Results",
    "Query"
]

st.title("Your Data Assistant")
prompt = st.text_input("Your Request")

tabs = st.tabs(tab_titles)

prompt_template = load_prompt(f"{root_dir}/prompts/tpch_prompt.yaml")
final_prompt = prompt_template.format(input=prompt)

llm = OpenAI(temperature=0)

if prompt:
    query_text = llm(prompt=final_prompt)
    output = execute_sf_query(query_text)
    with tabs[0]:
        st.write(output)
    with tabs[1]:
        st.write(query_text)
       