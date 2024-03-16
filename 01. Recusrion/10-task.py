strings = input().split(', ')
target = list((input()))
words_by_idx = {}
words_count = {}
output = []

for idx in range(len(target)):
    substring = ''

    for char in target[idx:]:
        substring += char
        if substring in strings:
            target_idx = ''.join(target).index(substring, idx)
            if target_idx not in words_by_idx:
                words_by_idx[target_idx] = []
            if substring not in words_by_idx[target_idx]:
                words_by_idx[target_idx].append(strings[strings.index(substring)])

for string in strings:
    if string not in words_count:
        words_count[string] = 0
    words_count[string] += 1


def find_patterns(idx, target, words_by_idx, words_count, used_words):

    if idx >= len(target):
        print(' '.join(used_words))
        return

    if idx not in words_by_idx:
        return

    for word in words_by_idx[idx]:
        used_words.append(word)
        words_count[word] -= 1

        find_patterns(idx + len(word), target, words_by_idx, words_count, used_words)

        used_words.pop()
        words_count[word] += 1


find_patterns(0, target, words_by_idx, words_count, [])
