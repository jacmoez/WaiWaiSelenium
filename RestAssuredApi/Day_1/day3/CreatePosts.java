package day3;


import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.util.HashMap;
import java.util.Map;

import static io.restassured.RestAssured.given;
import static org.hamcrest.Matchers.equalTo;
import static org.hamcrest.Matchers.notNullValue;

public class CreatePosts {
    private static final String BASE_URL="https://jsonplaceholder.typicode.com/";
    @BeforeAll
    public static void setup(){
        RestAssured.baseURI=BASE_URL;
    }

    @Test
    public  void testPost1(){
        String title="this is new title";
        Map<String,Object> post=new HashMap<>();// java
        post.put("title",title);
        post.put("body","this is content body");
        given()
                .contentType(ContentType.JSON)
                .body(post)
                .post("/posts")
                .then()
                .assertThat()
                .statusCode(201)
                .body("id",notNullValue())
                .body("title",equalTo(title));

    }

    @Test
    public  void testPost2(){
        String title="this is new title";
        Map<String,Object> post=new HashMap<>();// java
        post.put("title",title);
        post.put("body","this is content body");

        Map<String,Object> detail=new HashMap<>();
        detail.put("author","Test Author");
        detail.put("category","Test Catory");

        post.put("detail",detail);


        given()
                .contentType(ContentType.JSON)
                .body(post)
                .post("/posts")
                .then()
                .assertThat()
                .statusCode(201)
                .body("id",notNullValue())
                .body("title",equalTo(title))
                .body("detail.author",equalTo("Test Author"));

    }
}
