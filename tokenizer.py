import nltk


class Tokenizer(object):

    def tokenise(self, word=""):
        my_file = open(word, "r")
        code = my_file.read()
        return nltk.word_tokenize(code)

