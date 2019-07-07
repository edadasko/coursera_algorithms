'''
Task. You are given a binary tree with integers as its keys. You need to
      test whether it is a correct binary search tree. The definition of the
      binary search tree is the following: for any node of the tree, if its
      key is x, then for any node in its left subtree its key must be strictly
      less than x, and for any node in itsright subtree its key must be
      strictly greater than x. In other words, smaller elements are to the
      left, and bigger elements are to the right.
      You need to check whether the given binary tree structure satisfies this
      condition. You are guaranteed that the input contains a valid binary tree.
      That is, it is a tree, and each node has at most two children.
Input Format. The first line contains the number of vertices n. The vertices
              of the tree are numbered from 0 to 𝑛−1. Vertex 0 is the root.
              The next n lines contain information about vertices 0, 1, ..., n − 1
              in order. Each of these lines contains three integers key(i), left(i)
              and right(i) — key(i) is the key of the i-th vertex, left(i) is the
              index of the left child of the i-th vertex, and right is the index of
              the right child of the i-th vertex. If 𝑖 doesn’t have left or right child
              (or both), the corresponding left(i) or right(i) (or both) will be equal to −1.
Output Format. If the given binary tree is a correct binary search tree (see the definition
               in the problem description), output one word “CORRECT” (without quotes).
               Otherwise, output one word “INCOR- RECT” (without quotes).
'''
import sys
import threading
import math

sys.setrecursionlimit(10 ** 6)
threading.stack_size(2 ** 27)


class Tree:
    def __init__(self):
        self.n = int(sys.stdin.readline())
        self.key = [0] * self.n
        self.left = [0] * self.n
        self.right = [0] * self.n
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def is_binary(self):
        return True if not self.n else self._is_binary(0, -math.inf, math.inf)
    
    def _is_binary(self, node, min_key, max_key):
        if node == -1:
            return True
    
        is_left_subtree_correct = self._is_binary(self.left[node], min_key, self.key[node])
        is_right_subtree_correct = self._is_binary(self.right[node], self.key[node], max_key)
        return min_key < self.key[node] < max_key and\
            is_left_subtree_correct and is_right_subtree_correct


def main():
    tree = Tree()
    print('CORRECT' if tree.is_binary() else 'INCORRECT')


threading.Thread(target=main).start()
