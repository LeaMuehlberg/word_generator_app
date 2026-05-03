import java.util.ArrayList;

public class selectionsort {
    public static void main(String[] args) {
        ArrayList<Integer> l = new ArrayList<>();
        ArrayList<Integer> arr = new ArrayList<>();
        for (int num : new int[]{34, 2, 7, 45}) {
            arr.add(num);
        }
        l = SelectionSort(arr);
        System.out.println(l);
    }
    
    public static ArrayList SelectionSort(ArrayList<Integer> arr) {
        ArrayList<Integer> newArr = new ArrayList<>();
        while (arr.size() > 0) {
            int smallest = findSmallest(arr);
            int smallest_index = findSmallestIndex(arr);
            newArr.add(smallest);
            arr.remove(smallest_index);
        }
        return newArr;
    }

    public static int findSmallest(ArrayList<Integer> arr) {
        int smallest = arr.get(0);
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < smallest) smallest = arr.get(i);
        }
        return smallest;
    }

    public static int findSmallestIndex(ArrayList<Integer> arr) {
        int smallest = arr.get(0);
        int smallest_index = 0;
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) < smallest) {
                smallest = arr.get(i);
                smallest_index = i;
            }
        }
        return smallest_index;
    }
}
