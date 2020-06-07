import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#tr:nth-child(2) > td.number
#tr:nth-child(3) > td.info > a.title.ellipsis
#tr:nth-child(4) > td.info > a.artist.ellipsis

#이전코드
#for song in songs:
    #a_tag = song.select_one('td > a.title.ellipsis')
    #if a_tag is not None:
        #number = song.select_one('td.number').text[0].strip()
        #title = a_tag.text.strip()
        #people = song.select_one('td.info > a.artist.ellipsis').text.strip()
        #print (number, title, people)


#수정 코드
#decompose()
for song in songs:
    a_tag = song.select_one('td > a.title.ellipsis')
    if a_tag is not None:
        td_tag = song.select_one('td.number')
        td_tag.span.decompose()
        #td_tag의 span태그를 제거해라

        number = td_tag.text.strip()
        title = a_tag.text.strip()
        people = song.select_one('td.info > a.artist.ellipsis').text.strip()

        print (number, title, people)