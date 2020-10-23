import argparse
# parser = argparse.ArgumentParser() # this initialize the process
# parser.add_argument('echo')  # positional argument 'echo' for now it does nothing
# parser.add_argument('square', help='display a square of a given number', type=int) # here we specify what the postional agrgument does with the help text
# print(arg.square**2)

# Optional arguments
# parser.add_argument('-v','--verbosity',help='increase output verbosity', action='store_true')
# arg = parser.parse_args()
# if arg.verbosity:
# 	print('verbosity turned on')

# combination of optional and positional agrument
# parser.add_argument('square', help='display a square of a given number', type=int)
# parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
# args = parser.parse_args()
# answer = args.square**2

# if args.verbose:
# 	print(f'the square of {args.square} is {answer}')
# else:
# 	print(answer)


#restricting values of --verbose

# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity",type=int, choices=[0, 1, 2],
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)




# parser.add_argument("square", type=int,
#                     help="display the square of a given number")
# parser.add_argument("-v", "--verbosity", action="count",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity == 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity == 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)



# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", action="count",
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2

# # bugfix: replace == with >=
# if args.verbosity >= 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity >= 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)


# parser.add_argument("square", type=int,
#                     help="display a square of a given number")
# parser.add_argument("-v", "--verbosity", action="count", default=0,
#                     help="increase output verbosity")
# args = parser.parse_args()
# answer = args.square**2
# if args.verbosity >= 2:
#     print("the square of {} equals {}".format(args.square, answer))
# elif args.verbosity >= 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)



parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))