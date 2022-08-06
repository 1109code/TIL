# CSS

Cascading Style Sheets

스타일링을 지정하기 위한 언어

![image-20220801205354075](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220801205354075.png)

> 선택자를 통해 스타일을 지정할 HTML 요소 선택
>
> 속성(Property) : 어떤 스타일 기능을 변경할지 결정
>
> 값(Value) : 어떻게 스타일 기능을 변경할지 결정

### CSS 정의 방법

> 인라인(inline)
>
> 내부 참조(embedding) - \<style>
>
> 외부 참조(link file) - 분리된 CSS 파일

### CSS 구문 - 용어 정리

**기본 선택자**

> 전체 선택자, 요소 선택자
>
> 클래스 선택자 : 마침표(.)문자로 시작, 해당 클래스가 적용된 항목 선택
>
> 아이디 선택자 : # 문자로 시작, 해당 아이디가 적용된 항목 선택
>
> ​							일반적으로 하나의 문서에 1번만 사용, 여러개 사용해도 되지만 단일 id 권장
>
> 속성 선택자

**결합자(Combinators)**

> 자손 결합자, 자식 결합자
>
> 일반 형제 결합자, 인접 형제 결합자

**의사 클래스/요소(Pseudo Class)**

> 링크, 동적 의사 클래스
>
> 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

**CSS 적용 우선순위(cascading order)**

1.  중요도(Importance)
   1. !important
2. 우선 순위(Specificity)
   1. 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서

**CSS 상속**

> CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
>
> **상속 되는** 것 : text 관련 요소(font, color, text-align), opacity, visibility 등
>
> 상속 되지 않는 것 : box model 관련 요소(width, height, margin, padding, border, box-sizing, display) , position 관련 요소(position, top/right/bootm/left, z-index)



### 크기 단위

---

* px(픽셀)

> 고정적인 값

* %

> 가변적 레이아웃에 사용

* em

>(바로 위, 부모 요소에 대한) 상속의 영향을 받음
>
>배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

* rem

> 상속의 영향을 받지 않음
>
> 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

* viewport

> 웹 페이지를 방분한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역 (디바이스 화면)
>
> 디바이스의 viewport를 기준을 상대적인 사이즈가 결정됨
>
> vw, vh, vmin, vmax

# 색상 단위

* 색상 키워드(background-color: red;)

> 대소문자를 구분하지 않음

* RBG 색상(background-color: rgb(0, 255, 0);)

> 16진수 표기법 혹은 함수형 표기법을 사용해 특정 색을 표현하는 방식

* HSL 색상(background-color: hsl(0, 100%, 50%);)

> 색상, 채도, 명도를 통해 특정 색 표현



### 결합자(Combinators)

자손 결합자

> selectorA 하위의 모든 selectorB 요소

자식 결합자(>)

> selectorA 바로 아래의 selectorB 요소

일반 형제 결합자(~)

> selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택

인접 형제 결합자(+)

> selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택



## Box model

모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.

하나의 박스는 네 부분(영역)으로 이루어짐

* margin
* border
* padding
* content

box-sizing 시 border까지의 너비를 정하고 싶으면 border-box로 설정!!



## CSS Display

display: block

> 줄 바꿈이 일어나는 요소
>
> 화면 크기 전체의 가로 폭을 차지
>
> 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

display: inline

> 줄 바꿈이 일어나지 않는 행의 일부 요소
>
> content 너비만큼 가로 폭을 차지함
>
> width, height, margin-top, margin-bottom 지정 불가
>
> 상하 여백은 line-height로 지정

블록 레벨 요소

> div / ul, ol, li/ p / hr / form

인라인 레벨 요소

> span/ a / img / input, label / b, em, i, strong

### block

block의 기본 너비는 가질 수 있는 너비의 100%

너비를 가질 수 없다면 자동으로 부여되는 margin

### inline

inline의 기본 너비는 컨텐츠 영역 만큼



margin-right: auto;

margin-left: auto;



text-align: left;

text-align: right;

text-align: center;



### display

display: inline-block

> block과 inline 레벨 요소의 특징을 모두 가짐
>
> inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음

display: none

> 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
>
> 이와 비슷한 visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않음

https://developer.mozilla.org/ko/docs/Web/CSS/display



## CSS position

문서 상에서 요소의 위치를 지정

static: 모든 태그의 기본 값

> 일반적인 요소의 배치 순서 따름(좌상단)
>
> 부모 요소 내에 배치될 때는 부모 요소의 위치를 기준으로 배치

relative : 상대 위치

> 자기 자신의 static 위치를 기준으로 이동(nomral flow 유지)
>
> 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음(normal position 대비 offset)

absolute : 절대 위치

> 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
>
> static이 아닌 가장 가까이 있는 부모 /조상 요소를 기준으로 이동(없는 경우 브라우저 화면 기준으로 이동)

fixed : 고정 위치

> 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음(normal flow에서 벗어남)
>
> 부모 요소와 관계없이 viewport를 기준으로 이동
>
> * 스크롤 시에도 항상 같은 곳에 위치함

sticky : 스크롤에 따라 static -> fixed로 변경

> 속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따름
>
> 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성



## 개발자 도구

https://developer.mozilla.org/ko/

https://developer.chrome.com/docs/devtools/css/

https://emmet.io/

https://docs.emmet.io/cheat-sheet/



