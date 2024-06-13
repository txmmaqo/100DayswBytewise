Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*(n-1)

    
number = 5
factorial(number)
20
#ex2
class listNode:
    def __init__(self, value = 0, next = None):
        self.value = value
        se;f.next = next

        
def isPalindrome(head):
    vals = []
    current = head
    while current:
        vals.append(current.value)
        current = current.nexy
    return vals == vals[::-1]    

       
def createLL(values):
    if not values:
        return None
    head = listNode(values[0])
    current = head
    for value in values[1:]:
        current.next = listNode(value)
        current = current.next
    return head

values1 = [1,2,3,2,1]
head1 = createLL(values1)
if isPalindrome(head1):
    print("The linked list is paloindrome.")
else:
    print("This aint palindrome")

    
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    if isPalindrome(head1):
  File "<pyshell#21>", line 6, in isPalindrome
    current = current.nexy
AttributeError: 'listNode' object has no attribute 'nexy'. Did you mean: 'next'?
def createLL(values):
    if not values:
        return None
    head = listNode(value[0])
    current = head
    for value in values[1:]:
        current.next = listNode(value)
        current = current.next
    return head

def isPalindrome(head):
    vals = []
    current = head
    while current:
        vals.append(current.value)
        current = current.next
    return vals == vals[::-1]

if isPalindrome(head1):
    print("The linked list is paloindrome.")
else:
    print("This aint palindrome")

    
The linked list is paloindrome.
values2 = [1,2,3,4,5]
head2 = createLL(values2)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    head2 = createLL(values2)
  File "<pyshell#58>", line 4, in createLL
    head = listNode(value[0])
UnboundLocalError: cannot access local variable 'value' where it is not associated with a value
def createLL(values):
    if not values:
        return None
    head = listNode(values[0])
    current = head
    for value in values[1:]:
        current.nesxt = listNode(value)
        current = current.next
    return head

if isPalindrome(head2):
    print("The linked list is paloindrome.")
else:
    print("This aint palindrome")

    
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    if isPalindrome(head2):
NameError: name 'head2' is not defined. Did you mean: 'head1'?
head2 = createLL(values2)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    head2 = createLL(values2)
  File "<pyshell#66>", line 7, in createLL
    current.nesxt = listNode(value)
AttributeError: 'NoneType' object has no attribute 'nesxt'
def createLL(values):
    if not values:
        return None
    head = listNode(values[0])
    current = head
    for value in values[1:]:
        current.next = listNode(value)
        current = current.next
    return head

if isPalindrome(head2):
    print("The linked list is paloindrome.")
else:
    print("This aint palindrome")

    
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    if isPalindrome(head2):
NameError: name 'head2' is not defined. Did you mean: 'head1'?
head2 = createLL(values2)
if isPalindrome(head2):
    print("The linked list is paloindrome.")
else:
    print("This aint palindrome")

    
This aint palindrome
#ex3
def mergeSort(arr1, arr3):
    merged_array = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while i<len(arr2):
        merged_aray.append(arr2[j])
        j+=1

        
def mergeSort(arr1, arr3):
    merged_array = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while i<len(arr2):
        merged_aray.append(arr2[j])
        j+=1
    return merged_array
arr1 = [1,2,3]
SyntaxError: invalid syntax
def mergeSort(arr1, arr3):
    merged_array = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while i<len(arr2):
        merged_aray.append(arr2[j])
        j+=1
    return merged_array

arr1 = [1,2,3]
arr2 = [4,5,6]
def mergeSort(arr1, arr2):
    merged_array = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while i<len(arr2):
        merged_aray.append(arr2[j])
        j+=1
    return merged_array

arr1 = [1,2,3]
arr2 = [4,5,6]
result = mergeSort(arr1, arr2)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    result = mergeSort(arr1, arr2)
  File "<pyshell#104>", line 5, in mergeSort
    if arr1[i]<arr[j]:
NameError: name 'arr' is not defined. Did you mean: 'arr1'?
def mergeSort(arr1, arr2):
    merged_array = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while i<len(arr2):
        merged_aray.append(arr2[j])
        j+=1
    return merged_array

