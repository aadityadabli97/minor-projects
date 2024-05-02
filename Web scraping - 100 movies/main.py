from bs4 import BeautifulSoup
import requests

web_data=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best"
                      "-movies-2/")
text_data=web_data.text

parsed_data=BeautifulSoup(text_data,"html.parser")
#print(parsed_data.title)
#print(parsed_data.prettify())
#movie_titles=parsed_data.find(name="h3",class_="title")
movie_titles=parsed_data.find_all(name="h3",class_="title")
#print(movie_titles)
movie_titles_list=[]
for i in movie_titles:
    c=i.getText()
    movie_titles_list.append(c)

movie_list_sorted=movie_titles_list[-1::-1]

with open("movies.txt","w+",encoding="utf-8") as movie_file:
    for i in movie_list_sorted:
        movie_file.write(i + "\n")


