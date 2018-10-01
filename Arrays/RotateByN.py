class Rotate:
    def __init__(self, input_list, rotate_by):
        self.input_list = input_list
        self.rotate_by = rotate_by

    def get_list_length(self):
        return len(self.input_list)

    def rotateFunction(self):
        length_of_list = self.get_list_length()
        if self.rotate_by == 0:
            return
        for element_index in range(self.rotate_by):
            temp = self.input_list[0]
            for index in range(length_of_list - 1):
                self.input_list[index] = self.input_list[index + 1]
            self.input_list[length_of_list - 1] = temp

    def print_list(self):
        print self.input_list

test_list = [1,2,3,4,5]
rotate_by = 2
test = Rotate(test_list, rotate_by)
test.print_list()
test.rotateFunction()
test.print_list()
