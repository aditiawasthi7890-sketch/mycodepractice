//methods 

/*
public class main {
    static void greet() {
        System.out.println("hello! welcome to java.");
    }
    public static void main(String[]arg
        greet();
    }
}*/
/*
public class main {
    static int add(int a, int b){
        return a+b;
    }
    public static void main(String[]args){
        int result = add(5,7);
        System.out.println("sum="+  result);}
}*/
/*
public class main{
    static String getMessage(){
        return "java is awesome!";
    }
    public static void main(String[]args){
        String msg = getMessage();
        System.out.println(msg);  }
}*/
//copying
// int[]src= {1,2,3,4,5};
// int[]clone=src.clone();
//int[]first3= java.util.Arrays.copyOf(src,3);
//int[]mid=java.util.Arrays.copyOfRange(src, 1, 4);
//system.arraycopy(src,1,clone,0,3);

  /*public class main{
    public static void main(String[]args){
        int[] arr = { 5,2,9,1,5};

        Arrays.sort(arr);

        System.out.println("Sorted array :" + Arrays.toString(arr) );

        int pos = Arrays.binarySearch(arr , 5);
        System.out.println("position of 5 in the sorted array : " + pos);
    }
  }*/
//jagged array exmple
/* public class main{
    public static void main(String[]args){
        //creating jagged array with 3 rows
        int [][] jag = new int[3][];
        //initialising each row with different sizes
        jag[0] = new int[]{1,2,};
        jag[1] = new int[]{3,4,5};
        jag[2] = new int[]{6};

        //printing the jagged array 
        System.out.println("jagged Array Element:");
        for (int i = 0; i < jag.length; i++){
            for (int j = 0; j< jag[i].length; j++){
                System.out.println(jag[i][j] + " ");
            }
            System.out.println();
        }   
        
     }
 }*/

/*public class main{
    public static void main(String[]args){
        // declare and intialize a 2D array
        int[][] grid = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };
        // print element using nested for loop
        System.out.println("2D Array Element:");
        for (int i = 0; i < grid.length; i++){
            for (int j = 0; j < grid[i].length; j++){
                System.out.print(grid[i][j] + " ");
            
            }
            System.out.println();
        }
    }
}*/
/*public class main{
    //methhod to calculate sum of given row
    public static int rowSum(int[][] m, int r){
        int sum = 0;
        for (int j = 0; j <m[r].length; j++){
            sum += m[r] [j];

        }
        return sum;
    }
    //method to calculate sum of given column
    public static int colSum(int[][] m, int c){
        int sum = 0;
        for (int i = 0; i < m.length; i++){
            sum += m[i][c];
        }
        return sum;
    }

    public static void main(String[]args){
        //exmple 2d array
        int[][] matrix = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };
    
    //chosse a new row and column 
    int rowIndex = 2; //second row
    int colIndex = 2; //third colmn

    //calculate and print results
    System.out.println("sum of row" + rowIndex + "=" + rowSum(matrix , rowIndex));
    System.out.println("sum of column" + colIndex + "=" + colSum(matrix , colIndex));
}}*/
/*
public class main{
// method to transpose a square matrix in place 

public static void transposeSquare(int[][] m){
    for (int i = 0 ; i<m.length; i++){
        for (int j = i +1; j<m[0].length; j++){
            int t = m[i][j];
            m[i][j] = m[j][i];
            m[j][i] = t;
        }
    }
}
// method to print a 2d matrix 
public static void printMatrix(int[][] m){
    for (int[] row : m){
        for (int val : row){
            System.out.print(val + "");
     }
     System.out.println();
    }

}

public static void main(String[]args){

    int[][] matrix = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };
    System.out.println("Original Matrix:");
    printMatrix(matrix);

    transposeSquare(matrix);

    System.out.println("\nTransposed Matrix:");
    printMatrix(matrix);
}
}*/
/*
public class main{

    // Method to transpose a matrix and return a new matrix
    public static int[][] transpose(int[][] m) {
        int R = m.length;      // number of rows
        int C = m[0].length;   // number of columns
        int[][] t = new int[C][R];  // transposed matrix (C x R)

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                t[j][i] = m[i][j];
            }
        }
        return t;
    }

    // Method to print a matrix
    public static void printMatrix(int[][] m) {
        for (int[] row : m) {
            for (int val : row) {
                System.out.print(val + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        // Example: 2x3 matrix
        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6}
        };

        System.out.println("Original Matrix:");
        printMatrix(matrix);

        // Transpose and store in a new matrix
        int[][] transposed = transpose(matrix);

        System.out.println("\nTransposed Matrix:");
        printMatrix(transposed);
    }
}*/
   //OOPS CONCEPT
   /*public class main{
 {
    String brand;
    int speed;

    Car(String brand, int speed) {
        this.brand = brand;
        this.speed = speed;
    }

    void display() {
        System.out.println(brand + " is running at " + speed + " km/h");
    }
}

 public class Main 
   public static void main(String[] args) 
         Car car1 = new Car("Honda", 60)
         car1.display();
     }
}
} */


