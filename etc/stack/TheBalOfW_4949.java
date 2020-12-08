package etc.stack;
import java.io.*;
import java.util.*;


public class TheBalOfW_4949{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new
        InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new
        OutputStreamWriter(System.out));
        
        while(true){
            String input = br.readLine();
            if(input.equals(".")){//
                bw.flush();
                bw.close();
                return;
            }
            bw.write(balance(input));
        }
    }

    static String balance(String input)
    {
        Stack<Character> stack = new Stack<>();
        boolean result = true;
        for(char one:input.toCharArray())// 범위기반
        {
            if(one == '(' || one == '['){ 
                stack.push(one);
            }else if(one==')'){
                if(stack.isEmpty()||stack.pop()!='('){
                    result=false;
                    break;
                }
            }else if(one==']'){
                if(stack.isEmpty()||stack.pop()!='['){
                    result=false;
                    break;
                }
            }
        }

        if(!stack.isEmpty()){
            result=false;
        }
        return result?"yes\n":"no\n";
    }


}