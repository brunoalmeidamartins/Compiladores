class Factorial {
    public static void main(String[] a) {
        System.out.println(new Fac().ComputeFac(10));
    }
}

class Fac {
    public int ComputeFac(int num) {
        int num_aux;
        int b;
        if (num< 1)
            b = num;

        else
            num_aux = num * (this.ComputeFac(num-1));
        return num_aux;
    }

}
