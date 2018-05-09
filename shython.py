import sys
from tokenizer import Tokenizer
from semantic_analyser import SemanticAnalyser
from screen import Screen
from initialiser import Initializer
from codegenerator import CodeGenerator
from Tkinter import *


def check_semantic_analysis():
    print "tokenised list for semantic checking ", tokenised_list
    semantic_analyser = SemanticAnalyser(tokenised_list)

    if semantic_analyser.check_for_errors(available_class_list, available_func_with_classes):
        return True
    else:
        return False


def use_screen():
    s = Screen()
    width, height = s.get_screen_dimen()
    s.make(master=master)


if __name__ == '__main__':
    master = Tk()

    file_name = sys.argv[1]

    initializer = Initializer()
    available_class_list = initializer.initialize_class_list()
    print "Available class list : ", available_class_list

    available_func_with_classes = initializer.initialize_dict_func()
    print "Avaialable func with classes : ", available_func_with_classes

    tokenised_list = Tokenizer().tokenise(file_name)
    # print tokenised_list

    if check_semantic_analysis():
        print "No Semantic Error"
        print "code generation started"
        codegenerator = CodeGenerator()
        if codegenerator.check_screen(tokenised_list):
            print "screen initialised"
            use_screen()
            codegenerator.check_for_shapes()
            mainloop()
        else:
            print "Screen not initialized"

    else:
          print "Semantic Error Raised"






