import re

frequent = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an', 'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot', 'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from', 'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however', 'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may', 'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on', 'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since', 'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this', 'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which', 'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']


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
    for k, v in sorted(words.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(k, v)


def get_text():
    user_file = input("Which file: ")
    in_file = open(user_file)
    text = in_file.read()
    return text


def main():
    top_20(word_frequency(get_text()))


if __name__ == '__main__':
    main()
