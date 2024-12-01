// Binet's Formula to find nth fibonacci number => f(n) = (((1 + sqrt(5))/2)^n)/sqrt(5)
class Solution {
    public int fib(int n) {
        double phi = (1 + Math.sqrt(5)) / 2;
        return (int) Math.round(Math.pow(phi, n) / Math.sqrt(5));
    }
}
