#!usr/bin/env/python3

# A mixin is a base class that encapsulates some common behavior with the goal of reusing code


class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


# tk = BaseTokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
# print(list(tk))


class UpperIterableMixin:
    def __iter__(self):
        return map(str.upper, super().__iter__())


class Tokenizer(UpperIterableMixin, BaseTokenizer):
    pass


tk = Tokenizer("28a2320b-fd3f-4627-9792-a2b38e3c46b0")
print(list(tk))



