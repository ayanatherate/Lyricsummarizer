


import streamlit as st
import get_lyrics
from transformers import pipeline



#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

st.title('Music Lyrics Summarizer')
st.subheader('A Summary of the lyrics of your favourite English songs, prepared by AI')



    
    
   


    

#lyrics=get_lyrics(inp) 

def to_summary(inp):
    transcript=''
    lyrics=get_lyrics.ask_inp(inp) 
    for i in lyrics:
        transcript+=i+'.'+' '
    try:
        summed=summarizer(transcript[:len(transcript)],max_length=200,min_length=100)
    except IndexError:
        summed=summarizer(transcript[:3000],max_length=200,min_length=100)
        
    return summed[0]['summary_text']
    

summarizer = pipeline("summarization", model="knkarthick/MEETING-SUMMARY-BART-LARGE-XSUM-SAMSUM-DIALOGSUM") 

def take_inp():
    inp=st.text_input(label='Insert song name and artist name:')
    return inp


inp=take_inp()


if len(inp)>2:
    st.caption('Please wait while the AI tries to read the lyrics of your song from Google and understand it.')
    st.caption("<->  You have a cool music taste. But what's cooler is my ability to understand music  <->")
    st.write(to_summary(inp))
    st.stop()
else:
    st.stop()

if __name__=='__main__':
    take_inp()
    
