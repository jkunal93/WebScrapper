import requests
from bs4 import BeautifulSoup
import pprint

def scrape_stories(page_number=1):
    url = 'https://news.ycombinator.com/news'
    if page_number > 1:
        url = url + '?p='+ str(page_number)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    links = soup.select('.titleline')
    subtext = soup.select('.subtext')
    return create_custom_hn(links, subtext)

def sort_stories_by_scores(news):
    return sorted(news, key= lambda k: k['score'], reverse=True)

def create_custom_hn(links, subtext):
    hn =[]
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].find('a')['href']
        scores = subtext[idx].select('.score')
        if len(scores):
            score = int(scores[0].getText().replace(' points', ''))
            hn.append({'title': title, 'score': score, 'link': href})
    return sort_stories_by_scores(hn)

pprint.pprint(scrape_stories(1), sort_dicts=False)