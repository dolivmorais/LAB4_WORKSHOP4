import streamlit as st
class ExcelValidatorUI:

    def __init__(self):
        self.set_page_config()

    def set_page_config(self):
        st.set_page_config(
            page_title="Validator Excel",
        )
    
    def display_header(self):
        st.title("Validator Excel")

    def upload_file(self):
        return st.file_uploader("Carregar arquivo Excel", type=["xlsx"])

