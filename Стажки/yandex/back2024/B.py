def main(inputs):
    
    data = input().split()

    N = int(data[0])
    Q = int(data[1])

    first_time = {}
    last_time = {}
    print(data)
    index = 2
    for i in range(N):
        s = data[index]
        index += 1
        prefix = ""
        for j in range(len(s)):
            prefix += s[j]
            if prefix not in first_time:
                first_time[prefix] = i
            last_time[prefix] = i

    results = []
    for _ in range(Q):
        k = int(data[index])
        p = data[index + 1]
        index += 2
        if p not in first_time:
            results.append(-1)
            continue
        id = first_time[p] + k - 1
        if id > last_time[p]:
            results.append(-1)
            continue
        results.append(id + 1)

    print("\n".join(results))
    

if __name__ == "__main__":
    main("""10 3
aa
aaa
aab
ab
abc
ac
ba
daa
dab
dadba
4 a
2 da
4 da""")
