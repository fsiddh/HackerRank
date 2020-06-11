# Method 1:

    n = int(input())
    if 2 <= n <= 10:
        pass
    l = list(map(int, input().split()))
    for i in l:
        if -100 <= i <= 100:
            pass
    l.sort()
    l_s = set(l)
    l1 = list(l_s)
    updated_list = sorted(l1)
    print(updated_list[-2], end="")

# Method 2:- 

    scores_list = list()

    score_no = int(input())
    scores = input().split()

    for i in scores:
        scores_list.append(int(i))

    scores_list.sort()
    max_score = max(scores_list)
    index_max_score = scores_list.index(max_score)

    print(scores_list[index_max_score-1])

