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
    parts = []
    if 'parts' in desc[lang]:
        for part in desc[lang]['parts']:
            parts.append(part)

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

    def key_vals(self, dictionary, keys):
        for key in keys:
            self.key(key).vals(dictionary[key])
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
        authors_builder.op('{').key('id').vals(id).key('name').vals(desc['name']).cl('},')
    authors_builder.cl(']')

    texts_builder = PyBuilder('texts')
    texts_builder.op('{')
    for id, desc in sorted(authors.items()):
        texts_builder.key(id).op('[')
        for text in desc['texts']:
            texts_builder.op('{')
            texts_builder.key('id').vals(text['id']).key('name').vals(text['name'])
            texts_builder.key('parts').op('[')
            for part in text['parts']:
                texts_builder.op('{')
                texts_builder.key_vals(part, ['id', 'name', 'number'])
                texts_builder.cl('}')
            texts_builder.cl(']')
            texts_builder.cl('}')
        texts_builder.cl('],')
    texts_builder.cl('}')

    index_builder = PyBuilder('index')
    index_builder.op('{')
    index_builder.key('authors').val('authors')
    index_builder.key('texts').val('texts')
    index_builder.cl('}')

    with open('index_{0}.py'.format(lang), 'w') as index_file:
        index_file.write(authors_builder.str)
        index_file.write(texts_builder.str)
        index_file.write(index_builder.str)


if __name__ == '__main__':
   descriptions = get_descriptions()
   for lang in INTERFACE_LANGS:
       build_index(descriptions, lang)






