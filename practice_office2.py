s = input("enter the string:-")
res = ""
count = 1

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        res += s[i] + str(count)
        count = 1   # reset
# handle the last character
res += s[-1] + str(count)
print(res)
# s = input("Enter the string:-")

# max_len = 0
# current_len = 1
# max_sub = ""
# current_sub = s[0]

# for i in range(len(s)-1):
#     if ord(s[i+1]) - ord(s[i]) == 1:
#         current_len += 1
#         current_sub += s[i+1]
#     else:
#         if current_len > max_len:
#             max_len = current_len
#             max_sub = current_sub
#         current_len = 1
#         current_sub = s[i+1]

# # final check (for last substring)
# if current_len > max_len:
#     max_len = current_len
#     max_sub = current_sub

# print(max_sub)

# s = input("Enter the string: ")

# # Step 1: create alphabet mapping manually
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# char_pos = {}           # store each char → position
# pos = 0

# # fill mapping without using index()
# for ch in alphabet:
#     char_pos[ch] = pos
#     pos += 1

# max_len = 1
# current_len = 1

# # Step 2: check consecutive characters
# for i in range(len(s) - 1):
#     if char_pos[s[i+1]] - char_pos[s[i]] == 1:
#         current_len += 1
#     else:
#         if current_len > max_len:
#             max_len = current_len
#         current_len = 1

# # Step 3: final check
# if current_len > max_len:
#     max_len = current_len

# print(max_len)
