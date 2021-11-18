## 서버 생성 시 꼭 해야 할 설정

1. 자바 설치
2. 타임 존 변경
3. 호스트 이름 변경


## 1. 자바 설치

프로젝트의 자바 버전에 맞게 설치한다.

나는 자바 11버전 설치

Amazon Linux에서 지원하는 자바는 1.8까지(java 8)

그래서 Amazon Coretto를 통해 설치

**JDK 설치**

```sh
# aws coreetto 다운로드
sudo curl -L https://corretto.aws/downloads/latest/amazon-corretto-11-x64-linux-jdk.rpm -o jdk11.rpm

# jdk11 설치
sudo yum localinstall jdk11.rpm

# jdk version 선택
sudo /usr/sbin/alternatives --config java

# java 버전 확인
java --version

# 다운받은 설치키트 제거
rm -rf jdk11.rpm
```

**이전 버전 제거**

```sh
yum list installed | grep "java" # yum 설치 리스트 확인
# java-1.8.0-openjdk-headless.x86_64    1:1.8.0.222.b10-0.47.amzn1   @amzn-updates
# java-11-amazon-corretto-devel.x86_64  1:11.0.7.10-1                installed

sudo yum remove java-1.8.0-openjdk-headless.x86_64 
```


## 2. 타임 존 변경

```sh
sudo rm /etc/localtime
sudo ln -s /usr/share/zoneinfo/Asia/Seoul /etc/localtime

date
```

## 3. 호스트 이름 변경

파일 열고 

```sh
sudo vi /etc/cloud/cloud.cfg
```

내용 추가

```sh
preserve_hostname: true
```

호스트 이름 설정

```sh
sudo hostnamectl set-hostname $hostname
```

그리고 재시작하면 됨.

호스트네임 등록

```sh
sudo vi /etc/hosts
```

맨 밑줄에 추가

```sh
127.0.0.1   $hostname
```


