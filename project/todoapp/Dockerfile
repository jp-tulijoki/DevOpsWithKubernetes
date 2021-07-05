FROM openjdk:11
WORKDIR /todoapp
COPY .mvn/ .mvn
COPY mvnw pom.xml ./
RUN ./mvnw dependency:go-offline
COPY src ./src
EXPOSE 8080
CMD ["./mvnw", "spring-boot:run"]