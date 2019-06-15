class BubbleSort{
    public static void main(String[] a){
	System.out.println(new BBS().Start(10));
    }
}


// This class contains the array of integers and
// methods to initialize, print and sort the array
// using Bublesort
class a extends BBS{

    int[] number ;
    int size ;

    // Invoke the Initialization, Sort and Printing
    // Methods
    public int Start(int sz){
        int aux01 ;
        aux01 = this.Init(sz);
        aux01 = this.Print();
        System.out.println(99999);
        aux01 = this.Sort();
        aux01 = this.Print();
        return 0 ;
    }
}