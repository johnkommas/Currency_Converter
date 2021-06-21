class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def convert_height(self):
        return self.height / 0.3048


everest = Mountain('Everest', 8848)
anconcagua = Mountain('Aconcagua', 6960.8)
print(f'{everest.convert_height()} {anconcagua.convert_height()}')
