import sys
from tokenizer import Tokenizer
from semantic_analyser import SemanticAnalyser


def initialize_list():
    return ['screen', 'circle', 'rectangle', 'triangle', 'square']


def check_semantic_analysis():

    semantic_analyser = SemanticAnalyser(tokenised_list)

    if semantic_analyser.check_for_errors(available_class_list, available_func_with_classes):
        return True
    else:
        return False


def initialize_dict_func():
    d = dict()
    d["screen"] = "make"
    d["circle"] = "draw"

    return d


if __name__ == '__main__':
    file_name = sys.argv[1]

    available_class_list = initialize_list()

    available_func_with_classes = initialize_dict_func()

    print available_func_with_classes

    tokenised_list = Tokenizer().tokenise(file_name)

    if check_semantic_analysis():
        pass
    else:
        print "Semantic Error Raised"

    print tokenised_list