/*import java.util.ArrayList;

public class main {
    public static void main(String[] args) {
        ArrayList<String> fruits = new ArrayList<>();

        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        System.out.println("Fruits: " + fruits);

        fruits.remove("Banana");
        System.out.println("After removing Banana: " + fruits);

        if (fruits.size() > 2) {
            System.out.println("Fruit at index 2: " + fruits.get(2));
        } else {
            System.out.println("Index 2 not available, current size: " + fruits.size());
        }

        System.out.println("Total fruits: " + fruits.size());
    }
}*/


/*import java.util.ArrayList;
import java.util.Collections;

public class main {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);
        nums.add(5);

        System.out.println("Original List: " + nums);

        int k = 2;

        Collections.rotate(nums, k);
        System.out.println("Right Rotated by " + k + " steps: " + nums);

    }
}*/
    
//LINKED LIST  singly linked list 
// class node {
//     int data;
//     node next;

//     public node(int data) {
//         this.data = data;
//         this.next = null;
//     }
// }
// public class main {
//     node head;

//     public void insert(int data) {
//         node newNode = new node(data);
//         if (head == null) {
//             head = newNode;
//         } else {
//             node current = head;
//             while (current.next != null) {
//                 current = current.next;
//             }
//             current.next = newNode;
//         }
//     }

//     public void display() {
//         node current = head;
//         while (current != null) {
//             System.out.print(current.data + " ");
//             current = current.next;
//         }
//         System.out.println();
//     }

//     public static void main(String[] args) {
//         main list = new main();
//         list.insert(1);
//         list.insert(2);
//         list.insert(3);
//         list.display(); 
//     }
// }

//doubly linked list


// class Node {
//     int data;
//     Node next;
//     Node prev;

//     public Node(int data) {
//         this.data = data;
//         this.next = null;
//         this.prev = null;
//     }
// }

// class CircularDoublyLL {
//     Node head;

//     void insert(int data) {
//         Node newnode = new Node(data);

//         if (head == null) {
//             head = newnode;
//             newnode.next = head;
//             newnode.prev = head;
//             return;
//         }

//         Node tail = head.prev;
//         tail.next = newnode;
//         newnode.prev = tail;
//         newnode.next = head;
//         head.prev = newnode;
//     }

//     void display() {
//         if (head == null) {
//             System.out.println("list is empty");
//             return;
//         }

//         Node current = head;
//         do {
//             System.out.print(current.data + " ");
//             current = current.next;
//         } while (current != head);

//         System.out.println();
//     }
// }

// public class main {
//     public static void main(String[] args) {
//         CircularDoublyLL list = new CircularDoublyLL();
//         list.insert(1);
//         list.insert(2);
//         list.insert(3);
//         list.display();
//     }
// }




// class Node {
//     int data;
//     Node left;
//     Node right;

//     Node(int data) {
//         this.data = data;
//         left = right = null;
//     }
// }

// class BinaryTree1 {
//     Node root;

//     void inorder(Node node) {
//         if (node == null)
//             return;

//         inorder(node.left);
//         System.out.print(node.data + " ->");
//         inorder(node.right);
//     }
// }

// public class main {   
//     public static void main(String[] args) {
//         BinaryTree1 tree = new BinaryTree1();
//         tree.root = new Node(798);
//         tree.root.left = new Node(78);
//         tree.root.right = new Node(3);
//         tree.root.left.left = new Node(45);
//         tree.root.left.right = new Node(5);

//         System.out.println("Inorder traversal of binary tree:");
//         tree.inorder(tree.root);
//     }
// }

/*import java.util.*;
public class TicketManager {
    private ArrayList<Ticket> tickets = new ArrayList<>();
    private int maxSeat = 10;
    private int nextTicketId ;

    public void bookTicket(String passengerName, int age, String from , String to){}
    if(tickets.size() >= maxSeat){
        System.out.println("no seats available.");
        return;
    }
    int seatno = tickets.size() + 1;
    Ticket newTicket = new Ticket(nextTicketId++, passengerName, age, from, to, seatno);
    tickets.add(newTicket);
    System.out.println("Ticket booked successfully! Ticket ID: " + newTicket.getTicketId());
}*/
// public class ReverseString {
//     public static void reverse(char[] s) {
//         int left = 0;
//         int right = s.length - 1;

//         while (left < right) {
//             char temp = s[left];
//             s[left] = s[right];
//             s[right] = temp;

//             left++;
//             right--;
//         }
//     }

//     public static void main(String[] args) {
//         char[] s = {'h','e','l','l','o'};
//         reverse(s);

//         System.out.println(s);  // olleh
//     }
// }
