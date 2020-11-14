s=input()
arr=[list() for i in range(26)]
for n,i in enumerate(s):
    order=ord(i)-ord('A')
    arr[order].append(n)
    print(arr)

a=0
for i in range(26):
    for j in range(i+1,26):
        print(f'arr[{i}] = {arr[i]}, arr[{j}] = {arr[j]}')
        if arr[i][0]<arr[j][0]<arr[i][1]<arr[j][1] or arr[j][0]<arr[i][0]<arr[j][1]<arr[i][1]:
            a+=1
print(a)