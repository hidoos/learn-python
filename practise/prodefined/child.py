class Parent():
    def __init__(self, first_name, eye_colors):
        self.first_name = first_name
        self.eye_colors = eye_colors

class Child(Parent):
    def __init__(self):
        self.__super__().__init__()


