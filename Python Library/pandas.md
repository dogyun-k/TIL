# Pandas Library

Kaggle Pandas Tutorial을 진행하면서 정리하겠음.

> https://www.kaggle.com/learn/pandas

[연습문제](https://www.datamanim.com/dataset/99_pandas/pandasMain.html)


## 0. Pandas?

2차원 데이터를 다루면서 데이터 분석하는 데 가장 인기있는 파이썬 라이브러리

테이블 형태의 2차원 데이터. 엑셀 데이터 같은 것들..


- 설치

    ```sh
    $ pip3 install pandas
    ```

- 모듈 임포트

    ```py
    import pandas as pd
    ```

주로 `Jupyter Notebook` 환경에서 사용함


## 1. 데이터 생성, 읽기, 쓰기

- pd.read_csv(filepath, index_col="인덱스 열 이름")

데이터를 담는 객체를 생성하고 읽고 쓰기를 해 보자.

Pandas에서 객체의 종류는 Series, DataFrame 두 가지가 있다.

### 1. DataFrame

테이블. 엔트리와 그 값이 있다. 각각의 엔트리는 행, 열에 대응됨.

```py
pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}, index=['Product A', 'Produce B'])
```

### 6. Renaming and Combining

concat([테이블1, 테이블2]) : 열 정보가 똑같은 테이블 두 개 연결할 때

join() : 