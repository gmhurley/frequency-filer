# http://stackoverflow.com/questions/10079216/skip-first-entry-in-for-loop-in-python

import re

from tabulate import tabulate

frequent = ['', 'a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']


def word_frequency(text):
    words = {}
    for word in text.split():
        word = re.sub(r'[^A-Za-z]', '', word).lower()
        if word in frequent:
            continue
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def top_20(words):
    top_list = sorted(words.items(), key=lambda x: x[1], reverse=True)[:20]
    # http://stackoverflow.com/questions/14831830/convert-a-list-of-tuples-to-a-list-of-lists
    top_list = [list(elem) for elem in top_list]
    top_div = top_list[0][1]//50
    top_list[0][1] = '#' * 50
    for word in top_list[1:]:
        word[1] = '#' * ((word[1] - 50)//top_div)
    print(tabulate(top_list))


def get_text():
    user_file = input("Which file: ")
    in_file = open(user_file)
    text = in_file.read()
    return text


def main():
    top_20(word_frequency(get_text()))


if __name__ == '__main__':
    main()
