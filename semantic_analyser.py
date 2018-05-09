from screen import Screen
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from line import Line
from square import Square
from polygon import Polygon


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
                if i not in self.classes_list:
                    self.classes_list.append(i)
        # print "class list of user : ", self.classes_list

        for j in self.classes_list:
            class_index = self.tokenised_list.index(j)
            obj_index = class_index+1
            # print obj_index
            if self.tokenised_list[obj_index] in self.classes_list:
                return False
            self.objects_list.append(self.tokenised_list[obj_index])

        print self.objects_list
        for objects_used_by_user in self.objects_list:
            if self.objects_list.count(objects_used_by_user) > 1:
                # print "*******"
                return False

        # print "object used by the user :", self.objects_list

        result = 0
        for obj in self.objects_list:
            obj_index = self.objects_list.index(obj)

            class_obj = self.classes_list[obj_index]

            func_for_class_obj = available_func_with_classes[class_obj]
            # print "func for ", class_obj, "is :", func_for_class_obj

            for tokens in self.tokenised_list:
                if tokens.startswith(obj+"."):
                    if class_obj == 'screen':
                        result = self.for_screen(tokens, obj, func_for_class_obj, class_obj)
                        if result == 0:
                            print "Error in initialising screen"
                            return False

                    elif class_obj == 'circle':
                        result = self.for_circle(tokens, obj, func_for_class_obj, class_obj)
                        if result == 0:
                            print "Error in initialising circle"
                            return False

                    elif class_obj == 'rectangle':
                        result = self.for_rectangle(tokens, obj, func_for_class_obj, class_obj)
                        if result == 0:
                            print "Error in initialising rectangle"
                            return False

                    elif class_obj == 'triangle':
                        result = self.for_triangle(tokens, obj, func_for_class_obj, class_obj)
                        if result == 0:
                            print "Error in initialising triangle"
                            return False

                    elif class_obj == 'line':
                        result = self.for_line(tokens, obj, func_for_class_obj, class_obj)
                        if result == 0:
                            print "Error in initialising line"
                            return False

                    elif class_obj == 'square':
                        result = self.for_square(tokens, obj, func_for_class_obj, class_obj)
                        if result == 0:
                            print "Error in initialising square"
                            return False

                    elif class_obj == 'polygon':
                        result = self.for_polygon(tokens, obj, func_for_class_obj, class_obj)
                        if result == 0:
                            print "Error in initialising polygon"
                            return False
        #
        # if result == 1:
        #     return True
        # else:
        #     return False
        return True

    def for_circle(self, tokens, obj, func_for_class_obj, class_obj):
        if tokens[len(obj) + 1:] in func_for_class_obj:

            self.dict_class_with_used_func[class_obj] = tokens[len(obj) + 1:]

            index = self.tokenised_list.index(tokens)

            r = self.tokenised_list[index + 2]

            if index + 4 < len(self.tokenised_list):
                if self.tokenised_list[index+4] == '#':
                    fill_color = self.tokenised_list[index+5]
                    Circle().set_fill_color('#' + fill_color)

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

            if index + 10 < len(self.tokenised_list):
                if self.tokenised_list[index+10] == '#':
                    fill_color = self.tokenised_list[index+11]
                    Rectangle().set_fill_color('#' + fill_color)

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

            if index + 14 < len(self.tokenised_list):
                if self.tokenised_list[index + 14] == '#':
                    fill_color = self.tokenised_list[index + 15]
                    Triangle().set_fill_color('#' + fill_color)

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

    def for_square(self, tokens, obj, func_for_class_obj, class_obj):
        if tokens[len(obj) + 1:] in func_for_class_obj:

            self.dict_class_with_used_func[class_obj] = tokens[len(obj) + 1:]

            index = self.tokenised_list.index(tokens)

            side = self.tokenised_list[index + 2]

            if index+4 < len(self.tokenised_list):
                if self.tokenised_list[index + 4] == '#':
                    fill_color = self.tokenised_list[index + 5]
                    Square().set_fill_color('#' + fill_color)

            Square().set_side_length(int(side))

            return 1
        else:
            return 0

    def for_polygon(self, tokens, obj, func_for_class_obj, class_obj):
        if tokens[len(obj) + 1:] in func_for_class_obj:
            self.dict_class_with_used_func[class_obj] = tokens[len(obj) + 1:]
            # print "//////////////", tokens
            index = self.tokenised_list.index(tokens)
            co_ordinate_list = []
            for i in range(index+1, len(self.tokenised_list), 2):
                # print "-------", i
                if self.tokenised_list[i] != ")" or self.tokenised_list[i] != "#":
                    if self.tokenised_list[i+1] != "#":
                        co_ordinate_list.append(self.tokenised_list[i+1])
                    else:
                        break
                else:
                    break
            fill_color = self.tokenised_list[i+2]
            Polygon().set_fill_color('#' + fill_color)

            # print co_ordinate_list
            Polygon().set_points(co_ordinate_list)


