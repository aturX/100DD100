public class Dog {

    public String name;
    public String age;

    // 方法
    public boolean isAlive(){
        return true;
    }

    public Dog(String name, String age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public Dog() {
    }
}
