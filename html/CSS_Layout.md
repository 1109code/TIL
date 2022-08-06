# CSS Layout

* float (요즘엔 잘 안씀, ie때 씀
* flexbox(최근에는 이거 많이 씀)
* gird



## CSS layout techniques

> Display
>
> Position
>
> Float(CSS1, 1996) : 원래 Layout용은 아니 었음
>
> Flexbox(2012)
>
> Grid(2017)
>
> 기타(Responsive Web Design(2010), Media Queries(2012))

=> 뭐가 더 좋다 이런건 아님

## CSS 원칙

Inline Direction : 글자

Block Direction : 

Normal Flow 

> 모든 요소는 네모(박스모델)이고,
>
> 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)

## Float

> 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping 하도록 함
>
> 요소가 Normal flow를 벗어나도록 함

속성

> none : 기본값
>
> left : 요소를 왼쪽으로 띄움
>
> right : 요소를 오른쪽으로 띄움

## Flexbox

### CSS Flexible Box Layout

> 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
>
> 축
>
> * main axis(메인 축)
> * cross axis(교차 축)
>
> 구성 요소
>
> * Flex Container(부모 요소)
> * Flex Item(자식 요소)

> (수동 값 부여 없이)
>
> 1. 수직 정렬
> 2. 아이템의 너비와 높이 혹은 간격을 동일하게 배치

### Flex 속성

> 배치 설정
>
> * flex-direction
> * flex-wrap
>
> 공간 나누기
>
> * justify-content (main axis)
> * align-content (cross axis)
>
> 정렬
>
> * align-itmes (모든 아이템을 corss axis 기준으로)
> * align-self (개별 아이템)

### flex-direction

> Main axis 기준 방향 설정
>
> 역방향의 경우 HTML 태그 선언 순서와 시각적으로 다르니 유의 (웹 접근성에 영향)

### flex-wrap

> 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
>
> 즉, 기본적으로 컨테이너 영역을 벗어나지 않도록 함

![image-20220803100912319](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220803100912319.png)

### flex-direction * flex-wrap

> flex-direction : Main axis의 방향을 설정
>
> flex-wrap : 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
>
> flex-flow :
>
> * flex-direction 과 flex-wrap의 shorthand
> * flex-directino과 flex-

### justify-content

> Main axis를 기준으로 공간 배분

![image-20220803101414617](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220803101414617.png)



![image-20220803101607381](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220803101607381.png)



### align-content

> Cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인할 수 없음)

![image-20220803101736341](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220803101736341.png)

### justify-content & algin-content

> 공간 배분
>
> * flex-start:
> * flex-end:
> * center:
> * space-between:
> * space-around:
> * space-evenly

### algin-items

![image-20220803102422508](C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220803102422508.png)

### flex 정리

 [flex.html](..\..\..\live\web_03\flex추가자료\flex.html) 



### Flex에 적용하는 속성

> flex-grow : 남은 영역을 아이템에 분배
>
> order : 배치 순서