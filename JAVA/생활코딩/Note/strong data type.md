strong data type

int : 정수

double : 실수



## 주석

//

/* */

/** */	: Java Doc 주석



세미콜론 : 문장이 끝났음을 알려줌



## 데이터 타입

정수 : byte, short, int, long

실수 : float, double

 데이터 타입 뭘로 했느냐가 메모리량 결정



## 상수의 데이터 타입

상수 : 변하지 않는 값

double a = 2.2; => error

float a = 2.2F;

2.2에 이미 저장되어 있는 데이터 타입이 있음, double

float으로 바꾸려면 F 붙이기



2147483648도 long으로 저장되어 있음

int로 하면 error

long 으로 바꾸러면 L 붙이기



byte, short은 변수에 int사용 허용 (범위 안에서는)



## 형변환

200, 200.0 은 다른 비트값 가짐

### 자동 형변환(암시적 형변환, implicit Conversion)

```java
double a = 3.0F;
```

float => double은 데이터 손실 일어나지 않음



```java
float a = 3.0;
```

> 오류 발생
>
> 표현범위가 좁은 데이터 타입에서 넓은 데이터 타입으로의 변환만 허용됨.



### 명시적 형변환(Explicit Conversion)

```java
float a = 100.0; // error
int b = 100.0F; // error
```

```java
float a = (float)100.0;
int b = (int) 100.0F;
```



## 연산자

### 산술연산자

\+ - * / %

### +

> 문자열 합치기도 가능

### /

> int끼리 나눴을 때 소수점 날라감
>
> float끼리 나눴을 떄 안날라감
>
> int, float 나누면 int 자동형변환 해서 float으로 바뀜



=> 이항연산자(infix operator)



###  단항 연산자

\+ : 양수

\- : 음수

++ : 증가

-- : 감소

> ++ i : 더하고 i
>
> i++ : i하고 더하기





## 연산의 우선순위

![image-20221216054350052](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20221216054350052.png)

![image-20221216054401114](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20221216054401114.png)



## 비교와 Boolean

### 비교 연산자(관계 연산자)

== : 값이 같으면 true

= : 대입

!= : 다르면 true

\> : 좌가 크면 참

.equlas : 동등 비교

