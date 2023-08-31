class MySet:
    def __init__(self, initial_values=[]):
        self.dictionary = {}
        for value in initial_values:
            self.dictionary[value] = True

    def add(self, value):
        self.dictionary[value] = True

    def delete(self, value):
        if value in self.dictionary:
            del self.dictionary[value]

    def has(self, value):
        return value in self.dictionary

    def size(self):
        return len(self.dictionary)

# Uncomment these bonus methods if you'd like to implement them
#     def clear(self):
#         self.dictionary = {}
# 
#     def __str__(self):
#         elements = ", ".join(str(key) for key in self.dictionary.keys())
#         return f"MySet: {{{elements}}}"
