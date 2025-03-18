//  https://jsonplaceholder.typicode.com/posts

import io.restassured.*;
import org.junit.jupiter.api.*;

import static io.restassured.RestAssured.given;
import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.Matchers.*;


public class JsonPlaceHolderTest {

    @BeforeAll
    public static void setupURL(){
       RestAssured.baseURI="https://jsonplaceholder.typicode.com";
    }

    @Test
    public void getAllPosts(){
        given()
                .get("/posts")
                .then()
                .statusCode(200)
                .body("$.size()",greaterThan(10));
    }


    @Test
    public void getPostById(){
        given()
                .contentType("application/json")
                .pathParam("id",2)
                .get("/posts/{id}")
                .then()
                .statusCode(200)
                .body("id",equalTo(2));

    }

    @Test
    public void createPost(){
        given()
                .contentType("application/json")
                .body("{\"title\":\"New Title\", \"body\":\"this is content for new title\"}")
                .post("/posts")
                .then()
                .statusCode(201)
                .body("title",equalTo("New Title"));

    }

    @Test
    public void updatePost(){
        given()
                .contentType("application/json")
                .pathParam("id",1)
                .body("{ \"title\":\"Update title\", \"body\":\"this is body of updated\"}")
                .put("/posts/{id}")
                .then()
                .statusCode(200)
                .body("title",equalTo("Update title"));
    }

    @Test
    public  void deletePost(){
        given()
                .pathParam("id",1)
                .delete("/posts/{id}")
                .then()
                .statusCode(anyOf(is(200)));
    }


}
