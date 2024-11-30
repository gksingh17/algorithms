# get the longest palindromic substring
# idea is to treat every character as the center and
# move two pointers in opposite directions, checking if the string is a palindrome and updating max
# for odd characters it will be one character ahead


def longest_palidromic_subtstring(s):
    result = ""  # return string
    reslen = 0  # to check length

    for i in range(len(s)):
        left = i
        right = i
        # both pointers go in opposite directions and check if it's a palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > reslen:

                result = s[left: right + 1]  # substring
                reslen = right - left + 1
            left -= 1
            right += 1

        left = i
        right = i + 1  # odd number of chars
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > reslen:
                result = s[left: right + 1]  # substring
                reslen = right - left + 1
            left -= 1
            right += 1
    return result


s = "babad"
print(longest_palidromic_subtstring(s))
