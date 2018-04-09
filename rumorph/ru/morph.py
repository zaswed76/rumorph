import pymorphy2
import pprint

opcorpora = r"D:\Serg\programm\python3\Lib\site-packages\pymorphy2_dicts\data"
morph = pymorphy2.opencorpora_dict.wrapper.Dictionary(opcorpora)
f = morph.iter_known_words(prefix=u'')
r = []
for p in f:
    tag = p[1]
    if {"NOUN", "nomn", "sing"} in tag:
        print(p[2])

pprint.pprint(r)

