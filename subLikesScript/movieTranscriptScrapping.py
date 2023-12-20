from bs4 import BeautifulSoup
import requests
import os
import re
# from flask import Flask

def sanatize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]',' ',filename)
def moviesTranscriptStartingChar(char):
    root='https://subslikescript.com'
    website=f'{root}/movies_letter-{char}'
    AlphabetResult=requests.get(website)
    AlphabetResultcontent=AlphabetResult.text

    listsoup=BeautifulSoup(AlphabetResultcontent,'lxml')
    # print(soup.prettify())

    # pagination
    pagination=listsoup.find('ul',class_='pagination')
    pages=pagination.find_all('li',class_='page-item')
    last_page=pages[-2].text

    for page in range(1,int(last_page)+1):

        pageWebsite=f'{website}?page={page}'
        print(pageWebsite)
        result=requests.get(pageWebsite)
    
        contentListMovies=result.text
        soup=BeautifulSoup(contentListMovies,'lxml')
        boxListMovies=soup.find('article',class_='main-article')
        linksOfMovies=[]
        
        for link in boxListMovies.find_all('a',href=True):            
            linksOfMovies.append(link['href'])
        print(linksOfMovies)
        for link in linksOfMovies:
            movieTranscriptPage=f'{root}/{link}'
            movieResult=requests.get(movieTranscriptPage)
            movieContent=movieResult.text
            soap=BeautifulSoup(movieContent,'lxml')
            movieContentBox=soap.find('article',class_='main-article')
            # print(title)
            movieTitle=movieContentBox.find('h1').get_text()
            movieTranscript=movieContentBox.find('div',class_='full-script').get_text(strip=True,separator=' ')
            # print(transcript)
            file_name = f'{sanatize_filename(movieTitle)}.txt'
            folder_path = 'C:/Users/HP/Desktop/subLikesScript/subscript storage/'
            file_path = os.path.join(folder_path, file_name)

            try:
                with open (file_path,'w',encoding='utf-8') as file: # title + .txt
                    
                    file.write(movieTitle+'\n')
                    file.write(movieTranscript)
                    print(f'The file "{file_name}" has been created in the folder "{folder_path}".')
            except OSError as e :
                print(f"Error writing file: {e}")
def allMovieTranscript():
    for letter in range(ord('A'),ord('Z')+1):
        moviesTranscriptStartingChar(chr(letter))


def movieTranscriptBetter( str):
    root='https://subslikescript.com'
    char=str[0]
    website=f'{root}/movies_letter-{char}'
    alphabetResult=requests.get(website)
    alphabetResultContent=alphabetResult.text

    listsSoup=BeautifulSoup(alphabetResultContent,'lxml')


    pagination=listsSoup.find('ul',class_='pagination')
    pages=pagination.find_all('li',class_='page-item')
    last_page=pages[-2].text

    for page in range(1,int(last_page)):
        page_link=f'{website}?page={page}'
        movieListResult=requests.get(page_link)
        movieListResultContent=movieListResult.text
        movieListResultsoup=BeautifulSoup(movieListResultContent,'lxml')

        movieList=[]
        moviesListBox=movieListResultsoup.find('ul',class_='scripts-list')

        for movie in moviesListBox.find_all('a',href=True):
            title=movie.find('li').text
            if(title==str):
                
                movieLink=movie['href']
                movieTranscriptPage=f'{root}/{movieLink}'
                
                movieResult=requests.get(movieTranscriptPage)
                movieContent=movieResult.text
                
                soap=BeautifulSoup(movieContent,'lxml')
                movieContentBox=soap.find('article',class_='main-article')
                
                movieTitle=movieContentBox.find('h1').get_text()
                
                movieTranscript=movieContentBox.find('div',class_='full-script').get_text(strip=True,separator=' ')
                
                file_name = f'{sanatize_filename(movieTitle)}.txt'
                folder_path = 'C:/Users/HP/Desktop/subLikesScript/subscript storage/'
                file_path = os.path.join(folder_path, file_name)
                try:
                    with open (file_path,'w',encoding='utf-8') as file: # title + .txt
                        
                        file.write(movieTitle+'\n')
                        file.write(movieTranscript)
                        print(f'The file "{file_name}" has been created in the folder "{folder_path}".')
                except OSError as e :
                    print(f"Error writing file: {e}")
                return
            elif(title>str):
                print("movie not found enter a correct movie name")
                return
            
    
    # Handle the error (e.g., notify user, try different location)

            
   


###########################################code for testing############################################

# pip install -r requirements.txt

# moviesTranscriptStartingChar('B')
# movieTranscript('EAMI (2022) - full transcript')
# movieTranscriptBetter('A 2nd Chance (2012)')
t=1
while(t):
    print("enter your choice")
    print("1) extract subscripts of all the movies")
    print("2) extract subscript of movies starting with charachter")
    print("3) extract subscript of specefic movie")
    print("4) exit")
    t=int(input(""))
    if(t==1):
        allMovieTranscript()
    if(t==2):
        char=char(input ("enter the charachter : "))
        moviesTranscriptStartingChar(char)
    if(t==3):
        str=input("enter the movie name : ")
        movieTranscriptBetter( str)
    if(t==4):
        break


    