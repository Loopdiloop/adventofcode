
import java.io.*;


public class day01 {
    public static void main(String[] args) throws FileNotFoundException, IOException {
      
      File file = new File("/home/linuxloop/advent/adventofcode/2023/input/01_test2.txt");
      String testinput = "two1nine";

      String[] numberString = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};

      int sum = 0;

      //List<String> processedLines = new ArrayList<String>();

      //System.out.println(file.exists());

      FileReader reader = new FileReader(file);
      BufferedReader br = new BufferedReader(reader);
      String st;

      while ((st = br.readLine()) != null) {
        System.out.println(st);
        
        for (int i = 0; i < 10; i++) {
          //System.out.println(numberReplacements[i].charAt(0)); // As char!
          String number = numberString[i];
          //System.out.println(number.substring(0,1)); // As string!
          //System.out.println(number.substring(number.length()-1));
          st = st.replace(number, number.substring(0,1)+String.valueOf(i)+number.substring(number.length()-1));
        }
        System.out.println(st);
        
        st = st.replaceAll("[^\\d.]", "");
        System.out.println(st);
        sum += Integer.valueOf(st.substring(0,1)) + Integer.valueOf(st.substring(st.length()-1, st.length()));
        
        //System.out.println(Integer.valueOf(st.substring(0,1)));
        //System.out.println(Integer.valueOf(st.substring(st.length()-1, st.length())));
        
      }
      /*for (int j = 0; j < testinput.length()+1; j++) {
      testinput = testinput.replaceAll("[^\\d.]", "");
      
      
      sum = Integer.valueOf(testinput.substring(0,1)) + Integer.valueOf(testinput.substring(testinput.length()-1, testinput.length()));
      //}
      */
      System.out.println(testinput);
      System.out.println(sum);
      
    }
  }

