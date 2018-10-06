"""
  This program won't run properly without an input.
  Try with: 24 45 16 67 32
"""
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current))
            current = current.next
        return ' => '.join(nodes)

    def empty(self):
        return self.head is None

    # Get a Node with given value; returns first match
    def get_node(self, value):
        if self.empty():
            return None
        current = self.head
        while current and current.value != value:
            current = current.next
        return current

    # Insert a node at position n; n is 0 based
    def insert_at(self, value, n):
        if n < 0 or n > self.length:
            return None # handle invalid positions
        new_node = Node(value)
        if n == 0: # insert at beginning
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            insert_pos = 1 # 0 is handled in above if
            while insert_pos < n:
                current = current.next
                insert_pos += 1
            new_node.next = current.next
            current.next = new_node
        self.length += 1
        return new_node

    # Insert at end
    def append(self, value):
        self.insert_at(value, self.length)

    def delete(self, node):
        if self.empty() or node is None:
            return None # return if nothing in list or invalid node
        current = self.head
        prev = None
        while current and current != node:
            prev = current
            current = current.next
        if current: # found the node
            if current == self.head: # first node in list
                self.head = current.next
            else:
                prev.next = current.next
            self.length -= 1
            return node
        return None # node not found

    def reverse(self):
        if self.empty():
            return self # return without doing anything
        current_node = self.head
        prev_node = next_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        return self

    #### Recursive implementations
    def print_list(self, current_node):
        if not current_node:
            return
        sys.stdout.write('%s ' % current_node)
        self.print_list(current_node.next)

    def print_reverse(self, current_node):
        if not current_node:
            return
        self.print_reverse(current_node.next)
        sys.stdout.write('%s ' % current_node)

    def reverse_recursive(self, current_node):
        if not current_node:
            return self
        self.head = current_node
        self.reverse_recursive(current_node.next)
        if current_node.next:
            current_node.next.next = current_node
            current_node.next = None
        return self

############################## TESTING ##############################
if __name__ == '__main__':
    ll = LinkedList()
    print('Is list empty? %s' % ll.empty())
    print('List: %s' % ll)

    # Try with: 24 45 16 67 32
    list_items = sys.stdin.readline().strip().split(' ') # Read via STDIN
    # list_items = sys.argv[1:] # Read via CommandLine
    if list_items: # list from user input
        for i in list_items:
            ll.append(i)
            print('List: %s' % ll)
        print('List: %s' % ll.reverse())
        for i in list_items:
            ll.delete(ll.get_node(i))
            print('List: %s' % ll)
    else: # Do some random testing
        ll.append(1)
        print('List: %s' % ll)
        ll.append(3)
        print('List: %s' % ll)
        ll.insert_at(2, 1)
        print('List: %s' % ll)
        ll.append(4)
        print('List: %s' % ll)
        ll.print_list(ll.head)
        print('')
        print('List: %s' % ll.reverse())
        print('List: %s' % ll.reverse_recursive(ll.head))
        ll.print_reverse(ll.head)
        print('')

        ll.delete(ll.get_node(2))
        print('List: %s' % ll)
        ll.delete(ll.get_node(1))
        print('List: %s' % ll)
        ll.insert_at(5, 0)
        print('List: %s' % ll)
        ll.delete(ll.get_node(3))
        print('List: %s' % ll)
        ll.delete(ll.get_node(4))
        print('List: %s' % ll)
        ll.delete(ll.get_node(5))
        print('List: %s' % ll)

    print('Is list empty? %s' % ll.empty())

'''
Is list empty? True
List:
List: 1
List: 1 => 3
List: 1 => 2 => 3
List: 1 => 2 => 3 => 4
1 2 3 4
List: 4 => 3 => 2 => 1
List: 1 => 2 => 3 => 4
4 3 2 1
List: 1 => 3 => 4
List: 3 => 4
List: 5 => 3 => 4
List: 5 => 4
List: 5
List:
Is list empty? True
'''
