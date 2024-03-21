class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1, n+1)]

        for i in range(len(answer)):
            if int(answer[i]) % 15 == 0:
                answer[i] = "FizzBuzz"
            elif int(answer[i]) % 5 == 0:
                answer[i] = "Buzz"
            elif int(answer[i]) % 3 == 0:
                answer[i] = "Fizz"

        return answer
