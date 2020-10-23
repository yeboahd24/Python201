a = {'id': 5, 'username': 'Linux', 'email': 'linux@gmail.com'}
b = {'id': 5, 'username': 'Linux', 'email': 'parrot@gmail.com'}

# Merging in the old way
# print({**b, **a})

# b.update(a)
# print(b)

# New feature
# print(b | a)
# b |= a
# print(b)


# Timezone features
from datetime import datetime
from zoneinfo import ZoneInfo  # new feature do not forget to install tzdata for this to work

# current_time = datetime.now()
# print(current_time)
# current_time_london = datetime.now()
# print(current_time.astimezone(ZoneInfo('Europe/Amsterdam')))


# Type hint
# mylist: list[int] = [1,2,3,4]  # so here there is no need to import the typing libray
# print(mylist)

# remove prefix
data = ['Dr.Linux', 'Dr.Strange']
names = []
for name in data:
    # if name.startwith('Dr.'):
    # names.append(name[4:])
    # else:
    # names.append(name)
    names.append(name.removeprefix('Dr.'))  # so with this reduce the if statement

# print(names)

names = [name.removeprefix('Dr.') for name in data]


# print(names)


def foo(named: str):
    return named


print(foo('linx'))
