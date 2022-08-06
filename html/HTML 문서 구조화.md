# HTML 문서 구조화

### 인라인 / 블록 요소

> 인라인 요소는 글자처럼 취급
>
> 블록 요소는 한 줄 모두 사용

### 텍스트 요소

![image-20220801200341331](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220801200341331.png)

### 그룹 컨텐츠

![image-20220801200426962](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220801200426962.png)

## form

> 정보(데이터)를 서버에 제출하기 위해 사용하는 태그

### 기본 속성

> **action** : form을 처리할 서버의 URL(데이터를 보낼 곳)
>
> **method** : form을 제출할 때 사용할 HTTP 메서드(GET 혹은 POST)
>
> **enctype** : method가 post인 경우 데이터의 유형

### input

> 다양한 타입을 가지는 입력 데이터 유형과 위젯 제공

**대표적인 속성**

> name : form control에 적용되는 이름(이름/값 페어로 전송됨)
>
> value : form control에 적용되는 값(이름/값 페어로 전송됨)
>
> required, readonly, autofocus, autocomplete, disabled

### input label

> label을 클릭해 input 자체의 초점을 맞추거나 활성화 가능
>
> <input>에 id 속성을, <label>에는 for 속성을 활용하여 상호 연관 시킴

### input 유형 - 일반

> text : 일반 텍스트 입력
>
> password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
>
> email : 이메일 형식이 아닌 경우 form 제출 불가
>
> number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
>
> file : accept 속성을 활용하여 파일 타입 지정 가능

### 항목 중 선택

> checkbox : 다중 선택
>
> radio : 단일 선택

### 기타

> color : color picker
>
> date : date picker
>
> hidden : 사용자에게 보이지 않는 input
>
> https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input



font-weight: bold;