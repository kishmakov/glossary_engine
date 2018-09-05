#!/usr/bin/env python3

import json
import os
import string

INTERFACE_LANGS = ['el', 'en', 'ru']


def get_descriptions():
    descriptions = []
    for letter in string.ascii_uppercase:
        absolute_path = os.path.abspath('gt/' + letter)

        if not os.path.isdir(absolute_path):
            continue

        for name in os.listdir(absolute_path):
            about = absolute_path + '/' + name + '/about.json'

            if os.path.isfile(about):
                with open(about) as input:
                    descriptions.append(json.load(input))

    return descriptions


def parse_author(desc, lang):
    if lang not in desc:
        return None

    return desc[lang]


def parse_text(desc, lang):
    name = desc[lang]['name']
    parts = {}
    if 'parts' in desc[lang]:
        for number, id in desc[lang]['parts'].items():
            parts[number] = id

    return {'name': name, 'parts': parts}


def parse_texts(desc, lang):
    texts = []
    for text_id, text_desc in desc.items():
        if lang not in text_desc:
            continue

        text = parse_text(text_desc, lang)
        text['id'] = text_id.replace(' ', '_')
        texts.append(text)

    return texts


INDENT_STEP = 2


class PyBuilder:
    def __init__(self, name):
        self.indent = 0
        self.str = '{0} ='.format(name)

    def op(self, br='{'):
        indent = self.indent if self.str[-1] == '\n' else 1
        self.str += ' ' * indent + br + '\n'
        self.indent += INDENT_STEP
        return self

    def cl(self, br='}'):
        self.indent -= INDENT_STEP
        self.str += ' ' * self.indent + br + '\n'
        return self

    def key(self, key):
        self.str += ' ' * self.indent + '"{0}"'.format(key) + ':'
        return self

    def val(self, value):
        self.str += ' {0},\n'.format(value)
        return self

    def vals(self, value):
        self.str += ' "{0}",\n'.format(value)
        return self


def build_index(descriptions, lang):
    authors = {}
    for description in descriptions:
        author_id = description['id'].replace(' ', '_')
        texts = parse_texts(description['texts'], lang)
        author = parse_author(description['about'], lang)
        if author:
            authors[author_id] = {'name': author['name'], 'texts': texts}

    authors_builder = PyBuilder('authors')
    authors_builder.op('[')
    for id, desc in sorted(authors.items()):
        authors_builder.op('{').key('id').vals(id).key('name').vals(desc['name']).cl('}')
    authors_builder.cl(']')

    author_builder = PyBuilder('author')
    author_builder.op('{')
    for id, desc in sorted(authors.items()):
        author_builder.key(id).op('{')
        author_builder.key('name').vals(desc['name'])
        author_builder.key('texts').op('[')
        for text in desc['texts']:
            author_builder.op('{')
            author_builder.key('id').vals(text['id']).key('name').vals(text['name'])
            author_builder.key('parts').op('{')
            for part_num, part_id in text['parts'].items():
                author_builder.key(part_num).vals(part_id)
            author_builder.cl('}')
            author_builder.cl('}')
        author_builder.cl(']')
        author_builder.cl('}')
    author_builder.cl('}')

    index_builder = PyBuilder('index')
    index_builder.op('{')
    index_builder.key('authors').val('authors')
    index_builder.key('author').val('author')
    index_builder.cl('}')

    with open('index_{0}.py'.format(lang), 'w') as index_file:
        index_file.write(authors_builder.str)
        index_file.write(author_builder.str)
        index_file.write(index_builder.str)


if __name__ == '__main__':
   descriptions = get_descriptions()
   for lang in INTERFACE_LANGS:
       build_index(descriptions, lang)






