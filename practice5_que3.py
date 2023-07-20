# 3. Write an iterator class reverse_iter, that takes a list and iterates it from the reverse direction

class reverse_iter:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = len(data_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index  = self.index - 1
        return self.data_list[self.index]


my_list = [10, 20, 30, 40, 50]

reverse_iterator = reverse_iter(my_list)

for item in reverse_iterator:
    print(item)