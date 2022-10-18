import streamlit as st
from model import GeneralModel

def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("API key", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(input):

        return pred.model_prediction(input=input.strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("A Passive Voice Checker for Your Writing")

        #st.write("---")
        st.markdown("This app will help you identify when you are using passive voice in your writing and suggest ways to rewrite your sentences in\n active voice.")
        label = ""
        s_example = "The lamp was knocked over by a gust of wind."
        input = st.text_area(
            label,
            value=s_example,
            max_chars=1250,
            height=50,
        )

        if st.button("Check your text"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(input)
                st.markdown(report_text)
    else:
        st.error("Please enter your OpenAI API key. This can be found on:\n https://beta.openai.com/account/api-keys")
       