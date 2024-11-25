// Recursive Approach

class Solution {
    public void reverseString(char[] s) {
        recursiveReverse(s, 0, s.length - 1);
    }

    char[] recursiveReverse(char[] s, int l, int r) {
        if (l > r) {
            return s;
        }

        char temp = s[l];
        s[l] = s[r];
        s[r] = temp;

        return recursiveReverse(s, ++l, --r);
    }
}
