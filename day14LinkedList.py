

# # # # # #  linked list

# # # # # class LinkedList:
# # # # #      def __init__(self,data):
# # # # #           self.data = data
# # # # #           self.next = None
# # # # #      def addElementAtLast(self,element):
# # # # #          self.element = element
# # # # #          nodeAdd = self.element
# # # # #          print(currentNode)
# # # # #          while ( currentNode != None):
# # # # #                 currentNode.next = self.element
                
             
# # # # # Node1 = LinkedList(12)
# # # # # Node2 = LinkedList(33)
# # # # # Node3 = LinkedList(34)
# # # # # NodeMid= LinkedList(77)

# # # # # Node1.next = Node2
# # # # # Node2.next = NodeMid
# # # # # NodeMid.next =None
# # # # # # Node3.next = 
 
# # # # # head = LinkedList(33)
# # # # # head.next = Node1

# # # # # # print(Node2.data)
# # # # # currentNode = head
# # # # # Node1.addElementAtLast()
# # # # # while currentNode != None:
# # # # #    print(currentNode.data,end = "->")
# # # # #    currentNode = currentNode.next 
# # # # # print(None)



# # # # class node:
# # # #     def __init__(self,data):
# # # #         self.data= data
# # # #         self.next = None
# # # #     def addElementAtLast(self,element):
# # # #         self.element = element
# # # #         nodeAdd = self.element
# # # #         print(currentNode)
# # # #         while ( currentNode != None):
# # # #                currentNode.next = self.element
# # # #                currentNode = currentNode.next


# # # # newHead= node(99)
# # # # head = node(1)
# # # # n2 = node(2)
# # # # n3 = node(10)
# # # # n4 = node(4)
# # # # nMid = node(3)


 





# # # # newHead.next = head
# # # # head.next = n2
# # # # # nNew.next = n2
# # # # n2.next = n3
# # # # n3.next = nMid

# # # # nMid = n4

# # # # n4.next= None

# # # # currentNode = head
# # # # # delete link with value 10 
# # # # while currentNode != None:
# # # #     print(currentNode.data,end="->")
# # # #     if currentNode.data == 10:
# # # #         currentNode.next=currentNode.next 
# # # #     currentNode = currentNode.next
# # # # print(None)


# # # # pop
# # # # peek
# # # # isEmpty
# # # # append

# # # class stack:
# # #     def __init__(self):
# # #         self.item = []
# # #     def display(self):
# # #         print(f"stack {self.item}")
# # #     def is_Empty(self):
# # #         return len(self.item)==0
# # #     def pop_stack(self):
# # #         if not stack.is_Empty(self):
# # #             return self.item.pop()
# # #         else :
# # #             print("stack is empty")
# # #     def is_peek(self):
# # #         if not stack.is_Empty(self):
# # #             return (self.item[-1])
# # #         else:
# # #             print("stack is empty")
# # #     def append_stack(self,data):
# # #         self.item.append(data)
# # #         # reverse the stack
# # #     def reverse_stack(self):
# # #         # print(self.item[::-1])
# # #         for i in range(len(self.item)-1,-1,-1):
# # #             self.item.append(self.item.pop(i))
# # #         return self.item


# # # stk = stack()


# # # stk.append_stack(1)
# # # stk.append_stack(2)
# # # stk.append_stack(3)
# # # stk.append_stack(4)
# # # stk.append_stack(5)
# # # stk.append_stack(6)
# # # stk.append_stack(7)

# # # stk.display()

# # # a = stk.reverse_stack()
# # # print(a)
# # # how to convert linklist in list 















# # # You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# # # You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# # # Input: l1 = [2,4,3], l2 = [5,6,4]
# # # Output: [7,0,8]
# # # Explanation: 342 + 465 = 807.
# # # Example 2:

# # # Input: l1 = [0], l2 = [0]
# # # Output: [0]
# # # Example 3:

# # # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# # # Output: [8,9,9,9,0,0,0,1]




# # # class ListNode:
# # #     def __init__(self, data=0, next=None):
# # #         self.data = data
# # #         self.next = next
# # # def addTwoNumbers( l1: [ListNode], l2: [ListNode]) -> [ListNode]:
# # #         result = []
# # #         current = l1 
# # #         while current != None:
# # #             result.append(current.data)
# # #             current = current.next
# # #         reversedList = result.reverse()
# # #         return reversedList

# # # # why none is none
        
             
# # # Node1 = ListNode(12)
# # # Node2 = ListNode(33)
# # # Node3 = ListNode(34)
# # # NodeMid= ListNode(77)

# # # Node1.next = Node2
# # # Node2.next = NodeMid
# # # NodeMid.next =Node3




