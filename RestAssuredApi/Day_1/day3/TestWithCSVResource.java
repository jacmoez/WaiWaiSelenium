package day3;


import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.anyOf;
import static org.hamcrest.Matchers.is;

public class TestWithCSVResource {
    private static final String BASE_URL="https://jsonplaceholder.typicode.com/";
    @BeforeAll
    public static void setup(){
        RestAssured.baseURI=BASE_URL;
    }
    @ParameterizedTest
    @CsvSource({
            "Test Title 1, Test Body 1, 1, 201, Test Title 1",
            "Test Title 2, Test Body 2, 2, 201, Test Title 2",
            "Test Title 3, Test Body 3, 3, 201, Test Title 3",
            "Test Title 4, Test Body 4, 4, 201, Test Title 4",
            "Test Title 5, Test Body 5, 5, 201, Test Title 5",
            "Test Title 6, Test Body 6, 6, 201, Test Title 6",
            " , Test Body 7, 7, 201, ",
            "Test Title 8, , 8, 201, Test Title 8",
            "Test Title 9, Test Body 9, , 201, Test Title 9",
            " , , , 201, ",
            "Test Title 10, Test Body 10, abc, 201, Test Title 10",
            "Test Title 11, Test Body 11, 9999999999, 201, Test Title 11"
    })
    public  void createPost(String title,String body,Object userId,int expectedStatusCode, String expectedTitle){
        String requestBody="{"+
                (title!=null&&!title.isEmpty()?"\"title\":\""+title+"\",":"")+
                (body!=null&&!body.isEmpty()?"\"body\":\""+body+"\"":"")+
                "}";
        System.out.println(requestBody);
      given()
              .contentType(ContentType.JSON)
              .body(requestBody)
              .post("/posts")
              .then()
              .statusCode(anyOf(is(201)));
    }

}
