def find_pattern_indexes(string, pattern):
    pattern_indexes = []
    i = 0
    while i < len(string):
        if string[i:i+len(pattern)] == pattern:
            pattern_indexes.append(i)
            i += len(pattern)
        else:
            i += 1
    return pattern_indexes

# Sample input
string = "abaaababbbbaaabbabababababbbaaaaabababababbbbb"
pattern = "abb"

# Output
print(find_pattern_indexes(string, pattern)) # [6, 13, 24, 40]
