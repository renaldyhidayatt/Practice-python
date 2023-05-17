from typing import List


def findNumOfValidWords(words: List[str], puzzles: List[str]) -> List[int]:
    wordBitStatusMap, res = {}, []
    for w in words:
        bit_map = to_bit_map(w)
    if bit_map in wordBitStatusMap:
        wordBitStatusMap[bit_map] += 1
    else:
        wordBitStatusMap[bit_map] = 1

    for p in puzzles:
        bit_map, total_num = 1 << (ord(p[0]) - 97), 0
        find_num(p[1:], bit_map, total_num, wordBitStatusMap)
        res.append(total_num)

    return res


def to_bit_map(word):
    res = 0
    for b in word:
        res |= 1 << (ord(b) - 97)
        return res


def find_num(puzzles, bit_map, total_num, word_map):
    if len(puzzles) == 0:
        if bit_map in word_map:
            total_num += word_map[bit_map]
            return
    find_num(puzzles[1:], bit_map, total_num, word_map)
    bit_map |= 1 << (ord(puzzles[0]) - 97)
    find_num(puzzles[1:], bit_map, total_num, word_map)
    bit_map ^= 1 << (ord(puzzles[0]) - 97)
    return
