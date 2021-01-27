package www.xinx9.dev;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class TestingWebApplication{
    public static void main(String[] args){
        SpringApplication app = new SpringApplication(TestingWebApplication.class);
        app.run(args);
    }
}