import java.util.Arrays;

public class Main {


    public static void  main(String[] args){
        System.out.println("This is main!");

        // var sb = new StringBuilder();    // JDK 14 新特性

        /*
          ava定义了以下几种基本数据类型：

          整数类型：byte，short，int，long

          浮点数类型：float，double

          字符类型：char

          布尔类型：boolean
          **/

        // 浮点运算存在误差
        double x = 1.0 / 10;
        double y = 1 - 9.0 / 10;
        // 观察x和y是否相等:
        System.out.println(x);
        System.out.println(y);

        /* 浮点型判断相等的方式
        * // 比较x和y是否相等，先计算其差的绝对值:
            double r = Math.abs(x - y);
            // 再判断绝对值是否足够小:
            if (r < 0.00001) {
                // 可以认为相等
            } else {
                // 不相等
            }
        * */


        // 数组
        int [] all = new int[5];
        all[0] = 1;
        all[1] = 2;
        all[2] = 3;
        all[3] = 4;
        all[4] = 5;

        System.out.println(Arrays.toString(all));

        int[] all2 = new int[]{1,2,3,4,5};
        // int[] all2 = {1,2,3,4,5};
        System.out.println(Arrays.toString(all2));



        // 引用
        String[] names = {"ABC", "XYZ", "zoo"};
        String s = names[1];
        names[1] = "cat";
        System.out.println(s); // s是"XYZ"还是"cat"?
        System.out.println(Arrays.toString(names)); // s是"XYZ"还是"cat"?

        // 遍历数组
//        for (int anAll : all) {
//            System.out.println(anAll);
//        }
        for(int i=0; i<all.length; i++){
            System.out.println(all[i]);
        }

        // 数组排序 (冒泡排序)
        int[] ns = { 28, 12, 89, 73, 65, 18, 96, 50, 8, 36 };
        System.out.println(Arrays.toString(ns));
        for(int i=0; i<ns.length; i++){
            for(int j=i+1; j<ns.length; j++){
                int temp;
                if(ns[i] > ns[j]){
                    temp = ns[i];
                    ns[i] = ns[j];
                    ns[j] = temp;
                }
            }

        }
        System.out.println(Arrays.toString(ns));

    }
}