arr1 = [1,2,3]
arr2 = [4,5,6]
result = mergeSort(arr1, arr2)
print(result)
[1, 2, 3]
def mergeSort(arr1, arr2):
    merged_array = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while i<len(arr2):
        merged_aray.append(arr2[j])
        j+=1
    return merged_array

arr1 = [1,2,3]
arr2 = [4,5,6]
result = mergeSort(arr1, arr2)
print(result)
[1, 2, 3]
def mergeSort(arr1, arr2):
    merged_array = []
    i,j = 0,0
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            merged_array.append(arr1[i])
            i+=1
        else:
            merged_array.append(arr2[j])
            j+=1
    while i<len(arr1):
        merged_array.append(arr1[i])
        i+=1
    while i<len(arr2):
        merged_aray.append(arr2[j])
        j+=1
    return merged_array

arr2 = [2,4,6]
arr1 = [1,3,5]
result = mergeSort(arr1, arr2)
print(result)
[1, 2, 3, 4, 5]
#ex4
class treeNode:
    def __init__(Self, key):
        self.key = key
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, key):
        if self.root is None:
            self.root = treeNode(key)
        else:
            self._insert(self.root, key)
    def _insert(self, node, key):
        if key<node.key:
            if node.left is None:
                node.left = treeNode(key)
            else:
                self._insert(node.left,key)
        else:
            if node.right is None:
                node.right = treeNode(key)
            else:
                self._insert(node.right, key)
    def search(self, key):
        return self._search(self.root, key)
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right,key)
    def delete (self, key):
        self.root = self._delete(self.root, key)
    def _delete(self, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node,left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.key = min_larger_node.key
            node.right = self._delete(node.right, min_larger_node.ley)
        return node
    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def indrder(self):
        return self._inorder(self.root)
    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.key] + self._inorder(node.right)

    
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)
print("Searching for 40: ", bst.search(40) is not None)
Searching for 40:  True
print("Searching for 40: ", bst.search(90) is not None)
Searching for 40:  False
print("Inorder b4 deletion: ", bst.indrder())
Inorder b4 deletion:  [20, 30, 40, 50, 60, 70, 80]

#ex5
def palindrome(s):
    def expand_around_center(s, left, right):
        while left>= 0 and right <len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    if not s:
        return ''
    longest = ''
    for i in range (len(s)):
        palindrome1 = expand_around_center(s,i,i)
        palindrome2 = expand_around_center(s, i, i+1)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2
    return longest

print(palindrome("babad"))
bab
print(palindrome("cbbd"))
bb
#ex6
def mergeIntervals(intervals):
    if not intervals:
        return []
    instervals.sort(key = lambda x:x[0])
    merged = []
    for interval in intervals:
        if not merged or merged [-1][1] <interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged

intervals = [(1,3),(2,6),(8,10),(15,18)]
mergedIntervals = mergeIntervals(intervals)
Traceback (most recent call last):
  File "<pyshell#350>", line 1, in <module>
    mergedIntervals = mergeIntervals(intervals)
  File "<pyshell#348>", line 4, in mergeIntervals
    instervals.sort(key = lambda x:x[0])
NameError: name 'instervals' is not defined. Did you mean: 'intervals'?
def mergeIntervals(intervals):
    if not intervals:
        return []
    intervals.sort(key = lambda x:x[0])
    merged = []
    for interval in intervals:
        if not merged or merged [-1][1] <interval[0]:
            merged.append(interval)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
    return merged

intervals = [(1,3),(2,6),(8,10),(15,18)]
mergedIntervals = mergeIntervals(intervals)
print(mergedIntervals)
[(1, 6), (8, 10), (15, 18)]
#ex7
def maxSum(nums):
    if not nums:
        return 0
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSum(nums))
6
#ex8
def minDistance(str1, str2):
    m,n = len(str1), len(str2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range (m+1):
        dp[i][0] = i
    for j in range (n+1):
        dp[0][j]=j
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+1)
    return dp[m][n]
str1 = "kitten"
str2 = "sitting"
print(minDistance(str1,str2))
3
