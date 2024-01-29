import requests
from bs4 import BeautifulSoup


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
my_url = 'https://www.imdb.com/list/ls000634294/?sort=num_votes,desc&st_dt=&mode=detail&page=4'

response = requests.get(my_url, headers=headers)
page_html = response.text
page_soup = BeautifulSoup(page_html,"html.parser")


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
my_url = 'https://www.imdb.com/list/ls000634294/?sort=num_votes,desc&st_dt=&mode=detail&page=7'

response = requests.get(my_url, headers=headers)
page_html = response.text
page_soup = BeautifulSoup(page_html,"html.parser")

movies = page_soup.findAll('div', attrs={"class":"lister-item-content"})
movies_list = []

for movie in movies:
  movies_list.append(movie.h3.a.text)

runtime = page_soup.findAll('span', attrs={"class":"runtime"})
runtime_list = []

for rt in runtime:
  runtime_list.append(rt.text.strip('min'))
runtime_list = [int(i) for i in runtime_list]
res = dict(zip(movies_list, runtime_list))

mx = max(runtime_list)

for key in res:
  if res[key] == mx:
    print(f'{key} {res[key]}')