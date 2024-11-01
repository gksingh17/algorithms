from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    # need to group the words with same count of chars
    # use dictionary, use the sorted version of word as Key
    # add the word if the sorted version matches with the key present in dict
    anagrams = {}

    for word in strs:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams:
            # if key of sorted word already exists, group new anagram
            anagrams[sorted_word].append(word)
        else:
            # create new group
            anagrams[sorted_word] = [word]

    return anagrams.values()


def group_anagrams_defaultdict(strs: list[str]) -> list[list[str]]:
    # we can use a defaultdict to group the count of chars in each iteration
    # {(1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['act', 'cat']}
    result = defaultdict(list)
    for string in strs:
        count = [0] * 26  # key is count appereance of each char
        for char in string:
            count[ord(char) - ord('a')] += 1
        result[tuple(count)].append(string)

    return result.values()


strs = ["act", "pots", "tops", "cat", "stop", "hat"]
print(group_anagrams(strs))
print(group_anagrams_defaultdict(strs))
