from os.path import join as pjoin
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
    pattern = re.compile('[^\w]')
    return [re.sub(pattern, '', line).lower() for line in lst]


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
            path = pjoin(directory, p + suffix + ".txt")
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
    # dct = partsspeech.PartsSpeechDict()
    r = []
    for w in words_seq:
        parts = parts_speech(w)
        r.append((w, parts))
    return r
        # dct.add_word(w, parts)
    # return dct

def del_word_symbol(lst, pat):
    """
    убирает составные слова пишушиеся через тире
    :param lst:
    :param pat:
    :return: list
    """
    pattern = re.compile(pat)
    return [x for x in lst if re.search(pattern, x) is None]





if __name__ == '__main__':
    import pprint

    pat = re.compile("[.\s]+NOUN[.\s]+sing[.\s]+nomn")
    opcorpora = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora.txt"
    opcorpora_noun = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_noun.txt"
    opcorpora_nomn = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_nomn.txt"
    opcorpora_noname = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_noname.txt"
    opcorpora_Patr = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_Patr.txt"
    opcorpora_Surn = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_Surn.txt"
    opcorpora_Abbr = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_Abbr.txt"
    opcorpora_Orgn = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_Orgn.txt"
    opcorpora_Geox = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_Geox.txt"
    opcorpora_sing = r"D:\Serg\Dropbox\cube\dict.opcorpora.txt/dict.opcorpora_sing.txt"


    opcorpora_noun_words = r"D:\0SYNC\python_projects\cube_projects\libs\rumorph\rumorph\resources\NOUNS\corpora_noun.txt"
    noun_words = r"D:\0SYNC\python_projects\cube_projects\libs\rumorph\rumorph\resources\NOUNS\NOUN_no_duplicat.txt"
    diff_words = r"D:\0SYNC\python_projects\cube_projects\libs\rumorph\rumorph\resources\NOUNS\diff.txt"

    corpora_noun = file_to_words(opcorpora_noun_words)
    noun = file_to_words(noun_words)

    diff = set(noun) - set(corpora_noun)

    words_to_file(diff_words, diff)





    # lst = sorted(set(corpora_noun))
    # print(len(lst))
    # fl = pjoin(r"../resources/NOUNS", r"corpora_noun.txt")
    # words_to_file(fl, lst)
    # words_to_file(sorted(set(corpora_noun)), pjoin("../resources/NOUNS", "corpora_noun.txt"))
    # print(len(corpora_noun))
    # print(len(set(corpora_noun)))
    # noun = file_to_words(noun)

    # print(set(noun) - set(corpora_noun))



    # rlst = []
    # for line in file_to_words(opcorpora_sing):
    #     # фильтр
    #     # if not "Geox" in line:
    #     # if not "Geox" in line:
    #     # if "sing" in line:
    #     # if "ножны" in line.lower():
    #     w = line.split("\t")[0].lower()
    #     rlst.append(w)
    # res = file_to_words(opcorpora_noun_words)
    # print(pprint.pprint(res))
    # print(len(res))
    # куда
    # words_to_file(opcorpora_noun_words, rlst)

    # line = "ЁЖ	NOUN,anim,masc sing,nomn"

    # pat = re.compile("[.]*NOUN[,]anim")
    # print(re.search(pat, line))
    # print(line.split(","))

        # res = re.search(pat, line)
        # if res:
        #     print(line)
        #     print("---------------------------")






    # all_source_dict = r"D:\0SYNC\Serg\Dropbox\project\Cube\Dct"
    # parts_dir = "../resources/parts/no_dupl"
    # target_dicts = "../resources/target_dicts"
    # no_duplicate_letters_p = pjoin(target_dicts,"no_duplicate_letters.txt")
    # temp_dir = "../resources/temp"
    #
    #
    #
    # pro_ling_path = r"D:\Serg\project\pyomo\pyomo\resource\dictionaries\source\Про-Линг.txt"
    #
    # pro_ling_words = file_to_words(pro_ling_path)
    # # print(pro_ling_words[:50])
    #
    #
    # not_tire = del_word_symbol(pro_ling_words, "[-]")
    # not_point = del_word_symbol(not_tire, "[.]")
    # norm_words = normalize_words(not_point)
    # print(len(norm_words))
    # not_small_word = len_filter(norm_words, 2)
    # print(len(not_small_word))
    # #
    # # print(len(not_tire))
    # # print(len(not_small_word))
    # words_to_file(pjoin(temp_dir, "Про-Линг_norm.txt"), not_small_word)
    # pro_ling_path_all = r"D:\Serg\project\cube_projects\libs\rumorph\rumorph\resources\temp\Про-Линг_norm.txt"
    # dct = split_parts_speech(file_to_words(pro_ling_path_all))
    # print([x for x in dct if len(x[1]) > 1 and "NOUN" in x[1]])
    # dicts_to_files(dct, r"D:\Serg\project\cube_projects\libs\rumorph\rumorph\resources\parts\pro_ling", "pro_ling")


    # w_parts = split_parts_speech(file_to_words(no_duplicate_letters_p))
    # dicts_to_files(w_parts, parts_dir)
    # target_dicts = "../resources/target_dicts"
    # dal_p = pjoin(target_dicts, "dalf.txt")
    # no_duplicate_letters_p = pjoin(target_dicts,"no_duplicate_letters.txt")
    # dal =  set(file_to_words(dal_p))
    # no_duplicate_letters =  set(file_to_words(no_duplicate_letters_p))
    # r1 =  dal - no_duplicate_letters




    # words = file_to_words(pth)
    # norm_list = re_normalize_DALF(words)
    # words_to_file(os.path.join(target_dicts, "dalf.txt"), sorted(norm_list))
    # print(norm_list)
    # print(len(norm_list))


    # parts_speech_dir = "../resources/parts_speech"
    # words = file_to_words("../resources/new.txt")

    # len_norm = len_filter(norm, 2)
    # for w in words:
    #     if w and w[0].isupper():
    #         if w[0:10].find("-") > 0:
    #             print(w)
    #             print("--------------------------")


    # dct = split_parts_speech(words)
    # dicts_to_files(dct, parts_speech_dir, suffix="no_duplicate")
