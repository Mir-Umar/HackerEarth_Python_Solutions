num = input()                  # Reading input from STDIN
inp_ls = list(map(int, input().split()))

# Using for loop
# singer_count = {}
# for singer in inp_ls:
#     if singer in singer_count:
#         singer_count[singer] += 1
#     else:
#         singer_count[singer] = 1

# # Find the maximum count
# max_count = max(singer_count.values())

# # Count the number of favorite singers
# print(sum(1 for count in singer_count.values() if count == max_count))


# Using collections module of python
from collections import Counter
singer_count = dict(Counter(inp_ls))

# Find the maximum count
max_count = max(singer_count.values())

# Count the number of favorite singers
print(sum(1 for count in singer_count.values() if count == max_count))