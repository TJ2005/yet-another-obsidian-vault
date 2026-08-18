instead of Stack

Array dequeue is faster more modern


Resizable Circular Array


Head ++ to remove element
#### Arrays

Array dequeue


## When

- Linked list 
	- Multiple entries
	- Multiple Deletion
- Arrays
	- Multiple reads
- Stacks & Queue
	- array dequeue 
	- Circular dynamic array


### Arrays

```java
public class ArrayExamples {

    public static void main(String[] args) {

        // -------------------------------
        // 1D Array
        // -------------------------------
        int arr1D[] = new int[5];

        arr1D[0] = 10;
        arr1D[1] = 20;
        arr1D[2] = 30;
        arr1D[3] = 40;
        arr1D[4] = 50;

        System.out.println("1D Array:");
        for (int i = 0; i < arr1D.length; i++) {
            System.out.print(arr1D[i] + " ");
        }

        // -------------------------------
        // 2D Array
        // -------------------------------
        int arr2D[][] = {
            {1, 2, 3},
            {4, 5, 6}
        };

        System.out.println("\n\n2D Array:");
        for (int i = 0; i < arr2D.length; i++) {
            for (int j = 0; j < arr2D[i].length; j++) {
                System.out.print(arr2D[i][j] + " ");
            }
            System.out.println();
        }

        // -------------------------------
        // 3D Array
        // -------------------------------
        int arr3D[][][] = {
            {
                {1, 2},
                {3, 4}
            },
            {
                {5, 6},
                {7, 8}
            }
        };

        System.out.println("\n3D Array:");
        for (int i = 0; i < arr3D.length; i++) {
            for (int j = 0; j < arr3D[i].length; j++) {
                for (int k = 0; k < arr3D[i][j].length; k++) {
                    System.out.print(arr3D[i][j][k] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }

        // ------------------------------------------
        // 2D Array with Different Sized Arrays
        // (Jagged Array / Multi-sized Array)
        // ------------------------------------------
        int jagged[][] = new int[3][];

        jagged[0] = new int[] {1, 2};
        jagged[1] = new int[] {3, 4, 5, 6};
        jagged[2] = new int[] {7};

        System.out.println("Jagged 2D Array:");
        for (int i = 0; i < jagged.length; i++) {
            for (int j = 0; j < jagged[i].length; j++) {
                System.out.print(jagged[i][j] + " ");
            }
            System.out.println();
        }
    }
}
```


```java
public class Main {
    public static void main(String[] args) {

        int x[][][] = new int[2][1][3];

        // Assigning values
        x[0][0][0] = 10;
        x[0][0][1] = 20;
        x[0][0][2] = 30;

        x[1][0][0] = 40;
        x[1][0][1] = 50;
        x[1][0][2] = 60;

        // Printing values
        for (int i = 0; i < x.length; i++) {

            for (int j = 0; j < x[i].length; j++) {

                for (int k = 0; k < x[i][j].length; k++) {

                    System.out.print(x[i][j][k] + " ");
                }

                System.out.println();
            }

            System.out.println();
        }
    }
}cm
```