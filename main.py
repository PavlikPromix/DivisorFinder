n = int(input("Enter n: "))
arr = []

for i in range(n):
    if n % (i+1) == 0:
        arr.append(i+1)
        arr.append(n/(i+1))
for i in range(int(len(arr)/2)):
    if i%2!=0:
        pass
    else:
        print("{} {}".format(int(arr[i]), int(arr[i+1])))