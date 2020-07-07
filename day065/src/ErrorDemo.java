import sun.rmi.runtime.Log;
import java.util.logging.Logger;



class ErrorDemo {
    public static void main(String[] args) {

        System.out.println("异常和报错");

        try{
            System.out.println("error");

        }catch(Exception e){
            System.out.println(e);
        }finally{
            System.out.println("一直执行");
        }


        // 内置Logger 日志模块
        Logger logger = Logger.getGlobal();
        logger.info("log");


        // Commons Logging
        //使用Commons Logging只需要和两个类打交道，并且只有两步：
        //第一步，通过LogFactory获取Log类的实例； 第二步，使用Log实例的方法打日志
        Log log = LogFactory.getLog();


    }
}
/**
 *  JAVA 异常 继承关系
 * Exception
 * │
 * ├─ RuntimeException
 * │  │
 * │  ├─ NullPointerException
 * │  │
 * │  ├─ IndexOutOfBoundsException
 * │  │
 * │  ├─ SecurityException
 * │  │
 * │  └─ IllegalArgumentException
 * │     │
 * │     └─ NumberFormatException
 * │
 * ├─ IOException
 * │  │
 * │  ├─ UnsupportedCharsetException
 * │  │
 * │  ├─ FileNotFoundException
 * │  │
 * │  └─ SocketException
 * │
 * ├─ ParseException
 * │
 * ├─ GeneralSecurityException
 * │
 * ├─ SQLException
 * │
 * └─ TimeoutException
 * */