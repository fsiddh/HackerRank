def tuple_hash(n):
    t = tuple(map(int, input().split()))
    result = hash(t)
    return result


n = int(input())
result = tuple_hash(n)
print(result)
