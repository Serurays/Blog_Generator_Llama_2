import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# Function to get response from the Llama 2 model

def get_llama_response(input_text, no_words, blog_style):
    
    # Llama 2 model
    llm = CTransformers(
        model="C:/Users/MSI/Desktop/Langchain_Project/LLama_2/models/llama-2-7b-chat.ggmlv3.q8_0.bin",
        model_type="llama",
        config={"max_new_tokens":256,
                "temperature":0.01}
    )
    
    # Prompt Template
    template = """
            Write a blog for {blog_style} job profile for a topic {input_text}
            within the range of {no_words} words.
               """
               
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", "no_words"],
                            template=template)
    
    # Generate the response from the Llama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)
    
    return response


st.set_page_config(
    page_title="Blog Generator",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.header("Generate Blogs ✍️")

input_text = st.text_input("Enter the Blog Topic")

# Creating two more columns for the additional two fields
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No. of words")
with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Scientists", "Other People"), index=0)
    
submit = st.button("Generate")


# Final Response
if submit:
    st.write(get_llama_response(input_text, no_words, blog_style))