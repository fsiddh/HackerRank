eng_studs = int(input())
roll_no_eng_studs = set(map(int, input().split()))

french_studs = int(input())
roll_no_french_studs = set(map(int, input().split()))

result = roll_no_eng_studs.intersection(roll_no_french_studs)
print(len(result))
