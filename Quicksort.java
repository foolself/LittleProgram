import java.util.*;

class Quicksort {
    public static void main(String[] args) {
        int[] A = new int[]{1,5,3,8,0,21,567,9034,6,2};   //初始化待排序数组
        System.out.print("OK");
        for (int e : A) {
            System.out.print(e + ",");                    //排序前
        }
        QuickSort(A, 0, A.length - 1);                    //排序
        System.out.println("");
        for (int e : A){
            System.out.print(e + ",");                    //排序后
        }
    }

    public static int partition(int[] A, int first, int end) {
        int i = first;
        int j = end;
        int temp;
        while (i < j) {
            while (i < j && A[i] <= A[j]) j--;
            if (i < j) {
                 temp = A[i];
                 A[i] = A[j];
                 A[j] = temp;
                 i++;
            }
            while (i < j && A[i] <= A[j]) i++;
            if (i < j) {
                 temp = A[i];
                 A[i] = A[j];
                 A[j] = temp;
                 j--;                 
            } 
        }
        return i; 
    }

    public  static void QuickSort(int[] A, int first, int end) {
        int pivot;
        if (first < end) {
            pivot = partition(A, first, end);
            QuickSort(A, first, pivot - 1);
            QuickSort(A, pivot + 1, end);
        }
    }
}