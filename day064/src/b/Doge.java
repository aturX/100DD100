package b;

public class Doge {

    public String name;
    public String age;

    // 静态字段
    public static String number;

    // 静态方法
    public static void showNumber(){
        System.out.println("Class static field This is Doge BBB B");
        System.out.println(Doge.number);
    }

    public void showSomething(){
        System.out.println("show some thing...");
    }

}
