import sys
import collections
from typing import List

input= sys.stdin.readline
li = ["eat","tea","tan","ate","nat","bat"]

def group(strs: List[str])-> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    print(anagrams)
    return list(anagrams.values())


result = group(li)
print(result)
