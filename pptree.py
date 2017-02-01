# -*- coding: utf-8 -*-
"""
Clement Michard (c) 2015

modified by Matt Weeden
11/8/16
"""

class Node:
    def __init__(self, weight, name, parent=None):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = []

        if parent:
            self.parent.children.append(self)


def print_tree(current_node, indent="", last='updown'):

    nb_children = lambda node: sum(nb_children(child) for child in node.children) + 1
    size_branch = {child: nb_children(child) for child in current_node.children}

    """ Creation of balanced lists for "up" branch and "down" branch. """
    up = sorted(current_node.children, key=lambda node: nb_children(node))
    down = []
    while up and sum(size_branch[node] for node in down) < sum(size_branch[node] for node in up):
        down.append(up.pop())

    """ Printing of "up" branch. """
    for child in up:
        next_last = 'up' if up.index(child) is 0 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'up' in last else '│', " " * (len(current_node.name)+len(str(current_node.weight))+3))
        print_tree(child, indent=next_indent, last=next_last)

    """ Printing of current node. """
    if last == 'up': start_shape = '┌'
    elif last == 'down': start_shape = '└'
    elif last == 'updown': start_shape = ' '
    else: start_shape = '├'

    if up: end_shape = '┤'
    elif down: end_shape = '┐'
    else: end_shape = ''

    print('{0}{1}{2}{3}{4}'.format(indent, start_shape, current_node.name + ' (', str(current_node.weight) + ')', end_shape))

    """ Printing of "down" branch. """
    for child in down:
        next_last = 'down' if down.index(child) is len(down) - 1 else ''
        next_indent = '{0}{1}{2}'.format(indent, ' ' if 'down' in last else '│', " " * (len(current_node.name)+len(str(current_node.weight))+3))
        print_tree(child, indent=next_indent, last=next_last)
