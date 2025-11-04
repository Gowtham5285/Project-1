n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():  # opening brackets
            stack.append(char)
        elif char in mapping:         # closing brackets
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False  # invalid character
    return not stack
print(is_valid("(){}"))

chars = ['b', 'a', 'd', 'b', 'c', 'a']
unique = []

# Remove duplicates manually
for ch in chars:
    if ch not in unique:
        unique.append(ch)

# Sort manually (Bubble Sort)
for i in range(len(unique)):
    for j in range(i + 1, len(unique)):
        if unique[i] > unique[j]:
            unique[i], unique[j] = unique[j], unique[i]

print("Final sorted unique list:", unique)


