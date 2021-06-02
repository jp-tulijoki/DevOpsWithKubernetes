FROM openjdk:11 as build-state
COPY . .
RUN ./mvnw package

FROM openjdk:11
COPY --from=build-state ./target/todoapp-0.0.1-SNAPSHOT.jar todoapp.jar
CMD ["java", "-jar", "todoapp.jar"]