setA = set()
setB = set()
result = list()

test_cases = int(input())

for i in range(test_cases):
    setA_no = int(input())
    setA = set(map(int, input().split()))

    setB_no = int(input())
    setB = set(map(int, input().split()))

    if setA.issubset(setB):
        result.append('True')
    else:
        result.append('False')

for r in result:
    print(r)