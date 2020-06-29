public class MainDemo {


    public static void main(String[] args){
        System.out.println("test");


        // 方法
        Point p = new Point();

        p.setX("0");
        p.setY("0");

        System.out.println(p.getX());
        System.out.println(p.getY());

        // 引用类型传参
        String [] XY = new String[]{"1","1"};
        p.setXY(XY);
        System.out.println("beging: " + p.getXY());
        XY[0] = "2";
        System.out.println("end: " + p.getXY());

        // 基本类型传参，值复制，外部修改，值不变
        // 引用类型传参，地址传入，外部修改，值改变

    }
}
