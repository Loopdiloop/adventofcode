
import java.io.*;


public class day01 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
      
      File file = new File("/home/linuxloop/advent/adventofcode/2023/input/01.txt");

      String[] numberString = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
      int sum = 0;

      FileReader reader = new FileReader(file);
      BufferedReader br = new BufferedReader(reader);
      String st;

      while ((st = br.readLine()) != null) {

        for (int i = 0; i < 10; i++) {
          String number = numberString[i];
          st = st.replace(number, number.substring(0,1)+String.valueOf(i)+number.substring(number.length()-1));
        }
        
        st = st.replaceAll("[^\\d.]", "");
        sum += Integer.valueOf(st.substring(0,1) + st.substring(st.length()-1, st.length()));
      }
      System.out.println(sum);
    }
  }

