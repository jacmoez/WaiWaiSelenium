import io.restassured.http.ContentType;
import io.restassured.response.Response;

import static io.restassured.RestAssured.given;

public class ApiClient {

    public static Response get(String endpoint){
        return  given()
                .get(endpoint);
    }

    public  static Response get(String endpoint,String body){
        return given()
                .contentType(ContentType.JSON)
                .body(body)
                .post(endpoint);
    }
}
