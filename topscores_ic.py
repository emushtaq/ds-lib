"""
Sort a list of scores (MAX SCORE POSSIBLE: 100) in descending order in O(n)
"""


def sort_scores(unsorted_scores=[], HIGHEST_SCORE=100): 
    # defualt highest possible score is 100
    score_counts = [0] * (HIGHEST_SCORE + 1)

    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []

    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        for occurence in range(count):
            sorted_scores.append(score)

    return sorted_scores


if __name__ == "__main__":
    print(sort_scores([37, 89, 41, 65, 91, 53, 53], 100))