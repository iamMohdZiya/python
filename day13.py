
# # # a = [38, 27, 43, 3, 9, 82, 10]
# # # print(a)
# # # def merge_sort(arr):
# # #     if len(arr) <= 1:
# # #         return arr

# # #     mid = len(arr) // 2
# # #     left_half = merge_sort(arr[:mid])
# # #     right_half = merge_sort(arr[mid:])

# # #     return merge(left_half, right_half)
# # # def merge(left, right):
# # #     result = []
# # #     i = j = 0

# # #     while i < len(left) and j < len(right):
# # #         if left[i] <= right[j]:
# # #             result.append(left[i])
# # #             i += 1
# # #         else:
# # #             result.append(right[j])
# # #             j += 1

# # #     while i < len(left):
# # #         result.append(left[i])
# # #         i += 1
# # #     while j < len(right):
# # #         result.append(right[j])
# # #         j += 1

# # #     return result


# # # r = merge_sort(a)
# # # print(r)  



# # # quick sort 

# # def quick_sort(arr):
# #     if (len(arr)<=1):
# #         return arr
# #     small=[]
# #     large=[]
# #     pivot = arr[0]
# #     for i in range(1,len(arr)):
# #         if arr[i]<pivot:
# #             small.append(arr[i])
# #         else:
# #             large.append(arr[i])
# #     return quick_sort(small)+[pivot]+quick_sort(large)

# # aaa = [9,3,3,3,3,10,3,5,2,9,1,10,10,10]
# # r = quick_sort(aaa)
# # print(r)





# # prefix sum
# a = [1, 1, 1, 1, 1, 1, 1]
# def prefix_sum(start,end):
#     sum=0
#     for i in range(start,end+1):
#         sum=sum+a[i]
#     return sum
# print(prefix_sum(1,4))

# # prefix sum with cumulative sum array
# def prefix_sum_cumulative(arr, start, end):
#     cumulative_sum = [0] * (len(arr) + 1)
#     for i in range(1, len(arr) + 1):
#         cumulative_sum[i] = cumulative_sum[i - 1] + arr[i - 1]
    
#     return cumulative_sum[end + 1] - cumulative_sum[start]



# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.cumulative_sum = [0] * (len(nums) + 1)
#         for i in range(1, len(nums) + 1):
#             self.cumulative_sum[i] = self.cumulative_sum[i - 1] + nums[i - 1]

#     def sumRange(self, left: int, right: int) -> int:
#         sum = [0]* [len(nums)]   


# # Your NumArray object will be instantiated and called as such:
# # obj = NumArray(nums)
# # param_1 = obj.sumRange(left,right)


# class Solution:
#     def sortArray(self, arr: List[int]) -> List[int]:
#         if (len(arr)<=1):
#             return arr
#         small=[]
#         large=[]
#         pivot = arr[0]
#         for i in range(1,len(arr)):
#             if arr[i]<pivot:
#                 small.append(arr[i])
#             else:
#                 large.append(arr[i])
#         return sortArray(small)+[pivot]+sortArray(large)     
    



#     class Solution:
#     def sortArray(self, arr: List[int]) -> List[int]:
#         if len(arr) <= 1:
#             return arr

#         mid = len(arr) // 2
#         left_half = self.sortArray(arr[:mid])
#         right_half = self.sortArray(arr[mid:])

#         return self.merge(left_half, right_half)

#     def merge(self, left, right):
#         result = []
#         i = j = 0

#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1

#         while i < len(left):
#             result.append(left[i])
#             i += 1
#         while j < len(right):
#             result.append(right[j])
#             j += 1

#         return result
    




