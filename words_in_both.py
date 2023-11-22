def words_in_both(str1, str2):
    words1 = set(str1.lower().split())
    words2 = set(str2.lower().split())

    common_words = words1.intersection(words2)

    return common_words

str1 = "She is a jack of all trades"
str2 = "Jack was tallest of all"
result = words_in_both(str1, str2)

