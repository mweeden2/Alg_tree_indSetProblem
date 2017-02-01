# created by Matt Weeden
# 11/8/16
#
# This script solves an arbitrary highest-weight-independant-set-of-a-tree problem

import sys
from pptree import *
from utils import *


# OPTin(u) = w_u + SUM(OPTout(v)) where v is an element of children(u)
def optimal_in(u, l):
    if len(u.children) > 0:
        return u.weight + sum((optimal_out(v, l)[0] for v in u.children)), l + [u]
    else:
        return u.weight, l + [u]

# OPTout(u) = SUM(max(OPTin(v), OPTout(v))) where v is a child of u
def optimal_out(u, l):
    s = 0
    if len(u.children) > 0:
        for v in u.children:
            opt_in, l_in = optimal_in(v, [])
            opt_out, l_out = optimal_out(v, [])
            if opt_in > opt_out:
                s += opt_in
                l += l_in
            else:
                s += opt_out
                l += l_out
    return s, l

def find_max_w_ind_set(n):
    opt_in, l_in = optimal_in(n, [])
    opt_out, l_out = optimal_out(n, [])
    if opt_in > opt_out:
        return opt_in, l_in
    else:
        return opt_out, l_out

def print_sol(n, i):
    print '\n\n===============================================================' \
        + '\nTree ' + str(i) + '\n---------------------------------------------'
    print_tree(n)
    print
    print 'Solution\n---------------------------------------------'
    res = find_max_w_ind_set(n)
    print 'Max Weight:', res[0]
    l = [x.name for x in res[1]]
    l.reverse()
    print 'Set:', l


if __name__ == '__main__':
    n = define_example_1()
    print_sol(n, 1)
    n = define_example_2()
    print_sol(n, 2)
    n = define_example_3()
    print_sol(n, 3)
    n = define_example_4()
    print_sol(n, 4)
    n = define_example_5()
    print_sol(n, 5)