# # # my_list = [1, 2, 3, 4, 5]
# # # int_result = int(''.join(map(str, my_list)))
# # # print("Result:", int_result)


# # # class ListNode:
# # #     def __init__(self, val=0, next=None):
# # #         self.val = val
# # #         self.next = next
# # # digit_list = [int(digit) for digit in str(number)]
# # # class Solution:
# # #     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
# # #         result = []
# # #         current = l1
# # #         while current != None:
# # #             result.append(current.val)
# # #             current = current.next
# # #         # print (result[::-1])
# # #         result1 = int(''.join(map(str, result)))
# # #         # print(result1)


# # #         result2 = []
# # #         current = l2
# # #         while current != None:
# # #             result2.append(current.val)
# # #             current = current.next
# # #         # print (result2[::-1])
# # #         result3 = int(''.join(map(str, result2)))
# # #         # print(result3)

# # #         addition = result1+result3
# # #         digit_list = [int(x) for x in str(addition)]
# # #         print(digit_list[::-1])
# # #         new = ListNode(0)
# # #         current = new
# # #         for digit in digit_list:
# # #             current.next = ListNode(digit)
# # #             current = current.next
# # #         print(new.next)

# # # # Example usage
# # # l1 = ListNode(2)
# # # l1.next = ListNode(4)
# # # l1.next.next = ListNode(3)

# # # l2 = ListNode(5)
# # # l2.next = ListNode(6)
# # # l2.next.next = ListNode(4)

# # # solution = Solution()
# # # result = solution.addTwoNumbers(l1, l2)

# # # # Print the result
# # # while result:
# # #     print(result.val, end=" ")
# # #     result = result.next

# # # class ListNode:
# # #     def __init__(self, val=0, next=None):
# # #         self.val = val
# # #         self.next = next
# # # digit_list = [int(digit) for digit in str(number)]
# # # class Solution:
# # #     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
# # #         result = []
# # #         current = l1
# # #         while current != None:
# # #             result.append(current.val)
# # #             current = current.next
# # #         # print (result[::-1])
# # #         result1 = int(''.join(map(str, result)))
# # #         # print(result1)


# # #         result2 = []
# # #         current = l2
# # #         while current != None:
# # #             result2.append(current.val)
# # #             current = current.next
# # #         # print (result2[::-1])
# # #         result3 = int(''.join(map(str, result2)))
# # #         # print(result3)

# # #         addition = result1+result3
# # #         # digit_list = [int(x) for x in str(addition)]
# # #         digit_list= list(map(int, str(addition)))
# # #         # print(digit_list)
# # #         reverseList=digit_list[::-1]
# # #         # print(reverseList)
# # #         current = ListNode(0)
       
# # # #         for digit in reverseList:
# # # #             current.next = ListNode(digit)
# # # #             current = current.next
# # # #         return current.next
            

# # # # Definition for singly-linked list.
# # # class ListNode(object):
# # #     def __init__(self, val=0, next=None):
# # #         self.val = val
# # #         self.next = next



# # # class Solution(object):
# # #     def addTwoNumbers(self, l1, l2):
# # #         # :type l1: Optional[ListNode]
# # #         # :type l2: Optional[ListNode]
# # #         # :rtype: Optional[ListNode]
        
# # #         head = ListNode()
# # #         current = head
# # #         carry = 0
# # #         # This line checks if there are any remaining digits to process
# # #         while l1 or l2 or carry:
# # #             if l1:
# # #                 val1=l1.val
# # #             else:
# # #                 val1=0
# # #             if l2:
# # #                 val2=l2.val
# # #             else:
# # #                 val2=0


# # #             total = val1 + val2 + carry
# # #             carry = total // 10
# # #             current.next = ListNode(total % 10)

# # #             current = current.next
# # #             if l1:
# # #                 l1=l1.next
# # #             else:
# # #                 l1=None
# # #             if l2:
# # #                 l2=l2.next
# # #             else:
# # #                 l2=None

# # #         return head.next



d =[1,3,4,6,8,32,1]
target = 9
start = 0
end = len(d)-1
dictionary = {}
while end >=start: 
    if d[start] + d[end] == target:
        dictionary[(d[start], d[end])] = (start, end)
        start += 1
        end -= 1
    elif d[start] + d[end] < target:
        start += 1
    else:
        end -= 1
print(dictionary)



d = [1,3,4,6,8,32,1]
target = 9
dictionary = {}
for i in range(len(d)):
    dif = target - d[i]
    if dif in dictionary:
        print(f"Pair found: ({dif}, {d[i]})")
    dictionary[d[i]] = i