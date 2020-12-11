import json
from pprint import pprint

class my_range():
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cursor = self.start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.end:
            raise StopIteration
        with open('countries.json', encoding='utf8') as file:
            text = json.load(file)
            return text[self.cursor]['name']['common']

if __name__ == '__main__':
    with open('countries.json', encoding='utf8') as file:
        text = json.load(file)
    my_range = my_range(1, len(text))
    with open('result.txt', 'a', encoding='utf8') as result_file:
        for item in my_range:
            result_file.write(f'{item}: https://en.wikipedia.org/wiki/{item} \n')