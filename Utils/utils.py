class Human:
    name: str
    age: int
    def __init__(self, name = 'Igor'):
        self.name = name
        self.age = 20
    def say_hello(self):
        print('Hello world!')