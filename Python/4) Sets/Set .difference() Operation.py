eng_students = int(input())
eng_students_list = set(map(int, input().split()))

french_students = int(input())
french_students_list = set(map(int, input().split()))

result = eng_students_list.difference(french_students_list)
print(len(result))