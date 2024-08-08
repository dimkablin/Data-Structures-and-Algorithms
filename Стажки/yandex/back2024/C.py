def main():
    input_data = """5
        1 4
        2 5
        3 1
        4 5
        5 6"""
    
    data = input_data.split()
    
    N = int(data[0])
    a = []
    b = []
    
    for i in range(1, len(data), 2):
        a.append(int(data[i]))
        b.append(int(data[i+1]))

    ids = list(range(N))
    
    ids.sort(key=lambda i: (a[i], b[i]))

    bad = [0] * N

    max_b = 0
    for i in ids:
        if b[i] <= max_b:
            bad[i] = 1
        max_b = max(max_b, b[i])

    min_b = float('inf')
    ids.reverse()
    for i in ids:
        if b[i] >= min_b:
            bad[i] = 1
        min_b = min(min_b, b[i])

    ans = sum(1 for x in bad if x == 0)
    print(ans)

if __name__ == "__main__":
    main()
