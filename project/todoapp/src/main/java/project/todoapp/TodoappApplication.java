package project.todoapp;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.time.LocalDate;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class TodoappApplication {

    public static void main(String[] args) {
        SpringApplication.run(TodoappApplication.class, args);
        String directory = System.getProperty("user.dir") + "/src/main/resources/static/images/";
        int dateNumber = LocalDate.now().getDayOfYear();
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(directory + "date.txt"));
            writer.write(String.valueOf(dateNumber));
            writer.close();
        } catch (Exception writerException) {
            System.out.println(writerException.getMessage());
        }
        System.out.println("Server started in port 8080.");
    }

}
