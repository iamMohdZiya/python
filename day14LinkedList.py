

# # # #  linked list

# # # class LinkedList:
# # #      def __init__(self,data):
# # #           self.data = data
# # #           self.next = None
# # #      def addElementAtLast(self,element):
# # #          self.element = element
# # #          nodeAdd = self.element
# # #          print(currentNode)
# # #          while ( currentNode != None):
# # #                 currentNode.next = self.element
                
             
# # # Node1 = LinkedList(12)
# # # Node2 = LinkedList(33)
# # # Node3 = LinkedList(34)
# # # NodeMid= LinkedList(77)

# # # Node1.next = Node2
# # # Node2.next = NodeMid
# # # NodeMid.next =None
# # # # Node3.next = 
 
# # # head = LinkedList(33)
# # # head.next = Node1

# # # # print(Node2.data)
# # # currentNode = head
# # # Node1.addElementAtLast()
# # # while currentNode != None:
# # #    print(currentNode.data,end = "->")
# # #    currentNode = currentNode.next 
# # # print(None)



# # class node:
# #     def __init__(self,data):
# #         self.data= data
# #         self.next = None
# #     def addElementAtLast(self,element):
# #         self.element = element
# #         nodeAdd = self.element
# #         print(currentNode)
# #         while ( currentNode != None):
# #                currentNode.next = self.element
# #                currentNode = currentNode.next


# # newHead= node(99)
# # head = node(1)
# # n2 = node(2)
# # n3 = node(10)
# # n4 = node(4)
# # nMid = node(3)


# # newHead.next = head
# # head.next = n2
# # # nNew.next = n2
# # n2.next = n3
# # n3.next = nMid

# # nMid = n4

# # n4.next= None

# # currentNode = head
# # # delete link with value 10 
# # while currentNode != None:
# #     print(currentNode.data,end="->")
# #     if currentNode.data == 10:
# #         currentNode.next=currentNode.next 
# #     currentNode = currentNode.next
# # print(None)


# # pop
# # peek
# # isEmpty
# # append

# class stack:
#     def __init__(self):
#         self.item = []
#     def display(self):
#         print(f"stack {self.item}")
#     def is_Empty(self):
#         return len(self.item)==0
#     def pop_stack(self):
#         if not stack.is_Empty(self):
#             return self.item.pop()
#         else :
#             print("stack is empty")
#     def is_peek(self):
#         if not stack.is_Empty(self):
#             return (self.item[-1])
#         else:
#             print("stack is empty")
#     def append_stack(self,data):
#         self.item.append(data)
#         # reverse the stack
#     def reverse_stack(self):
#         # print(self.item[::-1])
#         for i in range(len(self.item)-1,-1,-1):
#             self.item.append(self.item.pop(i))
#         return self.item


# stk = stack()


# stk.append_stack(1)
# stk.append_stack(2)
# stk.append_stack(3)
# stk.append_stack(4)
# stk.append_stack(5)
# stk.append_stack(6)
# stk.append_stack(7)

# stk.display()

# a = stk.reverse_stack()
# print(a)



a = [1,23,4,3,7,1,4,6]
target = 10 
s = set()
n =len(a)
for i in range(n):
    for j in range(n):
        if a[i]+a[j] == target:
            s.add(a[i])
            s.add(a[j])
print(s)


n = 1234

# while n/10 ==0:
#     s = n%10
#     result = 10 * s+













