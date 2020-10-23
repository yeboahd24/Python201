#!usr/bin/env/python3
class DynamicAttributes(object):
    def __init__(self, attribute):
        self.attribute = attribute

    def __getattr__(self, item):
        if item.startswith('fallback_'):
            name = item.replace('fallback_', '')
            return f'[fallback resolved] {name}'
        raise AttributeError(f'{self.__class__.__name__} has no attribute {item}')


dyn = DynamicAttributes('value')
# print(dyn.fallback_test) # [fallback resolved] test
print(dyn.attribute)  # value
dyn.new_attribute = "linux"  # setting new attribute called new_attribute
print(dyn.new_attribute)
# print(dyn.item)  # error
