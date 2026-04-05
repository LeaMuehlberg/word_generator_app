public class vollkommen {
    public static void main(String[] args) {
        System.out.println(vollkommen(28));
    }

    public static boolean vollkommen(int n) {
        int result = 0;
        int i = 1;
        while(result <= (n / 2)) {
            if (n % i == 0) {
                result += i;
            }
            i++;
        }
        if (result != n) {
            return false;
        } else {
            return true;
        }
    }
}
