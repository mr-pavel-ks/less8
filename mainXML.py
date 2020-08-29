import  xml.etree.ElementTree as ET
from pprint import pprint
parser  = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)
root = tree.getroot()
news_list = root.findall('channel/item')
word_list_pop = []
pop = {}
for i, news in enumerate(news_list):
    description = news.find('description').text
    # print(description)
    description_list = description.split(' ')
    for word in description_list:
        word_list = []
        if len(word) > 6:
            word_list.append(word)
        for word_6s in word_list:
            word_list_pop.append(word_6s)
word_list_pop.sort()
for i in range(0, len(word_list_pop) - 1):
    if word_list_pop[i] == word_list_pop[i + 1]:
        count = word_list_pop.count(word_list_pop[i])
        pop[word_list_pop[i]] = count - 1
sorted_by_value = sorted(pop.items(), key=lambda kv: kv[1])[-10::]
pprint(sorted_by_value)