#***************Q1*************#
class Solution:
    def deleteNode(self, node:ListNode):
        node.val  = node.next.val
        node.next = node.next.next
        return
    
    #************Q2***********#
    class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        dummy_head = ListNode(-1)
        dummy_head.next = head
        
        current_node = dummy_head
        while current_node.next != None:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
                
        return dummy_head.next
    
    #**************Q3************#
    class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next
    
    #****************Q4***************#
    class Solution:
  def detectCycle(self, head: ListNode) -> ListNode:
    # Initialize two pointers, slow and fast, to the head of the linked list.
    slow = head
    fast = head

    # Move the slow pointer one step and the fast pointer two steps at a time through the linked list,
    # until they either meet or the fast pointer reaches the end of the list.
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        # If the pointers meet, there is a cycle in the linked list.
        # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
        # until they meet again. The node where they meet is the starting point of the cycle.
        slow = head
        while slow != fast:
          slow = slow.next
          fast = fast.next
        return slow

    # If the fast pointer reaches the end of the list without meeting the slow pointer,
    # there is no cycle in the linked list. Return None.
    return None

#******************Q5*****************#
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if not fast: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head
    
    #*********************Q6****************#
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        lastElement = head
        length = 1
        # get the length of the list and the last node in the list
        while ( lastElement.next ):
            lastElement = lastElement.next
            length += 1

        # If k is equal to the length of the list then k == 0
        # ElIf k is greater than the length of the list then k = k % length
        k = k % length
            
        # Set the last node to point to head node
        # The list is now a circular linked list with last node pointing to first node
        lastElement.next = head
        
        # Traverse the list to get to the node just before the ( length - k )th node.
        # Example: In 1->2->3->4->5, and k = 2
        #          we need to get to the Node(3)
        tempNode = head
        for _ in range( length - k - 1 ):
            tempNode = tempNode.next
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = tempNode.next
        tempNode.next = None
        
        return answer
    
    #********************Q7*****************#
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        # can be solved by finding prefix sum;
        # if l1+l2 = l1+l2+...+l5, meaning that l3 + ... + l5 = 0, 
		# then l3 + ... + l5 is the consecutive sequence of nodes we want to delete. 
		# If it's a array we could just remove numbers from index of l3 to l5. 
		# If it's a linked list, we could let l2.next = l5.next, we then need to have two pointers,
		# one point to l2 and the other point to l5;
        dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        d = {0:dummy} # key is the prefix sum, value is the last node of getting this sum value, which is l5
        while head:
            prefix += head.val
            d[prefix] = head
            head = head.next
		# Go from the dummy node again to set the next node to be the last node for a prefix sum 
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = d[prefix].next
            head = head.next
        
        return dummy.next
    
    #*****************Q8******************#
    class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        ## RC ##
        ## LOGIC : START WITH BASIC EVEN AND ODD POSITIONS, FOR NEXT ODD APPEND EVENS NEXT AND FOR NEXT EVEN APPEND ODDS NEXT ##
        
		## TIME COMPLEXITY : O(N) ##
		## SPACE COMPLEXITY : O(1) ##

        if(not head): return head
        odd = head
        even = head.next
        evenHead = even
        while(even and odd and even.next and odd.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head
