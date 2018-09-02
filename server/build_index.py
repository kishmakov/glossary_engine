#!/usr/bin/env python3

import json
import os
import subprocess
import sys
import string

INTERFACE_LANGS = ['el', 'en', 'ru']


# def collect_lines(fn):
#     lines = set()
#
#     for user in os.listdir(HOME):
#         homedir = HOME + '/' + user
#         if not os.path.isdir(homedir):
#             continue
#
#         bashrc = homedir + '/.bash_history'
#         if not os.path.isfile(bashrc):
#             continue
#
#         with open(bashrc) as f:
#             for line in f.read().splitlines():
#                 lines.add(line)
#
#     with open(output, 'w') as dst:
#         for line in sorted(list(lines)):
#             dst.write(line + '\n')

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
        author_name = description['author'][lang]
        authors[author_id] = author_name

    index = {'authors': authors}
    with open('index_{0}.json'.format(lang), 'w') as index_file:
        index_file.write(json.dumps(index, indent=4, sort_keys=True))


if __name__ == '__main__':
   descriptions = get_descriptions()
   for lang in INTERFACE_LANGS:
       build_index(descriptions, lang)






