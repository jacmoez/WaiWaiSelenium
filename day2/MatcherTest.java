package day2;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.hamcrest.CoreMatchers.equalTo;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.*;


public class MatcherTest{

    @Test
    void objMatcher(){
        String obj1="Hello";
        Object obj2="Hello";
        Object obj3=new String("Hello"); // ref1
        Object obj4=new String("Hello"); // ref2
        assertThat(obj1,equalTo(obj2));
        assertThat(obj1,is(obj2));
        assertThat(obj4,is(obj3));

//        assertThat(obj1,not(equalTo(obj2)));

        String null_value=null;
        assertThat(null_value,nullValue());
//        assertThat(null_value,notNullValue());

//        assertThat(obj3,sameInstance(obj4));

        assertThat(obj1,instanceOf(String.class));

        int num=20;
        assertThat(num,instanceOf(String.class));
        assertThat(num,any(Object.class));
    }


    @Test
    void numberMatcher(){
        int actual=10;
        int guess=5;
//        assertThat(actual,greaterThan(guess));
//        assertThat(actual,greaterThanOrEqualTo(guess));
//        assertThat(actual,lessThan(guess));
//        assertThat(actual,lessThanOrEqualTo(guess));
        assertThat(10.2,closeTo(10.19,0.05));
    }

    @Test
    void strigMatcher(){
        String str="Hello Developer";
        assertThat(str,equalTo("Hello Developer"));
//        assertThat(str,equalTo("HELLO"));
        assertThat(str,equalToIgnoringCase("HELLO DEVELOPER"));
        assertThat(str,containsString("Hello"));
        assertThat(str,startsWith("Hello"));
        assertThat(str,endsWith("Developer"));

        assertThat(str,stringContainsInOrder("Hello","Developer"));

        String test="   Hello  ";
        assertThat(test.trim(),equalTo("Hello"));

        String test1="";
        boolean con=test1=="";
        assertThat(test1,con);

        String test2=null;
        assertThat(test2,emptyOrNullString());
    }

    @Test
    void collectionTest(){
        List<Integer> ints=new ArrayList<>();
        ints.add(10);
        ints.add(20);
        ints.add(30);

        assertThat(ints,hasItem(30));
        assertThat(ints,hasItems(30,10));

        assertThat(ints,hasSize(3));

        //assertThat(ints,contains(10,30,20));
        assertThat(ints,containsInAnyOrder(10,30,20));

        assertThat(ints,everyItem(greaterThan(5)));

        Integer[] ary=new Integer[]{1,2,3,4,5};// array
        assertThat(ary,arrayContaining(1,2,3,4,5));
        assertThat(ary,arrayContainingInAnyOrder(1,3,2,4,5));
        assertThat(ary,arrayWithSize(5));
        System.out.println(ints);
       /*
        // 8 bits 256/2 => 128 [ -128 0 127]
        byte b1=10;
        byte b2=127;
        // 65536/2 => 32768 [-32768 0  32767]
        short s1=-32768;

        // type casting
        byte b3=10;
        int i1=b3;//ok  Implicit type casting

        int i2=32;
        byte b4=(byte)i2; // explicit type casting

        char ch='A';
        int c=ch; // char code
        char c1=66;
        System.out.println(c);
        System.out.println(c1);
        */
    }


    /*
      Primitive , Non-primitive
      Primitive
      1.byte     =>  1 byte => 1byte = 8 bits
      2.short    =>  2 bytes=> 2x8 =>16 bits
      3.int      =>  4 bytes
      4.long     =>  8 bytes

      5.float    =>  4 bytes
      6.double   =>  8 bytes

      7.char     =>  2 bytes
      8.boolean  =>  1 bit (yes,no - 0,1)
     */
}
