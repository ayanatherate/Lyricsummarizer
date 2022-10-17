# -*- coding: utf-8 -*-


def get_lyrics(inp):
    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from bs4 import BeautifulSoup
    
    
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #browser = webdriver.Chrome(
        #executable_path=r"C:\Users\User\Desktop\PROGRAM_FILES\chromedriver")
    
    lyrics_text=[]
    strung_together=''.join(inp.split(' '))
    initial="https://www.google.com/search?q="
    str_=f"{initial}{strung_together}+lyrics&oq="
    
    browser.get(str_) 
    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')
    
    lyrics_soup = soup.find_all('div', {'class': 'ujudUb'})
    for span_tags in lyrics_soup:
        span_content=soup.find_all('span', {'jsname': 'YS01Ge'})
        for embedded_lyrics in span_content:
            lyrics_text.append(embedded_lyrics.get_text())
    
    
    return lyrics_text


def ask_inp(inputfromuser):
    #song_inf=str(input("Enter artist name and song name space separated: "))    
    return get_lyrics(inputfromuser)

if __name__=='__main__':
    ask_inp()
