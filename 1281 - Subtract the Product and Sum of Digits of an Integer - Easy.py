class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        sumOfDigits = 0
        productOfDigits = 1
        for i in n:
            sumOfDigits += int(i)
            productOfDigits *= int(i)

        return productOfDigits - sumOfDigits
