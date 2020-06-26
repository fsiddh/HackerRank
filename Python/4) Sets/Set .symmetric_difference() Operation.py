eng_students = int(input())
eng_students_list = set(map(int, input().split()))

french_students = int(input())
french_students_list = set(map(int, input().split()))

result = (eng_students_list.union(french_students_list)) - (eng_students_list.intersection(french_students_list))
print(len(result))