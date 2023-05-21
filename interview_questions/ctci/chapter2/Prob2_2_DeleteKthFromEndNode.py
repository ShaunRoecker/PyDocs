from linked_list import LinkedList

def kth_to_last(ll, k):
    leader = follower = ll.head
    count = 0

    while leader:
        if count >= k:
            follower = follower.next
        count += 1
        leader = leader.next
    return follower


