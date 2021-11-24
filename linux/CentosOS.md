## Python 버전 바꾸기

파이썬 버전을 확인하니 2.x버전을 사용하고 있어 3.x로 바꾸기

```sh
$ python --version
```

```sh
$ which python
```

설치되있는 파이썬 목록 가져오기
```sh
$ ls /bin | grep python
```

현재 활성화된 파이썬 확인
```sh
$ update-alternatives --config python
```

아무것도 없다면 (혹은 원하는 버전이 없다면) 설정을 해주자.
```sh
$ sudo update-alternatives --install /bin/python python /bin/python3.7 1
```

```sh
$ sudo update-alternatives --config python
```

원하는 파이썬 버전 번호 입력 후 엔터

## 포트 번호로 프로세스 종료하기

```sh
$ netstat -tnlp | grep ${port}
```

해당 명령어로 포트 번호 확인 후 

```sh
$ kill -9 ${port}
```

프로세스를 종료하면 된다.