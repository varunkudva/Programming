"""
Largest sum contiguous subarray
Given a array, find a contiguous sub-array within the array which has the largest sum.
Array has both positive and negative integers

Solution:
Kadanes algorithm

"""
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

def maxSum(A):
    min_idx, max_idx = 0,0
    max_sum = 0
    sum = 0
    for i in range(0, len(A)):
        sum += A[i]
        if sum > max_sum: max_idx = i
        max_sum = max(sum, max_sum)
        if sum < 0:
            sum = 0
            min_idx = i+1
    print(min_idx, max_idx, A[min_idx:max_idx+1])

# The bruteforce approach
def maxsum_brute(A):
    max = A[0]
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]
            if sum > max:
                max = sum
    return max

#maxSum(A)
print(maxsum_brute(A))
