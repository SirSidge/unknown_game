import ast

class Dictionary():
    def __init(self):
        self.dictionary = {}

    def fetch_dictionary(self):
        with open("assets/converted_dictionary.txt", "r") as file:
            content = file.read()
            self.dictionary = ast.literal_eval(content)

    def show_dict(self):
        print(self.dictionary["Happy"])