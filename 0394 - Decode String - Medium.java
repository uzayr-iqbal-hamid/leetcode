class Solution {
    public String decodeString(String s) {
        Stack<Integer> number = new Stack<>();
        Stack<StringBuilder> chars = new Stack<>();

        StringBuilder sb = new StringBuilder();

        int num = 0;

        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                num = num * 10 + (c - '0');
            } else if (c == '[') {
                number.push(num);
                num = 0;
                chars.push(sb);
                sb = new StringBuilder();
            } else if (c == ']') {
                int k = number.pop();
                StringBuilder temp = sb;
                sb = chars.pop();
                while (k-- > 0) {
                    sb.append(temp);
                }
            } else {
                sb.append(c);
            }
        }

        return sb.toString();
    }
}
