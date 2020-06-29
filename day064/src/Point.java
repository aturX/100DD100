public class Point {


    private String X;
    private String Y;
    private String[] XY;


    public String getX() {
        return this.X;
    }

    public String getY() {
        return this.Y;
    }

    public void setX(String X){
        this.X = X;
    }

    public void setY(String Y){
        this.Y = Y;
    }

    public String getXY(){
        return this.XY[0] + this.XY[1];
    }

    public void setXY(String[] XY){
        this.XY = XY;
    }


    /*构造方法*/

    // 无参数构造方法 (编译器默认生成)
//    public Point(){
//
//    }
    // 含参数构造方法
    public Point(String X){
        this.X = X;
    }

    // 多重构造方法
    public Point(String X, String Y){
        this.X = X;
        this.Y = Y;
    }

    // 内部调用构造方法
    public Point(){
        this("0");  // 调用另一个 构造方法
    }
}
