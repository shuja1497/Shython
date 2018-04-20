from screen import Screen
from circle import Circle


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
            print self.objects_list

            obj_index = self.objects_list.index(obj)

            class_obj = self.classes_list[obj_index]

            func_for_class_obj = available_func_with_classes[class_obj]

            for tokens in self.tokenised_list:
                if tokens.startswith(obj+"."):
                    if obj == 's':
                        result = self.for_screen(tokens, obj, func_for_class_obj, class_obj)
                    elif obj == 'c':
                        result = self.for_circle(tokens, obj, func_for_class_obj, class_obj)

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
            print index

            w = self.tokenised_list[index + 2]
            h = self.tokenised_list[index + 4]

            s = Screen()
            s.set_screen_dimen(w, h)
            return 1

        else:
            return 0




