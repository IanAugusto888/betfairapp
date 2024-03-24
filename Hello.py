import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service= service)


def run():
    st.set_page_config(
        page_title="Betfair App",
    )
    st.write()

run()
