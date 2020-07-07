import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class ReflectionDemo {


    String getFullName(Dog dog){
        return dog.getName();
    }

    String getFullNameObj(Object obj){

        Dog dog = (Dog) obj;
        return dog.getName();
    }

    public static void main(String[] args) throws NoSuchFieldException, IllegalAccessException, NoSuchMethodException, InvocationTargetException {
        Dog dog = new Dog();
        dog.setName("gou");
        String name1 = new ReflectionDemo().getFullName(dog);
        String name2 = new ReflectionDemo().getFullName(dog);


        System.out.println(name1);
        System.out.println(name2);

        // 利用反射拿到字段的一个Field实例只是第一步，我们还可以拿到一个实例对应的该字段的值。
        Class c = dog.getClass();
        Field f = c.getDeclaredField("name");
        Object value = f.get(dog);
        System.out.println(value); // " gou "

        // 1. 反射功能一： 修改字段

        // 反射  可以修改字段值
        f.set(dog, "DogeDoge");
        // 反射读写字段是一种非常规方法，它会破坏对象的封装
        System.out.println(dog.getName());

        // 2. 反射功能二:  调用方法
        Method m = Dog.class.getMethod("isAlive");

        // 在s对象上调用该方法并获取结果:
        Boolean r = (boolean) m.invoke(dog);
        System.out.println(r);

        // 获取父类
        Class n = dog.getClass();
        System.out.println(n);
        Class o = n.getSuperclass();
        System.out.println(o);

    }


}
