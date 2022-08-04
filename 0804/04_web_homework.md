# 1. CSS flex-direction

**flex-direction: row;**

> 우리가 글씨를 읽는 좌에서 우의 수평방향

**flex-direction: row-reverse;**

> 우리가 글씨를 읽는 반대인 우에서 좌의 수평방향

**flex-direction: column**;

> 위에서 아래로의 수직방향

**fex-direction: column-reverse;**

> 아래에서 위로의 수직방향



# 2. Bootstrap flex-direction

flex-direction: row;  == **flex-row**

flex-direction: row-reverse; == **flex-row-reverse**

flex-direction: column; == **flex-column**

flex-direction: column-reverse; == **flex-column-reverse**



# 3. align-items

align-items: flex-start;

> main 축의 수직 방향을 기준으로 최상단 배치

align-items: flex-end;

> main 축의 수직 방향을 기준으로 최하단 배치

align-items: center;

> main 축의 수직 방향을 기준으로 중앙에 배치

align-items: baseline;

> 모든 요소들의 밑변을 기준으로 정렬



# 4. flex-flow

**(1) flex-direction, flex-wrap**



# 5. Bootstrap Grid System

(a) : container

(b) : row

(c) : breakpoint가 들어갈 수 있다

반응형 제작을 위해 6개의 breakpoint가 있는데 각각 sm, md, lg, xl, xxl이 그 예이다. 

화면의 크기가 이에 해당하는 너비가 되었을 때 그리드의 설정 또한 이에 맞춰 변형된다.

(d) : 해당 값에 breakpoint에 따라 요소가 grid에서 차지 할 column의 크기를 지정할 수 있다.