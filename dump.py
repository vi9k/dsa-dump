x = "ajshgdjagsjdhgjagsdjg"

# output:
# {a: 3,
#  j: 4, }
count = {}
# for char in x:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
# print(count)
from collections import Counter

count = Counter(list(x))
third_largest = sorted(count.items(), key=lambda items: (-items[1],))[2][1]
skip=0
print(dict(count))
l=[]
for k,v in sorted(count.items(), key=lambda items: (-items[1],)):
    if v == third_largest:
        l.append((k,v))

print(l)
