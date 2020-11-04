'''
@Author: haikuoxin  
@Date: 2020-11-04 04:50:45  
@Last Modified by:   haikuoxin  
@Last Modified time: 2020-11-04 04:50:45 
'''
from queue import Queue

class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def create_binary_tree(input_list=[]):
    """
    构建二叉树
    """
    if input_list is None or len(input_list) == 0:
        return None

    data = input_list.pop(0)
    if data is None:
        return None
    node = TreeNode(data)
    node.left = create_binary_tree(input_list)
    node.right = create_binary_tree(input_list)
    return node

def pre_order_traversal(node):
    """
    前序遍历
    """
    if node is None:
        return
    print(node.data)
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)
    return node

def in_order_traversal(node):
    """
    中序遍历
    """
    if node is None:
        return
    in_order_traversal(node.left)
    print(node.data)
    in_order_traversal(node.right)
    return node

def post_order_traversal(node):
    """
    后序遍历
    """
    if node is None:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node.data)
    return node

def level_order_traversal(node):
    """
    广度优先遍历
    """
    queue = Queue()
    queue.put(node)
    while not queue.empty():
        node = queue.get()
        print(node.data)
        if node.left is not None:
            queue.put(node.left)
        if node.right is None:
            queue.put(node.right)



if __name__ == "__main__":
    my_input_list = [3, 2, 9, None, None, 10, None, None, 8, None, 4]
    root = create_binary_tree(my_input_list)
    print('前序遍历')
    pre_order_traversal(root)
    print('中序遍历')
    in_order_traversal(root)
    print('后序遍历')
    post_order_traversal(root)