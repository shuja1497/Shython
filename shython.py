import sys
from tokenizer import Tokenizer
from semantic_analyser import SemanticAnalyser
from screen import Screen
from Tkinter import *


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
    d["circle"] = ["draw", "show"]

    return d


def use_screen():
    s = Screen()
    width, height = s.get_screen_dimen()
    s.make(master=master)
    print width, height

    mainloop()


if __name__ == '__main__':
    master = Tk()

    file_name = sys.argv[1]

    available_class_list = initialize_list()

    available_func_with_classes = initialize_dict_func()

    # print available_func_with_classes

    tokenised_list = Tokenizer().tokenise(file_name)

    if check_semantic_analysis():
        pass
    else:
        print "Semantic Error Raised"

    print tokenised_list

    semantic_analyzer = SemanticAnalyser(tokenised_list)

    dict_class_with_used_func = semantic_analyzer.dict_class_with_used_func

    user_class_list = dict_class_with_used_func.keys()
    print user_class_list
    user_func_list = dict_class_with_used_func.values()

    if available_class_list[0] in user_class_list:
        use_screen()

    else:
        print "Screen not initialized"






