import xml.etree.cElementTree as ET
from pprint import pprint

tree = ET.parse('newsafr.xml')
root = tree.getroot()

news_text_list = []
xml_news = root.findall('channel/item')
for top_news in xml_news:
    top_news = top_news.find('description').text.lower()
    news_text_list += top_news.split()

news_list = []
for word in news_text_list:
    if len (word) > 6:
        news_list.append (word)

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
