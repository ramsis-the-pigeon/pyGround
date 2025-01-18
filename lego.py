MOD = 10**9 + 7

def legoBlocks(n, m):
    #Calculate single row configurations
    ways = [0] * (m + 1)
    ways[0] = 1
    for i in range(1, m + 1):
        ways[i] = ways[i - 1]
        if i > 1:
            ways[i] += ways[i - 2]
        if i > 2:
            ways[i] += ways[i - 3]
        if i > 3:
            ways[i] += ways[i - 4]
        ways[i] %= MOD

    #Calculate total ways to build a wall of height n
    totalWays = [pow(ways[i], n, MOD) for i in range(m + 1)]

    #Calculate valid walls
    validWays = [0] * (m + 1)
    validWays[0] = 1
    for width in range(1, m + 1):
        validWays[width] = totalWays[width]
        for k in range(1, width):
            validWays[width] -= validWays[k] * totalWays[width - k]
            validWays[width] %= MOD

    return validWays[m]

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = legoBlocks(n, m)
        print(result)