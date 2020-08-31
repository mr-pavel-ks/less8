import json
from pprint import pprint
with open('newsafr.json', encoding='utf-8') as f:
    word_list_pop = []
    pop = {}
    json_data = json.load(f)
    items = json_data['rss']['channel']['items']
    for list_ in items:
        description = list_['description']
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
            pop[word_list_pop[i]] = count
    sorted_by_value = sorted(pop.items(), key=lambda kv: kv[1], reverse=True)[:10]
    pprint(sorted_by_value)
