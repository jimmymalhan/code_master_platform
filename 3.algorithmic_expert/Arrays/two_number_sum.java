public class two_number_sum {
    public static int[] twoNumberSum(int[] array, int targetSum) {
        int[] result = new int[2];
        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] + array[j] == targetSum) {
                    result[0] = array[i];
                    result[1] = array[j];
                    return result;
                }
            }
        }
        return result;
    }
// main method
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        int target = 15;
        int[] result = twoNumberSum(arr, target);
        System.out.println(result[0] + " " + result[1]);
    }
}

// javac two_number_sum.java
// java two_number_sum