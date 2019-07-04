'''
Compute tree height
Task. You are given a description of a rooted tree. Your task is to compute and output its height.
      Recall that the height of a (rooted) tree is the maximum depth of a node, or the maximum
      distance from a leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.
Input Format. The first line contains the number of nodes n. The second line contains n integer numbers
              from −1 to n − 1 — parents of nodes. If the i-th one of them (0 <= i <= n − 1) is −1,
              node i is the root, otherwise it’s 0-based index of the parent of i-th node.
              It is guaranteed that there is exactly one root. It is guaranteed that the input represents a tree.
Output Format. Output the height of the tree.
'''

import sys
import threading


class Node:
    def __init__(self, key):
        self.key = key
        self.childs = []
    
    def add_child(self, node):
        self.childs.append(node)


def make_tree(parents):
    size = len(parents)
    root = None
    nodes = [Node(i) for i in range(size)]
    for i in range(size):
        if parents[i] != -1:
            nodes[parents[i]].add_child(nodes[i])
        else:
            root = nodes[i]
    return root


def compute_height(tree):
    if not tree.childs:
        return 1
    else:
        return max(map(compute_height, tree.childs)) + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    tree = make_tree(parents)
    print(compute_height(tree))


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
