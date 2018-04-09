
from collections import MutableMapping

class PartsSpeechDict(MutableMapping):


    def __init__(self):
        self._data = {}

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value


    def __delitem__(self, key):
        del self._data[key]


    def add_word(self, word, part_speech):
        for ps in part_speech:
            seq = self._data.get(ps, [])
            seq.append(word)
            # self._data[str(ps)] = seq






if __name__ == '__main__':
    pspeech = PartsSpeechDict()
    pspeech.add_word('word', {"NOUN", "VERB"})
    pspeech.add_word('cat', {"NOUN"})
    pspeech.add_word('dog', {"NOUN", "VERB"})
    print(list(pspeech["NOUN"]))