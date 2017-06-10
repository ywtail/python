# coding:utf-8
import requests
from bs4 import BeautifulSoup


def query_baidu_baike(word):
    url = BAIDU_URL.format(word)
    r = requests.get(url)
    result = r.content
    summary = parse_html(word, result)
    return summary, url


def parse_html(word, content):
    soup = BeautifulSoup(content, 'html.parser')
    try:
        summary_node = soup.find('div', class_='lemma-summary')
        summary = summary_node.get_text()
        return summary
    except:
        others.append(word)


if __name__ == '__main__':
    BAIDU_URL = 'http://baike.baidu.com/item/{0}'
    input_filename = input('待查询词汇所在文件名：')

    words = open(input_filename).read().split()
    print('文件中的词汇数： ', len(words))
    others = []

    mydict_file = open('searched.txt', 'w')
    others_file = open('tosearch.txt', 'w')

    for word in words:
        summary, url = query_baidu_baike(word)
        print(word, summary)
        if summary:
            mydict_file.write(word)
            mydict_file.write(summary)
            s = '更多解释参见： ' + url
            mydict_file.write(s + '\n\n')

    for w in others:
        others_file.write(w + '\n')

    print('一共 {} 个词，未查询到 {} 个词'.format(len(words), len(others)))
    print('Done!')