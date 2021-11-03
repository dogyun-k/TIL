
파일 전송 시

RestApi를 통해 이미지 파일 등을 Json에 넣어 보낼 경우

```
파일 -> BinaryCode
BinaryCode -> String

       (전송)

String -> BinaryCode
BinaryCode -> 파일
```

```java
import java.util.Base64;

// 파일 -> 바이너리코드
if (file.type == MultipartFile){
    byte[] bytes = file.getBytes();
}

// 바이너리코드 -> 스트링
String temp = Base64.getEncoder().encodeToString(binaryCode);

// 스트링 -> 바이너리코드
byte[] binary = Base64.getDecoder().decode(temp);
// 바이너리코드 -> 파일
FileInputStream inputStream = new FileInputStream(uploadPath + fileName);

BufferedImage bufferedImage = ImageIO.read(inputStream);
File file = new File(filePath_image);
ImageIO.write(bufferedImage, "png", file);

inputStream.close();
```