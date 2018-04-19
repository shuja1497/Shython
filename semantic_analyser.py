class SemanticAnalyser(object):

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

        # initialize list in a diff func
        for i in self.tokenised_list:
            if i in available_class_list:
                self.classes_list.append(i)

        for j in self.classes_list:
            class_index = self.tokenised_list.index(j)
            obj_index = class_index+1

            self.objects_list.append(self.tokenised_list[obj_index])

        print self.classes_list
        print self.objects_list

        result = 0
        for obj in self.objects_list:
            obj_index = self.objects_list.index(obj)

            class_obj = self.classes_list[obj_index]

            func_for_class_obj = available_func_with_classes[class_obj]

            for tokens in self.tokenised_list:
                if tokens.startswith(obj+"."):
                    if tokens[len(obj)+1:] in func_for_class_obj:
                        result = 1
                        print "success"
                    else:
                        result = 0
                        print "failure"

        if result == 1:
            return True
        else:
            return False


