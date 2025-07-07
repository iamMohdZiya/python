

# # def bubbly3(a):
# #     n=len(a)-1
# #     for i in range(n): 
# #         for j in range(n-i):
# #              if a[j] > a[j+1]:
# #                 a[j+1],a[j]= a[j],a[j+1]
# #     return a

# # def bubbly4(a):
# #     n=len(a)-1
# #     for i in range(n): 
# #         for j in range(n-i):
# #              if a[j] < a[j+1]:
# #                 a[j+1],a[j]= a[j],a[j+1]
# #     return a

# # def bubbly2(a):
# #     for i in range(len(a)): 
# #         for j in range(1,len(a)-i):
# #             if a[j-1] > a[j]:
# #                 a[j-1],a[j]= a[j],a[j-1]
# #     return a

# def bubbly(a):
#     for i in range(len(a)-1): 
#         for j in range(len(a)-1):
#             if a[j] > a[j+1]:
#                 a[j+1],a[j]= a[j],a[j+1]
#     return a 



# a = [9,3,4,2,7,4,2,8]
# sortedArray = bubbly(a)
# # sortedArray2= bubbly4(a)

# print(a)
# print(a)

# bubble sort 



def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(a)-1):
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    print(arr)
a = [1,7,4,6,3,2,1]
bubble_sort(a)
