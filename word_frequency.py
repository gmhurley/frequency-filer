import re


def word_frequency(text):
    words = {}
    for word in text.split():
        word = re.sub(r'[^A-Za-z]', '', word).lower()
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
