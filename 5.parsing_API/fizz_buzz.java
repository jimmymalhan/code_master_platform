// fizz buzz

// O(n) time | O(1) space
class fizz_buzz {
    public static void main(String[] args) {
        int i = 1;
        while (i <= 100) {
            if (i % 3 == 0 && i % 5 == 0) {
                System.out.println("FizzBuzz");
            } else if (i % 3 == 0) {
                System.out.println("Fizz");
            } else if (i % 5 == 0) {
                System.out.println("Buzz");
            } else {
                System.out.println(i);
            }
            i++;
        }
    }
}

// javac fizz_buzz.java
// java fizz_buzz
