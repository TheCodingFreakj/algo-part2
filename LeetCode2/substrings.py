
def are_all_characters_unique(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        seen.add(char)
    return True


def longest_substring(s, first, second, string_l0, longest_string, results, index):

    n = len(s)

    # if (are_all_characters_unique(s) and len(s)>2 and len(s)<5):
    #     for i in range(len(s)):
    #         results.append(s[i])
    #     return results
    if (len(longest_string) == 1 and index == n):
        return
    if (len(s) == 3 and s[0] == s[1] and s[1] != s[2]):
        longest_string = s[1]
        results.append(longest_string)
        longest_string = s[2]
        results.append(longest_string)
        return results

    if (len(s) == 3 and s[0] == s[1] == s[2]):
        longest_string = s[1]
        results.append(longest_string)
        return results

    if (len(s) == 2 and s[0] != s[1]):
        longest_string = s[0]
        results.append(longest_string)
        longest_string = s[1]
        results.append(longest_string)
        return results

    if (len(s) == 2 and s[0] == s[1]):
        longest_string = s[0]
        results.append(longest_string)
        return results

    if (index == n):
        first = first + 1
        longest_substring(s, first, first, '', '', results, 0)

    if (second == n):
        first = first + 1
        longest_substring(s, first, first, '', '', results, 0)

    if (index < n):

        if (second >= n):
            return results

        if (second < n):
            to_be_seen = s[second+1:] or ''

            if s[second] not in string_l0:
                string_l0 = string_l0 + s[second]
                second = second+1
                longest_string = string_l0

                if string_l0 in s:
                    longest_string = string_l0
                    results.append(longest_string)

                if (to_be_seen != ''):
                    if (s[second] not in to_be_seen):
                        string_l0 = string_l0 + s[second]
                        second = second+1
                        longest_string = string_l0
                        if (to_be_seen != ''):
                            if string_l0 in s:
                                longest_string = string_l0
                                results.append(longest_string)

            else:
                second = second+1

        index = index+1

    longest_substring(s, first, second, string_l0,
                      longest_string, results, index)
    print(results)
    return max(results, key=len)


s = "eapiahdrjgtgyurbfhzlfsjmucymimwmonupuxideblevcfdkhorbzevecjmrfzfutworhtxiebgjijtrzksbqpfvzrmgqtb"
results = []
def longest_substring_without_repeating(s: str) -> str:
    n = len(s)
    longest_substring = ""
    start = 0
    char_index_map = {}

    for i in range(n):
        if s[i] in char_index_map and char_index_map[s[i]] >= start:
            start = char_index_map[s[i]] + 1
        else:
            if i - start + 1 > len(longest_substring):
                longest_substring = s[start:i+1]
        char_index_map[s[i]] = i

    return longest_substring
if (len(s) > 10):
   print(longest_substring_without_repeating(s))
else:    
   print(longest_substring(s, 0, 1, s[0], '', results, 0))
