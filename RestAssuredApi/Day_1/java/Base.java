import io.restassured.RestAssured;
import org.junit.jupiter.api.BeforeAll;

public class Base {
    protected  static final String BASE_URL="https://jsonplaceholder.typicode.com";// const
    @BeforeAll
    public  static void setupUrl(){
        RestAssured.baseURI=BASE_URL;
    }


}
