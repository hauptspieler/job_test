from collections import Counter
giv_list = ["f", "f", "s", "c", "s", "u", "u", "a ", "t", "l", "h ", "m ", "a", "e", "r", "e", "m", "@", "r", "t", "i", "u", "f", "h", "o",
            "a ", "u ", "e", "r", "f", "m", "o", "r", "c ", "a", "s ", "@", "m", "e", "o", "u ", "u", "u ", "a ", "@", "@", "e", "e", "a",
            "m", "s", "e", "s", "u", "c", "@", "c", "m", "h", "t", "h ", "t ", "a", "h", "a ", "@", "o", "t ", "o", "i", "a ", "m", "h", "a",
            "f", "i", "r", "@", "a", "h", "t", "e", "s", "l", "h ", "i", "h", "a", "u", "a", "h", "u ", "t",
            "c", "@", "s", "r", "@", "e", "a", "c", "u ", "m", "@", "m", "a", "f", "c", "a", "m", "i", ".", "m", "@", "m", "o", "@", "u", "s",
            "s", "c", "s ", "u", "t", "t ", "c", "m", "u", "m", "c", "t", "t ", "u", "t ", "f", "a ", "c",
            "t", "a", "r", "@", "t", "m", "m", "u", ".", "e", "u ", "c ", "i", "a ", "@", "u ", "a", "l", "a", "@", "f", "f", "t",
            "o", "t", "u", "o", "r", "u", "t", "u", "t", "e", "p", "c ", "s", "u", "s", "t", "h ", "o ", "h", "s ", "h ", "u",
            "e", "s", "m", "t ", "h ", "s", "u", "u", "o", "a", "s", "c", "l", "o ", "c ", "s", "s ", "s", "a", "u ", "h", "a",
            "f", "h", "@", "o", "u ", "p", "h", "t", "c", "e", "a", "c", "o", "a", "h", "u", "s", "m", "h ", "u", "a",
            "m", "a", "r", ".", "h", "s", "t ", "u", "h", "c", "s ", "c", "r", "h ", "c", "s", "u", "s", "f", "m", "h", "l", "c ", "t", "u",
            "t", "c ", "u ", "c ", "a", "s", "e", "m", "s ", "c", "a", "f", "f", ".", "e", "h", "m", "r", "i", "u",
            "e", "a", "t", "r", "m", "o", "t ", "c", "m", "s ", "f", "c ", "a", "m", "a ", "s", "t", "s", "u",
            "t", "p", "m", "l", "o", "p", "m", "h ", "i", "l", "c", "s ", "r", "h ", "p", "h", "a ", "c ", "o", "e", "h", "t", "u",
            "e", "o", "i", "h", "s ", "s ", "u", "s", "l", "s", "a ", "c", "a ", "t ", "t", "a ", "h", "h ", "u", "t", "t",
            "c", "t", "u", "@", "f", "o", "s", "t ", "r", "h ", "f", "a", "t", "f", "@", "u", "c", "e"]

# printing given list
print("given list", str(giv_list))

# sorting on bais of frequency of elements in descending order
result = [item for items, c in Counter(giv_list).most_common()
          for item in [items] * c]

result.sort(reverse=True)

# printing final result
print("final list", str(result))
