import re


def re_normalize_DALF(text):
    """
    создаёт из словаря даля список слов
    :param text: list
    :return: list
    """
    res = set()
    pat = re.compile(r"(\b[А-ЯЁ]+\b)([\s])")
    for w in text:
        if w and w[0].isupper():
            match = re.match(pat, w)
            if match:
                res.add(match.group(1).lower())
    return res
