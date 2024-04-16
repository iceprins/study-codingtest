package codingTest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class baekjoon_9935 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String basic = br.readLine();
        String explode = br.readLine();

        Stack<Character> st = new Stack<>();

        for (int i = 0; i < basic.length(); i++) {
            st.push(basic.charAt(i));

            if (st.size() >= explode.length()) {
                boolean flag = true;

                for (int j = 0; j < explode.length(); j++) {
                    if (st.get(st.size() - explode.length() + j) != explode.charAt(j)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) {
                    for (int j = 0; j < explode.length(); j++) {
                        st.pop();
                    }
                }
            }
        }
        StringBuilder ans = new StringBuilder();

        for (Character c : st) {
            ans.append(c);
        }

        if (ans.length() == 0)
            System.out.println("FRULA");
        else
            System.out.println(ans);
    }
}
