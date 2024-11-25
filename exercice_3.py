def longuest_unique_substring(string) :
    n = len(string)
    res = 0

    for i in range(n):
        visited_chars = [False] * 256

        for j in range(i, n):
            if visited_chars[ord(string[j])] :
                break
            else:
                res = max(res, j - i + 1)
                visited_chars[ord(string[j])] = True

    return res

# print(longuest_unique_substring("aaeeiigg"))
# print(longuest_unique_substring("aeig"))