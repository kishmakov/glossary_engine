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


def build_index(descriptions, lang):
    authors = {}
    for description in descriptions:
        author_id = description['id'].replace(' ', '_')
        texts = []
        for text_id, text_desc in description['texts'].items():
            if lang in text_desc:
                texts.append({'id': text_id.replace(' ', '_'), 'name': text_desc[lang]['name']})

        authors[author_id] = {'name': description['author'][lang], 'texts': texts}

    with open('index_{0}.py'.format(lang), 'w') as index_file:
        index_file.write('authors = [\n')
        for id, desc in sorted(authors.items()):
            index_file.write('    {{"id": "{0}", "name": "{1}"}},\n'.format(id, desc['name']))
        index_file.write(']\n')

        index_file.write('author =  {\n')
        for id, desc in sorted(authors.items()):
            index_file.write('    "{0}": {{\n'.format(id))
            index_file.write('        "name": "{0}",\n'.format(desc['name']))
            index_file.write('        "texts": [\n'.format(desc['name']))
            for text in desc['texts']:
                index_file.write('            {{"id": "{0}", "name": "{1}"}},\n'.format(text['id'], text['name']))
            index_file.write('        ],\n')
            index_file.write('    },\n')
        index_file.write('}\n')

        index_file.write('index =  {\n')
        index_file.write('    "authors": authors,\n')
        index_file.write('    "author": author,\n')
        index_file.write('}\n')


if __name__ == '__main__':
   descriptions = get_descriptions()
   for lang in INTERFACE_LANGS:
       build_index(descriptions, lang)






