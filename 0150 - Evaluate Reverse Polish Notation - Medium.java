class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack = new Stack<>();

        for (String token: tokens) {
            if (isOperator(token)) {
                int a = stack.pop();
                int b = stack.pop();

                switch(token) {
                    case "+": stack.push(b + a); break;
                    case "-": stack.push(b - a); break;
                    case "/": stack.push(b / a); break;
                    case "*": stack.push(b * a); break;
                }
            } else {
                stack.push(Integer.parseInt(token));
            }

        }

        return stack.pop();
    }

    public boolean isOperator(String token) {
        return token.equals("+") || token.equals("-") || token.equals("/") || token.equals("*");
    }
}
