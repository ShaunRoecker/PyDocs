from linked_list import LinkedList


def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.append_all([1, 2, 3, 4])
    middle_node = ll.add(5)
    ll.append_all([7, 8, 9])

    print(ll)
    delete_middle_node(middle_node)
    print(ll)