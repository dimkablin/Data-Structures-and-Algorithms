class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        count = [0] * (n + 1)

        # Применение изменений сдвигов
        for start, end, direct in shifts:
            if direct == 0:
                direct = -1
            count[start] += direct
            if end + 1 < n:
                count[end + 1] -= direct

        # Накопление изменений
        current_shift = 0
        result = []

        for i in range(n):
            current_shift += count[i]
            # Применение текущего сдвига к символу
            new_char = chr((ord(s[i]) - ord('a') + current_shift) % 26 + ord('a'))
            result.append(new_char)

        return ''.join(result)
