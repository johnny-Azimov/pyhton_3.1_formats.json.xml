import json
from pprint import pprint

with open('newsafr.json', encoding='utf-8') as news:
    json_news = json.load(news)
    news_list = []
    for top_news in json_news['rss']['channel']['items']:
        top_news = top_news['description'].lower()
        for word in top_news.split():
            if len(word) > 6:
                news_list.append(word)
    top_word = {}
    for afr_news in news_list:
        top_list_word = {afr_news:news_list.count(afr_news)}
        top_word.update(top_list_word)

    list_word = list(top_word.items())
    list_word.sort(key=lambda afr_news:afr_news[1])
    list_word = list_word[-10:]
    print('\nТоп 10 самых часто встречающихся в новостях слов длиннее 6 символов:\n')
    list_word.reverse()

    for afr_news in range(10):
        print(list_word[afr_news])