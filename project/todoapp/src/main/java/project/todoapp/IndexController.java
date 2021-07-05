package project.todoapp;

import java.awt.Image;
import java.awt.image.BufferedImage;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.net.URL;
import java.time.LocalDate;
import javax.imageio.ImageIO;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class IndexController {
    
    @GetMapping("*")
    public String index() {
        String directory = System.getProperty("user.dir") + "/src/main/resources/static/images/";
        BufferedImage image = null;
        int dateNumber = LocalDate.now().getDayOfYear();
        String date = "";
        try {
            BufferedReader reader = new BufferedReader(new FileReader(directory + "date.txt"));
            date = reader.readLine();
            reader.close();
        } catch (Exception readerException) {
            System.out.println(readerException.getMessage());
        }
        if (!(date.equals(String.valueOf(dateNumber)))) {
            try {
                URL url = new URL("https://picsum.photos/" + dateNumber);
                image = ImageIO.read(url);
                ImageIO.write(image, "jpg", new File(directory + "image.jpg"));
            } catch (Exception downloadException) {
                System.out.println(downloadException.getMessage());
            }
        }
        return "index";
    }
       
}
