# created by Matt Weeden
# 11/9/16
#
# This script generates a string that can be used to define an example tree for the w_tree.py script

import sys
import random
import string


# check that cmd line arguments are ok
def get_args(args):
    usage = 'Usage: python tree_gen.py [-d min_depth_of_tree] [-n number_of_nodes]\nNOTE: 1 <= number_of_nodes <= 27'

    min_depth = -1
    num_nodes = -1

    if not len(args) in [1, 3, 5]:
        print usage
        sys.exit()

    if len(args) > 1:
        last_arg = ""
        for arg in args:
            if last_arg == "-d":
                try:
                    min_depth = int(arg)
                    if min_depth > 26 or min_depth < 1:
                        print usage
                        sys.exit()
                except ValueError:
                    print usage
                    sys.exit()
            if last_arg == "-n":
                try:
                    num_nodes = int(arg)
                    if num_nodes > 27 or num_nodes < 1:
                        print usage
                        sys.exit()
                except ValueError:
                    print usage
                    sys.exit()
            last_arg = arg

    return min_depth, num_nodes


if __name__ == '__main__':
    d, n = get_args(sys.argv)

    letters = "R" + string.letters[:26]

    print "R = Node(" + str(random.randint(0, 125)) + ", \"R\")"
    for i in range(1, n):
        parent_num = random.randint(0, i-1)
        parent = letters[parent_num]
        print letters[i], '= Node(' + str(random.randint(0, 125)) + ', "' + letters[i] + '", ' + parent + ')'
