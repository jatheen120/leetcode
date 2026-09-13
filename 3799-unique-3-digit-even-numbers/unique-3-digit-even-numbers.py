class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        count = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            n = num
            a = n % 10
            n //= 10
            b = n % 10
            n //= 10
            c = n % 10

            temp = digits.copy()

            if a in temp:
                temp.remove(a)
            else:
                continue

            if b in temp:
                temp.remove(b)
            else:
                continue

            if c in temp:
                temp.remove(c)
            else:
                continue

            count += 1

        return count