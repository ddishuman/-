## Part 1

###### Counting #######
import os
def top3(URLS):
    dict = {}
    for line in URLS:
        filename = os.path.basename(line)
        if filename in dict:
            dict[filename] +=1
        else:
            dict[filename] = 1
              
    sorted_dict = sorted(dict, key=dict.get, reverse=True)
    for k in sorted_dict[:3]:
        print(k, dict[k])   

urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]

top3(urls)


###### Integration #######
def anonymous(x):
    return x**2 + 1
def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        ''' your work here '''
        area += (step *anonymous(intercept))
    
    return area

print(integrate(anonymous, 0, 10))


###### Multiples of 3 and 5. #######
def sumBelowX(x):
    mul_3 = [i for i in range(1, x) if i%3==0]
    mul_5 = [j for j in range(1, x) if j%5==0 and j%15!=0]
    return sum(mul_3 + mul_5)

print(sumBelowX(100))


## Part 2

###### a) #######
import requests
from requests_html import HTML

def fetch(board_name):
    url = 'https://www.ptt.cc/bbs/' + board_name + '/index.html'
    response = requests.get(url)
    #response = requests.get(url, cookies ={'over18': '1'})
    return response

def parse_article(doc):
    html = HTML(html=doc)
    post_entries = html.find('div.r-ent')
    return post_entries

def parse_article_meta(entry, board_name):
    return {
            'date' : entry.find('div.date', first=True).text,
            'author' : entry.find('div.author', first=True).text,
            'title' : entry.find('div.title', first=True).text,
            #'article' : entry.find('div.article', first=True).text,  #不確定
            'board' : board_name
            }

board_name = 'Tennis'
resp = fetch(board_name)
#print(resp.text)
post_entries = parse_article(resp.text)


for entry in post_entries:
    meta = parse_article_meta(entry, board_name)
    print(meta)




