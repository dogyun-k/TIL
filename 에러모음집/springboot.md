## template might not exist or might not be accessible by any of the configured Template Resolvers

**Error Message**
```java
org.thymeleaf.exceptions.TemplateInputException: Error resolving template [/fragments/header.html], template might not exist or might not be accessible by any of the configured Template Resolvers
```

**Why?**
- 프라그먼트 경로를 못 찾고 있는 것.
- 스프링부트 템플릿 엔진의 기본 경로는 `template/`인데 `/fragments/header.html`로 경로를 지정해주니까 `template//fragments/header.html`로 찾게되서 발생한다.

**Solution**
1. Classpath 재설정

`application.yml`
```yml
spring:
    thymeleaf:
        prefix: classpath:/template
```

2. 파일 내 경로를 제대로 작성

`main.html`
```html
before
<nav th:replace="/fragments/nav.html :: fragment-nav">

after
<nav th:replace="fragments/nav.html :: fragment-nav">
```
- `/`를 지워줌.



## TemplateEngine

**Error Message**
```java
2021-11-13 23:09:15.199 ERROR 16696 --- [io-8080-exec-10] org.thymeleaf.TemplateEngine             : [THYMELEAF][http-nio-8080-exec-10] Exception processing template "post/postsView": An error happened during template parsing (template: "URL [file:src/main/resources/templates/post/postsView.html]")

org.thymeleaf.exceptions.TemplateInputException: An error happened during template parsing (template: "URL [file:src/main/resources/templates/post/postsView.html]")
```

**Why?**
- 템플릿 엔진 파싱 오류

**Solution**
- 엔티티 속성 이름을 변경하고 html에 적용을 안 했음.


## Amazon Linux에서 Build 오류 - 라이브러리 미지원 

**Error Message**
```java
org.gradle.api.tasks.TaskExecutionException: Execution failed for task ':generateAot'.
Caused by: org.springframework.aot.CodeGenerationException: Could not generate spring.factories source
Caused by: java.lang.IllegalStateException: Devtools is not supported yet, please remove the related de
```

**Why?**
- Devendencies : Devtools를 지원하지 않음

**Solution**
- Devtools 라이브러리를 지운다.


## com.fasterxml.jackson.databind.exc.MismatchedInputException

**Try**
- API를 호출 한 뒤에 반환 값이 비어있을 때 발생함.

**Why?**
- API서버에서 응답 데이터의 JSON 변환을 두 번 해주어 발생함

**Soluction**
- API 서버에서 응답 데이터의 JSON을 한 번만 해주게 수정함.


## org.springframework.dao.InvalidDataAccessResourceUsageException

**Error Message**
```sh
Servlet.service() for servlet [dispatcherServlet] in context with path [] threw exception [Request processing failed; nested exception is org.springframework.dao.InvalidDataAccessResourceUsageException: could not extract ResultSet; SQL [n/a]; nested exception is org.hibernate.exception.SQLGrammarException: could not extract ResultSet] with root cause

java.sql.SQLException: 'dietblog.hibernate_sequence' is not a SEQUENCE
```

**Why?**

공식 문서에서 발쵀

- 데이터 액세스 리소스를 잘못 사용할 때 발생하는 예외에 대한 루트입니다. 예를 들어 RDBMS를 사용할 때 잘못된 SQL을 지정할 때 발생합니다. 리소스별 하위 클래스는 구체적인 데이터 액세스 패키지에 의해 제공됩니다.

**Solution**
- 설정파일이 없었다.
- 즉 DB 연결이 안 됐었다. 하..ㅋ

**왜 그런 뻘짓을 했나**
- 개발환경과 배포환경의 설정파일 내용이 달라서 `.gitignore`에 설정파일들을 추가해놨었다.
- 이러면 각자의 설정파일을 가지고 있겠지? 라고 멍청하게 생각했다.
- 그리고 깃에 푸쉬를 하니까 설정파일이 없는 채로 푸쉬됐다.
- 그 상태에서 배포환경에서 Pull을 하니까 설정파일이 없는 채로 실행이 됐던 것이다..



## Springboot 구글 로그인 세션 테이블 생성

**Error Message**
```java
org.springframework.jdbc.BadSqlGrammarException: PreparedStatementCallback; bad SQL grammar [DELETE FROM SPRING_SESSION WHERE EXPIRY_TIME < ?]; nested exception is org.h2.jdbc.JdbcSQLSyntaxErrorException: Table "SPRING_SESSION" not found; SQL statement:
DELETE FROM SPRING_SESSION WHERE EXPIRY_TIME < ? [42102-200]
```

**Why?**

- 세션 정보를 저장할 테이블이 생성안되서 발생하는 문제


**Solution**

- 아래 쿼리 실행하여 수동으로 테이블을 생성해준다.

    ```sql
    CREATE TABLE SPRING_SESSION (
        PRIMARY_ID CHAR(36) NOT NULL,
        SESSION_ID CHAR(36) NOT NULL,
        CREATION_TIME BIGINT NOT NULL,
        LAST_ACCESS_TIME BIGINT NOT NULL,
        MAX_INACTIVE_INTERVAL INT NOT NULL,
        EXPIRY_TIME BIGINT NOT NULL,
        PRINCIPAL_NAME VARCHAR(100),
        CONSTRAINT SPRING_SESSION_PK PRIMARY KEY (PRIMARY_ID)
    );

    CREATE UNIQUE INDEX SPRING_SESSION_IX1 ON SPRING_SESSION (SESSION_ID);
    CREATE INDEX SPRING_SESSION_IX2 ON SPRING_SESSION (EXPIRY_TIME);
    CREATE INDEX SPRING_SESSION_IX3 ON SPRING_SESSION (PRINCIPAL_NAME);

    CREATE TABLE SPRING_SESSION_ATTRIBUTES (
        SESSION_PRIMARY_ID CHAR(36) NOT NULL,
        ATTRIBUTE_NAME VARCHAR(200) NOT NULL,
        ATTRIBUTE_BYTES LONGVARBINARY NOT NULL,
        CONSTRAINT SPRING_SESSION_ATTRIBUTES_PK PRIMARY KEY (SESSION_PRIMARY_ID, ATTRIBUTE_NAME),
        CONSTRAINT SPRING_SESSION_ATTRIBUTES_FK FOREIGN KEY (SESSION_PRIMARY_ID) REFERENCES SPRING_SESSION(PRIMARY_ID) ON DELETE CASCADE
    );
    ```


## org.h2.jdbc.JdbcSQLSyntaxErrorException: Column "start_value" not found [42122-202]

- DB를 AWS RDS에서 H2로 변경했는데 이런 문제가 발생함.
- 근데 그냥 해도 웹애플리케이션은 잘 동작함.

**Why?**
