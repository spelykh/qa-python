__author__ = 'Stepan_Pelykh'

import re


def num_sentences(filename):
    with open(filename, 'r') as f:
        s = f.read()
        sentences = len([item for item in s.split() if item.endswith('.')])
        print("Count of sentences = {}".format(sentences))

num_sentences('alice_in_wonderland.txt')

