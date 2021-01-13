public class Random{
    public static void main(String[] args) {
        long a = System.currentTimeMillis();
        a = a%1000;
        System.out.print("The random number is : ");
        System.out.println(a);
    }
}