import json
from pprint import pprint
with open('newsafr.json', encoding='utf-8') as f:
    word_list_pop = []
    pop = {}
    json_data = json.load(f)
    rss_ = json_data['rss']
    channel_ = rss_['channel']
    items_ = channel_['items']
    for list_ in items_:
        description_ = list_['description']
        description_list = description_.split(' ')
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
