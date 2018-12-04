# Dakota Bourne (db2nb)
"""
assignment is designed to take any new assignment, with a grade, and figure out if it is in a category that is put into
an overall dictionary, and if so it will put the grade with respective weight into a list for that category.
total is designed to take the proportions of each category, and calculate the overall grade based on the weight of each
category, by the average score of each category.
"""
scores_dict = {}


def assignment(kind, grade, weight=1):
    global scores_dict
    i = 0
    if 0 <= grade <= 100:
        if kind not in scores_dict.keys():
            scores_dict[kind] = []
        if kind in scores_dict.keys():
            while weight != i:
                scores_dict[kind].append(grade)
                i += 1


def total(proportions):
    global scores_dict
    n = 0
    total_scores = 0
    total_scores_per_lst = 0
    proportion_total = 0
    for key in scores_dict.keys():
        for scores in scores_dict[key]:
            n += 1
            if n == 1:
                total_scores_per_lst = scores
            else:
                total_scores_per_lst += scores
        if key not in proportions.keys():
            total_scores_per_lst = 0
        else:
            average_score = (total_scores_per_lst / n)
            total_scores += (average_score * proportions[key])
            proportion_total += proportions[key]
        n = 0
    total_scores /= proportion_total
    return total_scores
