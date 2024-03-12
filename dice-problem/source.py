def count_ways(n):
    if n<0:
        return 0
    
    ways = [0] * (n+1)
    ways[0] = 1  
    
    for i in range(1, n+1):
        for j in range(1, 7):
            if i >= j:
                ways[i] += ways[i-j]

    return ways[n]


n = int(input())
for _ in range(n):
    ans = count_ways(int(input()))
    file1 = open("output.txt", "a")  # append mode
    file1.write(str(ans)+"\n")
    file1.close()
