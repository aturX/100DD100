public class SayHello extends Say{

    //Java使用extends关键字来实现继承
    private String people;
    public String getPeople() {
        return this.people;
    }
    public void setPeople(String people) {
        this.people = people;
    }

    public void sayHiAndHello(){
        this.sayHi(this.people);
        System.out.println("Hello");
    }

    public SayHello(String id, String people){
        super(id);
        this.people = people;
    }


}
