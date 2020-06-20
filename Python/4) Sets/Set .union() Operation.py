english_students_no = int(input())
english_set = set(map(int, input().split()))

french_students_no = int(input())
french_set = set(map(int, input().split()))

result = english_set.union(french_set)
print(len(result))