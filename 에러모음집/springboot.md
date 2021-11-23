## template might not exist or might not be accessible by any of the configured Template Resolvers

**Error Message**
```java
org.thymeleaf.exceptions.TemplateInputException: Error resolving template [/fragments/header.html], template might not exist or might not be accessible by any of the configured Template Resolvers
```

**Why?**
- 프라그먼트 경로를 못 찾고 있는 것.

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


