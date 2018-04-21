from screen import Screen
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from line import Line


class SemanticAnalyser(object):
    dict_class_with_used_func = dict()

    def __init__(self, tokenised_list):
        self.tokenised_list = tokenised_list
        self.classes_list = []
        self.objects_list = []

    def check_for_errors(self, available_class_list, available_func_with_classes):
        if self.check_for_brackets():
            if self.check_for_right_function_calling(available_class_list, available_func_with_classes):
                return True
            else:
                return False
        else:
            return False

    def check_for_brackets(self):
        diff = self.tokenised_list.count("(") - self.tokenised_list.count(")")

        if diff == 0:
            return True
        else:
            return False

    def check_for_right_function_calling(self, available_class_list, available_func_with_classes):

        for i in self.tokenised_list:
            if i in available_class_list:
                self.classes_list.append(i)

        for j in self.classes_list:
            class_index = self.tokenised_list.index(j)
            obj_index = class_index+1

            self.objects_list.append(self.tokenised_list[obj_index])

        result = 0
        for obj in self.objects_list:
            obj_index = self.objects_list.index(obj)

            class_obj = self.classes_list[obj_index]

            func_for_class_obj = available_func_with_classes[class_obj]

            for tokens in self.tokenised_list:
                if tokens.startswith(obj+"."):
                    if class_obj == 'screen':
                        result = self.for_screen(tokens, obj, func_for_class_obj, class_obj)
                    elif class_obj == 'circle':
                        result = self.for_circle(tokens, obj, func_for_class_obj, class_obj)

                    elif class_obj == 'rectangle':
                        result = self.for_rectangle(tokens, obj, func_for_class_obj, class_obj)

                    elif class_obj == 'triangle':
                        result = self.for_triangle(tokens, obj, func_for_class_obj, class_obj)

                    elif class_obj == 'line':
                        result = self.for_line(tokens, obj, func_for_class_obj, class_obj)

        if result == 1:
            return True
        else:
            return False

    def for_circle(self, tokens, obj, func_for_class_obj, class_obj):
        if tokens[len(obj) + 1:] in func_for_class_obj:

            self.dict_class_with_used_func[class_obj] = tokens[len(obj) + 1:]

            index = self.tokenised_list.index(tokens)

            r = self.tokenised_list[index + 2]
            Circle().set_radius(int(r))
            return 1
        else:
            return 0

    def for_screen(self, tokens, obj, func_for_class_obj, class_obj):
        if tokens[len(obj) + 1:] in func_for_class_obj:

            self.dict_class_with_used_func[class_obj] = tokens[len(obj) + 1:]

            index = self.tokenised_list.index(tokens)
            w = self.tokenised_list[index + 2]
            h = self.tokenised_list[index + 4]

            s = Screen()
            s.set_screen_dimen(w, h)
            return 1

        else:
            return 0

    def for_rectangle(self, tokens, obj, func_for_class_obj, class_obj):
        if tokens[len(obj) + 1:] in func_for_class_obj:

            self.dict_class_with_used_func[class_obj] = tokens[len(obj) + 1:]

            index = self.tokenised_list.index(tokens)
            x1 = self.tokenised_list[index + 2]
            y1 = self.tokenised_list[index + 4]
            x2 = self.tokenised_list[index + 6]
            y2 = self.tokenised_list[index + 8]

            rect = Rectangle()
            rect.set_rect_dimensions(x1, y1, x2, y2)
            return 1
        else:
            return 0

    def for_triangle(self, tokens, obj, func_for_class_obj, class_obj):
        if tokens[len(obj) + 1:] in func_for_class_obj:

            self.dict_class_with_used_func[class_obj] = tokens[len(obj) + 1:]

            index = self.tokenised_list.index(tokens)
            x1 = self.tokenised_list[index + 2]
            y1 = self.tokenised_list[index + 4]
            x2 = self.tokenised_list[index + 6]
            y2 = self.tokenised_list[index + 8]
            x3 = self.tokenised_list[index + 10]
            y3 = self.tokenised_list[index + 12]

            triangle = Triangle()
            triangle.set_triangle_dimensions(int(x1), int(y1), int(x2), int(y2), int(x3), int(y3))
            return 1
        else:
            return 0

    def for_line(self, tokens, obj, func_for_class_obj, class_obj):
        if tokens[len(obj) + 1:] in func_for_class_obj:

            self.dict_class_with_used_func[class_obj] = tokens[len(obj) + 1:]

            index = self.tokenised_list.index(tokens)
            x1 = self.tokenised_list[index + 2]
            y1 = self.tokenised_list[index + 4]
            x2 = self.tokenised_list[index + 6]
            y2 = self.tokenised_list[index + 8]

            line = Line()
            line.set_line_dimension(x1, y1, x2, y2)
            return 1
        else:
            return 0




