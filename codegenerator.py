from semantic_analyser import SemanticAnalyser
from initialiser import Initializer
from circle import Circle

class CodeGenerator(object):
    user_class_list = []

    def __init__(self):
        pass

    def check_for_shapes(self):
        for shapes in CodeGenerator.user_class_list:
            if shapes == 'circle':
                self.use_circle()


    def check_screen(self, tokenised_list):

        semantic_analyzer = SemanticAnalyser(tokenised_list)

        dict_class_with_used_func = semantic_analyzer.dict_class_with_used_func

        CodeGenerator.user_class_list = dict_class_with_used_func.keys()

        available_class_list = Initializer().initialize_class_list()

        if available_class_list[0] in CodeGenerator.user_class_list:
            CodeGenerator.user_class_list.remove(available_class_list[0])
            return True
        else:
            return False

    def use_circle(self):
        circle = Circle()
        circle.draw()





