s = set()

elements_no = int(input())
elements = input().split()
s_set = set(map(int, elements))

functions_no = int(input())
for i in range(functions_no):
    functions_element = input().split()

    if len(functions_element) == 2:

        function = functions_element[0]
        element = int(functions_element[1])

        if function == 'remove':
            s_set.remove(element)
        if function == 'discard':
            s_set.discard(element)

    else:
        if functions_element[0] == 'pop':
            s_set.pop()

print(sum(s_set))

