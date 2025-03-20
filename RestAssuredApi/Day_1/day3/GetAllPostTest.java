package day3;

import io.restassured.response.Response;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Map;

import static io.restassured.RestAssured.given;
import static io.restassured.RestAssured.oauth;
import static org.hamcrest.Matchers.*;

public class GetAllPostTest {

    @Test
    public void testDataSize(){
        given()
                .get("https://jsonplaceholder.typicode.com/posts/")
                .then()
                .assertThat()
                .body("$",hasSize(100));
        System.out.println("Test : Response Body Size");
    }

    @Test
    public  void testCheckId(){
        given()
                .get("https://jsonplaceholder.typicode.com/posts/")
                .then()
                .assertThat()
                .body("id[0]",equalTo(1))
                .body("userId[0]",equalTo(1));
    }

    @Test
    public  void testCheckTitle(){
        given()
                .get("https://jsonplaceholder.typicode.com/posts/")
                .then()
                .assertThat()
                .body("title",hasItem(equalTo("nesciunt quas odio")));
        System.out.println("Test :  Title Test");
    }

    @Test
    public  void testCheckItem(){
        given()
                .get("https://jsonplaceholder.typicode.com/posts/")
                .then()
                .assertThat()
                .body("id",hasItems(1,2,4,3));
        System.out.println("Test : Item Check");
    }

    @Test
    public  void testCheckItem1(){
        given()
                .get("https://jsonplaceholder.typicode.com/posts/")
                .then()
                .assertThat()
                .body("id",everyItem(greaterThan(0)));
        System.out.println("Test : Item Check");
    }

    @Test
    public void testExtractIds(){
       Response  res=given()
                .get("https://jsonplaceholder.typicode.com/posts/");
        List<Integer> ids=res.jsonPath().getList("id");
        System.out.println("Ids : "+ids);
    }


    @Test
    public void testExtractData(){
        Response  res=given()
                .get("https://jsonplaceholder.typicode.com/posts/");
        List<Object> posts=res.jsonPath().getList("$"); // list

        for(int i=0;i<posts.size();i++){
//            System.out.println(posts.get(i));
            Map<String,Object> map= (Map<String, Object>) posts.get(i);
            System.out.println(map.get("title"));
            System.out.println("-------------------------");
        }

    }

    @Test
    public void testListFiltering(){
        given()
                .get("https://jsonplaceholder.typicode.com/posts/")
                .then()
                .assertThat()
                .body("findAll{post->post.userId==1}.id",hasItems(1,2,3,4,5,6,7,8,9,10));

        given()
                .get("https://jsonplaceholder.typicode.com/posts/")
                .then()
                .assertThat()
                .body("findAll{post->post.userId==1}.id",hasSize(10));

    }


}
