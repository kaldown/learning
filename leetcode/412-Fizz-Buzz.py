class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        def convert(i):
            if not i % 15:
                return "FizzBuzz"
            elif not i % 5:
                return "Buzz"
            elif not i % 3:
                return "Fizz"
            else:
                return str(i)
        result = []
        for num in range(1, n+1):
            result.append(convert(num))
        return result
