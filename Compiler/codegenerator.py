from Shapes.line import Line
from Shapes.polygon import Polygon
from Shapes.rectangle import Rectangle
from Shapes.square import Square
from Shapes.triangle import Triangle
from Initializer.initialiser import Initializer
from Shapes.circle import Circle
from Compiler.semantic_analyser import SemanticAnalyser


class CodeGenerator(object):
    user_class_list = []

    def __init__(self):
        pass

    def check_for_shapes(self):
        for shapes in CodeGenerator.user_class_list:
            if shapes == 'circle':
                self.use_circle()
            if shapes == 'rectangle':
                self.use_rectangle()
            if shapes == 'triangle':
                self.use_triangle()
            if shapes == 'line':
                self.use_line()
            if shapes == 'square':
                self.use_square()
            if shapes == 'polygon':
                self.use_polygon()

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
        Circle().draw()

    def use_rectangle(self):
        Rectangle().draw()

    def use_triangle(self):
        Triangle().draw()

    def use_line(self):
        Line().draw()

    def use_square(self):
        Square().draw()

    def use_polygon(self):
        Polygon().draw()






