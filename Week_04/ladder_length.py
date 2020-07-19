from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set_is_invalid = True
        length = len(endWord)

        trans_map = defaultdict(list)
        for word in wordList:
            if endWord == word: set_is_invalid = False
            for i in range(length):
                trans_map[word[: i] + "*" + word[i + 1:]].append(word)
        if set_is_invalid: return 0

        step_queue = [(beginWord, 1)]
        visited = {beginWord}
        while step_queue:
            curr_word, step = step_queue.pop(0)
            for i in range(length):
                new_word = curr_word[: i] + "*" + curr_word[i + 1:]
                for trans_word in trans_map[new_word]:
                    if trans_word == curr_word or trans_word in visited: continue
                    if trans_word == endWord: return step + 1
                    step_queue.append((trans_word, step + 1))
                    visited.add(trans_word)

        return 0