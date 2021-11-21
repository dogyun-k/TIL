## 스프링부트 테스트 빌드 시 발생하는 오류

**Try**
```sh
$ ./gradlew test
```

**Error Message**
```
Contextloads() failed
```

**Why?**
- main과 test 환경은 다르다.
- test 과정에서 설정파일인 `application.yml`이 없어서 발생하는 오류

**Solution**
- `ApplicationTest.java`의 `@SpringBootTest` 주석처리

or

- test 패키지에 main의 `application.yml`을 그대로 추가해주기


## Amazon Linux에서 Build 오류 - JVM 메모리 부족

**Error Message**
```sh
  1 #
  2 # There is insufficient memory for the Java Runtime Environment to continue.
  3 # Native memory allocation (mmap) failed to map 262144 bytes for committing reserved memory.
  4 # Possible reasons:
  5 #   The system is out of physical RAM or swap space
  6 #   The process is running with CompressedOops enabled, and the Java Heap may be blocking the growt    h of the native heap
  7 # Possible solutions:
  8 #   Reduce memory load on the system
  9 #   Increase physical memory or swap space
 10 #   Check if swap backing store is full
 11 #   Decrease Java heap size (-Xmx/-Xms)
 12 #   Decrease number of Java threads
 13 #   Decrease Java thread stack sizes (-Xss)
 14 #   Set larger code cache with -XX:ReservedCodeCacheSize=
 15 #   JVM is running with Unscaled Compressed Oops mode in which the Java heap is
 16 #     placed in the first 4GB address space. The Java Heap base address is the
 17 #     maximum limit for the native heap growth. Please use -XX:HeapBaseMinAddress
 18 #     to set the Java Heap base and to place the Java Heap above 4GB virtual address.
 19 # This output file may be truncated or incomplete.
 20 #
 21 #  Out of Memory Error (os_linux.cpp:2993), pid=4126, tid=4145
 22 #
 23 # JRE version: OpenJDK Runtime Environment Corretto-11.0.13.8.1 (11.0.13+8) (build 11.0.13+8-LTS)
 24 # Java VM: OpenJDK 64-Bit Server VM Corretto-11.0.13.8.1 (11.0.13+8-LTS, mixed mode, tiered, compre    ssed oops, serial gc, linux-amd64)
 25 # No core dump will be written. Core dumps have been disabled. To enable core dumping, try "ulimit     -c unlimited" before starting Java again
 26 #
```

**Why?**
- 메모리가 부족

**Solution**
- Increase physical memory or swap space : 스왑 공간을 만들기
> https://aws.amazon.com/ko/premiumsupport/knowledge-center/ec2-memory-swap-file/


## pip3 install 시 MemoryError

**Try**
```sh
$ pip3 install torch
```

**Error Message**
```
블라블라...

MemoryError
```

**Why?**
- 설치 시 caching을 사용해서 그럼
- EC2 싱글코어에서 설치할려니까 설치 메모리가 부족?

**Solution**
- 캐싱 미사용 옵션을 주고 설치한다.
  
    ```sh
    $ pip3 install --no-cache-dir torch
    ```

## OpenCV 설치 오류

**Error Message**
```
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```

**Solution**
```sh
$ yum install mesa-libGL
```