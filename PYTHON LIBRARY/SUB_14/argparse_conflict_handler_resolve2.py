import argparse

parser = argparse.ArgumentParser(conflict_handler='resolve')
parser.add_argument('-a', action="store")
parser.add_argument('--long-b', '-b',
action="store",
help='Long and short together')
parser.add_argument('-b', action="store", help='Short alone')
print(parser.parse_args(['-h']))