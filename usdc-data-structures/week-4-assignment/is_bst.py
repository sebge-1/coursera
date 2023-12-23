#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**9) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def IsBinarySearchTree(tree):
    if not tree:
          return True

    def traverse_in_order(index, min_val, max_val):
        if index == -1:
            return True

        key = get_key(tree[index])
        if key < min_val or key > max_val:
            return False

        left_index = get_left_index(tree[index])
        right_index = get_right_index(tree[index])

        is_left_bst = traverse_in_order(left_index, min_val, key)
        is_right_bst = traverse_in_order(right_index, key, max_val)

        return is_left_bst and is_right_bst

    root = 0
    root_key = get_key(tree[root])
    left_index = get_left_index(tree[root])
    right_index = get_right_index(tree[root])

    is_left_bst = traverse_in_order(left_index, float('-inf'), root_key)
    is_right_bst = traverse_in_order(right_index, root_key, float('inf'))

    return is_left_bst and is_right_bst

def get_key(array):
  return array[0]

def get_left_index(array):
  return array[1]

def get_right_index(array):
  return array[2]

def main():
  nodes = int(sys.stdin.readline().strip())
  tree = []
  for i in range(nodes):
    tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree(tree):
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
