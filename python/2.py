class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    num1 = ""
    num2 = ""
    curr_node = l1
    while(curr_node != None):
        num1 += str(curr_node.val)
        curr_node = curr_node.next
    num1 = int(num1[::-1])
    
    curr_node = l2
    while(curr_node != None):
        num2 += str(curr_node.val)
        curr_node = curr_node.next
    num2 = int(num2[::-1])
    
    out = str(num1 + num2)[::-1]
    prev_node = ListNode(int(out[-1]))

    if(len(out) != 1):
        out = out[::-1]
        for x in out[1:]:
            curr_node = ListNode(int(x), prev_node)
            prev_node = curr_node
        return curr_node
    else:
        return prev_node




if __name__ == "__main__":
    #Stuff for l1
    node3 = ListNode(3)
    node2 = ListNode(4, node3)
    node1 = ListNode(2, node2)

    #Stuff for l2
    node6 = ListNode(4)
    node5 = ListNode(6, node6)
    node4 = ListNode(5, node5)

    test_node1 = ListNode(0)
    test_node2 = ListNode(0)

    x = addTwoNumbers(test_node1, test_node2)
    curr_node = x
    while(curr_node != None):
        print(curr_node.val)
        curr_node = curr_node.next