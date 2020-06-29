public class Say {
    public String id;

    public void sayHi(){
        System.out.println("Hi");
    }

    public void sayHi(String A){
        System.out.println(A + " Hi");
    }

    public void sayHi(String A, String B){
        System.out.println(A + " Hi " + B + " Hi ");
    }

    public Say(String id){
        this.id = id;
    }



}
