public class factorial {
    public static void main(String[] args) {
        int x = factorial(5);
        System.out.println(x);
    }

    public static int factorial(int number) {
        if (number <= 1) return 1;
        return number * factorial(number - 1);
    }

    public static int it_factorial(int n) {
        int result = 1;
        if (n == 0) return 1;
        for (int i = n; i > 0 ; i--) {
            result = result * i;
        }
        return result;
    }
}