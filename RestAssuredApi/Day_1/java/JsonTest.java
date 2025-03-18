import org.junit.jupiter.api.Test;

import static org.hamcrest.Matchers.equalTo;

public class JsonTest  extends  Base{
    @Test
    public void testGetAllPosts(){
        ApiClient.get("/posts")
                .then()
                .statusCode(200)
                .body("$.size()",equalTo(100));

    }

    @Test
    public  void testGetPostById(){
        int id=1;
        String end_point="/posts/"+id;
        ApiClient.get(end_point)
                .then()
                .body("id",equalTo(id));
    }
}
