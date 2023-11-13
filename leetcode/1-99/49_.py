from collections import defaultdict


def groupAnagrams(strs):
    record = defaultdict(list)

    for s in strs:
        s_key = "".join(sorted(s))

        record[s_key].append(s)

    return list(record.values())
