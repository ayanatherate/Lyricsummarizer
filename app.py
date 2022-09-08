# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:02:01 2022

@author: User
"""

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import glob


import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")


def delete_selenium_log():
    if os.path.exists('selenium.log'):
        os.remove('selenium.log')


def show_selenium_log():
    if os.path.exists('selenium.log'):
        with open('selenium.log') as f:
            content = f.read()
            st.code(content)


from transformers import pipeline


driver=webdriver.Chrome(options=options, service_log_path='selenium.log')
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

st.title('Music Lyrics Summarizer')
st.subheader('A Summary of the lyrics of your favourite English songs, prepared by AI')
def get_lyrics(inp):
    
    lyrics_text=[]
    strung_together=''.join(inp.split(' '))
    initial="https://www.google.com/search?q="
    str_=f"{initial}{strung_together}+lyrics&oq="
    
    driver.get(str_) 
    src = driver.page_source
    soup = BeautifulSoup(src, 'lxml')
    
    lyrics_soup = soup.find_all('div', {'class': 'ujudUb'})
    for span_tags in lyrics_soup:
        span_content=soup.find_all('span', {'jsname': 'YS01Ge'})
        for embedded_lyrics in span_content:
            lyrics_text.append(embedded_lyrics.get_text())
    return lyrics_text

inp=st.text_input(label='Insert song name and artist name:')
st.caption('Please wait while the AI tries to read the lyrics of your song from Google and understand it.')

lyrics=get_lyrics(inp) 
transcript=''
for i in lyrics:
    transcript+=i+'.'+' '
summarizer = pipeline("summarization", model="knkarthick/MEETING-SUMMARY-BART-LARGE-XSUM-SAMSUM-DIALOGSUM") 

def summarize(lyrics):
    try:
        summed=summarizer(transcript[:len(transcript)],max_length=200,min_length=100)
    except IndexError:
        summed=summarizer(transcript[:3000],max_length=200,min_length=100)
        
    return summed[0]['summary_text']

summary=summarize(transcript[:len(transcript)-10])
#print(summary)
st.caption("<->  You have a cool music taste. But what's cooler is my ability to understand music  <->")
st.write(summary)

st.stop()

