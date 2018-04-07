import os
import re
import pymorphy2
from rumorph.ru import partsspeech

morph = pymorphy2.MorphAnalyzer()



parts_speech_list = ["NOUN", "ADJF", "ADJS", "COMP", "VERB", "INFN", "PRTF", "PRTS",
                     "GRND", "NUMR", "ADVB", "NPRO", "PRED", "PREP", "CONJ", "PRCL",
                     "INTJ"]
def len_filter(lst, length: int):
    """

    :param lst:
    :param length: не менее этой длины
    :return: list
    """
    return [x for x in lst if len(x) > length]

def normalize_words(lst):
    """
    убирает  не буквенные символы в спмске
    :param lst:
    :return: list
    """
    pattern = re.compile('[\d\W]+\Z|^[\d\W]+')
    return [re.sub(pattern, '', line) for line in lst]


def file_to_words(file):
    """
    получить список слов из файла
    :param file: path
    :return: дшые
    """
    with open(file, "r", encoding="utf-8") as f:
        return [x.strip() for x in f]

def words_to_file(file, lst):
    """
    сохранить список слов в файл

    :param file: str path
    :param lst: list
    """
    with open(file, "w", encoding="utf-8") as f:
        f.write('\n'.join(lst))

def dicts_to_files(dictionaries: partsspeech.PartsSpeechDict, directory, suffix=None):
    if suffix is None:
        suffix = ""
    else:
        suffix = "_" + suffix
    for p, w_list in dictionaries.items():
            path = os.path.join(directory, p + suffix + ".txt")
            words_to_file(path, w_list)



class PartsSpeech:
    def __init__(self):
        pass


def parts_speech(word: str) -> set:
    """

    :param word: str - word cyrillic
    :return: set - parts of speech which can be a word
    """
    return {x.tag.POS for x in morph.parse(word)}





def split_parts_speech(words_seq):
    dct = partsspeech.PartsSpeechDict()
    for w in words_seq:
        parts = parts_speech(w)
        dct.add_word(w, parts)
    return dct



if __name__ == '__main__':
    parts_speech_dir = "../resources/parts_speech"
    words = file_to_words("../resources/new.txt")
    norm = normalize_words(words)
    len_norm = len_filter(norm, 2)
    print(len_norm)


    # dct = split_parts_speech(words)
    # dicts_to_files(dct, parts_speech_dir, suffix="no_duplicate")
