## 세션이 필요한 이유 

HTTP 통신은 stateless한 특징을 가지고 있다.

즉 하나의 요청과 응답이 끝난 뒤면 요청한 클라이언트를 기억하지 못 한다.

이전에 요청한 클라이언트를 기억하기 위해 **세션**을 사용해서 기억을 한다.

세션을 유지하는 방법 : **쿠키** / URL 재작성

**세션**
- 사용자 정보를 서버에 저장
- 클라이언트의 최초 접속 시 새로운 세션을 생성하고 세션 ID 전송
- 이후 접속마다 클라이언트가 세션 ID 재전송
- 서버는 세션 ID에 해당하는 세션 정보를 획득
- 세션 ID 전송 수단으로 쿠키를 사용할 수 있음\


(왜 기억해야할까? 로그인 등과 같이 사용자가 여러 페이지를 탐방할 때 각각의 페이지에서도 해당 유저를 기억하고 있어야 해당하는 처리를 해 줄 수 있다.)

**쿠키**
- 브라우저를 통해 클라이언트에 저장되는 사용자 정보
- (name, value) 쌍으로 이루어진 정보
- 초기에 웹 서버에 의해 HTTP Header에 포함되어 클라이언트에게 전송
- 이후에 접속마다 클라이언트가 웹 서버에게 재전송
- 보안적 취약성으로 인해 중요 정보를 저장하지 않아야 함

## HttpSession

**둘 이상의 웹 사이트 요청 또는 방문**에서 사용자를 식별하고 해당 사용자에 대한 정보를 저장하는 방법을 제공합니다.

> HTTP는 Stateless 특성때문에 하나의 요청/응답은 독립적이다. 그래서 두 개 이상의 요청/응답 시에는 이전의 요청에 대한 정보가 1도 없다. 그래서 사용자를 식별하지 못 함.

서블릿 컨테이너는 이 인터페이스를 사용하여 HTTP 클라이언트와 HTTP 서버 간에 세션을 만듭니다. 세션은 지정된 기간 동안 두 개 이상의 연결 또는 페이지 요청에 걸쳐 유지됩니다. 세션은 일반적으로 사이트를 여러 번 방문할 수 있는 한 명의 사용자에 해당합니다. **서버는 쿠키를 사용하거나 URL을 다시 쓰는 것과 같은 다양한 방법으로 세션을 유지**할 수 있습니다.


- 세션 추가하기.

    ```java
    @Controller
    public class testController() {
        public String testSession(HttpSession session) {
            User user = new User();
            session.setAttribute("user", user);

            return "index";
        }
    }
    ```
    - User 객체를 생성하고 세션에 추가하는 로직.

## @SessionAttributes

- 모델(Model) 정보를 HTTP 세션에 저장해주는 어노테이션.
- 컨트롤러에 추가하는 어노테이션 `@SessionAttributes("속성")`
- 해당 컨트롤러에서 생성하는 모델의 Key 이름이 속성 이름과 같다면 해당 모델을 세션에 저장함.

    ```java
    @SessionAttributes("user")
    @Controller
    public class testController() {
        public String testSession(Model model) {
            User user = new User();
            model.addAttribute("user", user);

            return "index";
        }
    }
    ```
    - user 객체가 model에 key "user"로 추가되면 Controller에서는 `@SessionAttributes`에 의해 이를 인식하여 세션에 추가함.

- 세션 만료하기

    ```java
    @SessionAttributes("user")
    @Controller
    public class testController() {
        public String testEndSession(SessionStatus status) {
            status.setComplete();

            return "index";
        }
    }
    ```
    - `SessinoStatus`로 세션의 상태를 받아와서 이를 완료로 바꾼다.

## @ModelAttribute

- 요청 메세지의 객체 바인딩 뿐만 아니라 세션에 있는 데이터도 바인딩할 때 사용한다.