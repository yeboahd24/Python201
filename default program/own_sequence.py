#!usr/bin/env/python3
# Creating your own sequence


class Items(object):
    def __init__(self, *values):
        self.__values = list(values)  # Encapsulation

    def __len__(self):
        return len(self.__values)

    def __getitem__(self, item):
        return self.__values.__getitem__(item)


item = Items(1, 2, 3, 4, 5)
# print(len(item))
print(item[0])

# When indexing by a range, the result should be an instance of the same type of
# the class
