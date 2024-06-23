class Solution:
    def equalFrequency(self, word: str) -> bool:
        table = {c: 0 for c in word}
        for c in word:
            table[c] += 1

        freqs = list(table.values())
        freqs_set = set(freqs)
        for freq in freqs_set:
            new_freqs = freqs.copy()
            new_freqs.remove(freq)

            if freq - 1 > 0:
                new_freqs.append(freq - 1)

            if len(set(new_freqs)) == 1:
                return True

        return False
