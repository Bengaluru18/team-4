// Converting Java variables to JSON Object
import com.google.gson.Gson;

public class TestObjectToJson {
  private int data1 = 100;
  private String data2 = "hello";

  public static void main(String[] args) {
      TestObjectToJson obj = new TestObjectToJson();
      Gson gson = new Gson();

      //convert java object to JSON format
      String json = gson.toJson(obj);

      System.out.println(json);
  }

}
