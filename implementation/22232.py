# import re
from functools import cmp_to_key as cmp
n, m = map(int, input().split())

files = []
os = set()
for _ in range(n):
    file = input().split('.')
    # regmatch = re.match('(?P<name>\w+)\.(?P<ext>\w+)', file)
    # files.append((regmatch.group('name'), m.group('ext')))
    files.append(file)

for _ in range(m):
    input()

def compare(a, b):
    return ord(b) - ord(a)

def f(a,b):
    n = min(len(a), len(b))
    for i in range(n):
        res = compare(a[i], b[i])
        if  res != 0:
            return res

    return 1 if len(a) < len(b) else -1

files.sort(key = cmp(lambda a, b : 1 if a[0] > b[0] else (-1 if a[0] < b[0] else f(a[1], b[1]))))
print(*[el[0]+'.'+el[1] for el in files], sep='\n')