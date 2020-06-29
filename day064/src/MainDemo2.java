import a.Doge;

public class MainDemo2 {


    public static void main(String[] args){
        /* 重 载 */
        System.out.println("------------------重载----------------------");
        Say d = new Say("1");
        d.sayHi();
        d.sayHi("Aaaa");
        d.sayHi("AA","BB");

        /* 继 承 */
        System.out.println("------------------继承----------------------");
        SayHello dd = new SayHello("007","lsy");
        dd.setPeople("Lsy");
        dd.sayHiAndHello();
//        Java只允许一个class继承自一个类，因此，一个类有且仅有一个父类。
        //protected修饰的字段可以被子类访问

        //如果父类没有默认的构造方法，子类就必须显式调用super()并给出参数以便让编译器定位到父类的一个合适的构造方法。

        /* 抽 象 类 */
//        Pring pp = new Print();  抽象类无法创建实例
        System.out.println("------------------抽象类----------------------");
        PrintHello ph = new PrintHello();
        ph.run();


        //如果一个class定义了方法，但没有具体执行代码，这个方法就是抽象方法，抽象方法用abstract修饰
        // 因为无法执行抽象方法，因此这个类也必须申明为抽象类（abstract class）


        /* 接 口 */
        System.out.println("------------------接口----------------------");
        PrintInter pi = new PrintInterImpl();
        pi.run();
        pi.runHello();


        /* 静态字段 静态方法 */
        System.out.println("------------------静态字段 静态方法----------------------");
        Doge doge = new Doge();

        doge.showSomething(); // 普通方法

        Doge.showNumber();    // 静态方法

        Doge.number = "1";   //

        Doge.showNumber();

        doge.number = "111"; // 通过实例 引用赋值静态变量

        doge.showNumber();  // 通过实例 引用静态方法

        /* 包 */
        System.out.println("------------------包----------------------");

        a.Doge.showNumber();

        b.Doge.showNumber();
    }
}
