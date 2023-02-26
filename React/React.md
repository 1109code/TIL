# React

## 2강

### npx - execute npm package binaries

```
$ npx create-react-app <your-project-name>
```

=> npx : npm 패키지 설치 이후 실행 execute까지 해주는 명령어



```
# 경로 변경
$ cd my-app

# 애플리케이션 실행
$ npm start
```



## 3강

### JSX

A syntax extension to JavaScript => 자바스크립트 확장 문접

JavaScript + XML / HTML



### JSX의 역할

내부적으로 xml, html을 javascript로 변환

```jsx
React.createElement(
	type,
	[props],
	[...children]
)
```

리액트에서 JSX를 쓰는것이 필수는 아니지만 생산성, 가독성 올라가므로 쓰는게 편리함



### JSX의 장점

* 코드가 간결해짐
* 가독성 향상
* 버그를 발견하기 쉬움
* Injection Attacks 방어 (보안성 올라감)

injection : 입력창에 코드 넣어서 실행되는 것

SSS 방지



### JSX 사용법

모든 JavaScript 문법 지원 + XML / HTML

중간에 javascript 쓰고 싶으면 중괄호 써서 쓰면 됨



## 4강 Rendering Element

Element : 어떤 물체를 구성하는 성분

Elements are the smallest building blocks of React apps.

리액트 앱을 구성하는 가장 작은 블록



React Elements  / DOM Elements



Elements는 화면에서 보이는 것들을 기술

```jsx
const element = <h1>Hello, wowrld</h1>;
```

Elements의 생김새

리액트 Elements는 자바스크립트 객체 형태로 존재 => 일반적인 자바스크립트 객체 ,한번 생성되면 바꿀 수 없음(불변성)



리액트 엘리먼트는 자바스크립트 객체로 존재

![image-20230108150013723](C:\Users\SSAFY\Desktop\GIT\TIL\React\React.assets\image-20230108150013723.png)

![image-20230108150050852](C:\Users\SSAFY\Desktop\GIT\TIL\React\React.assets\image-20230108150050852.png)



리액트 엘리먼트는 우리눈에 실제로 보이는 사실을 기술



### Elements의 특징

React elements are immutable(불변성)

Elements 생성 후에는 children이나 attributes를 바꿀 수 없다.



Component(붕어빵 틀)로 구워져 나온 Element(붕어빵)는 못바꾸는것 처럼



변경하고 싶으면 새로운 Element를 만듬!

화면이 얼마나 자주 갱신되느냐가 속도 차이



### Elemtns 렌더링 하기

```html
<div id="root"></div>
```



### 렌더링된 Element 업데이트 하기

![image-20230108150548496](C:\Users\SSAFY\Desktop\GIT\TIL\React\React.assets\image-20230108150548496.png)



## 5강 Components and Props

### Components

React는 Component-Based

레고 블록 조립하듯 컴포넌트들을 모아서 개발

객체지향까지는 아니지만 비슷한 개념



### Props

Prop이 여러개!

Prop : Property(속성)

Component의 속성

컴포넌트에 전달할 다양한 정보를 담고 있는 자바스크립트 객체



### Props의 특징

Read-Only : 값을 변경 할 수 없다.

새로운 값을 컴포넌트에 전달하여 새로 Element를 생성

JavaScript의 속성



pure : 입력값(input)을 변경하지 않으면, 같은 입력값에 대해서는 항상 같은 출력값(ouput)을 리턴

Impure : 입력값(input)을 변경



All React components must act like pure functions with respect to their props.

모든 리액트 컴포넌트는 그들의 Props에 관해서는 Pure 함수 같은 역할을 해야한다.

모든 리액트 컴포넌트는 Props를 직접 바꿀 수 없고, 같은 Props에 대해서는 항상 같은 결과를 보여줄것!



### Props 사용법

js : 정수, 변수, 다른 컴포넌트 등이 들얼갈 때는 중괄호로 감싸야함

jsx사용 시 간단하게 컴포넌트 props 넣을 수 있음



### Function Component

간단한 코드를 가짐

### Class Component

React.Component를 상속 받아 만듬



### Component의 이름

Component 이름은 항상 대문자로 시작해야 함

react는 소문자로 시작되는 함수를 DOM으로 인식



### Component 렌더링


### Component 합성

Component안에 또 다른 Component

복잡한 화면을 여러 개의 Component로 나눠서 구현 가능



### Component 추출

큰 컴포넌트를 산산조각냄

재사용성 증가

component작아질수록 기능과 목적 명확

개발속도 증가

재사용 가능한 Component를 많이 가지고 있을 수록 개발 속도가 빨라짐



## 6강. State and Lifecycle

### State

리액트 Component의 상태

리액트 Component의 데이터

리액트 Component의 변경 가능한 데이터

state는 개발자가 정의

렌더링이나 데이터 흐름에 사용되는 값만 state에 포함시켜야 함

state는 JavaScript 객체이다



constructor : 생성자

this.state

state는 직접 수정 할 수 없다.(하면 안된다)

setState로 수정



this.setState({

​	name: 'Inje'

});



### LifeCycle(생명 주기)

![image-20230108160710250](C:\Users\SSAFY\Desktop\GIT\TIL\React\React.assets\image-20230108160710250.png)

 Component가 계속 존재하는 것이 아니라, 시간의 흐름에 따라 생성되고 업데이트 되다가 사라진다.



## 7강. Hooks

### Hooks

Function Component : state 사용 불가, Lifecylce에 따른 기능 구현 불가 => Hookds로 구현

원래 존재하는 기능에 갈고리 걸고 끼어들어가 수행되는 것

Hooks : state 고나련 함수, Lifecycle 관련 함수, 최적화 관련 함수



### useState()

state를 사용하기 위한 Hook



### useEffect()

side effect를 수행하기 위한 hook

side effect = 부작용, 의도치 않는 코드가 실행되서 버그 발생할 때

react에서는 부정적인 의미는 아님(효과, 영향)

다른 컴포넌트에 영향을 미칠 수 잇으며, 렌더링 중에는 작업이 완료될 수 없기 때문

리액트의 함수 컴포넌트에서 side effect를 실행할 수 있게 해주는 hook

useEffect(이펙트 함수 의존성 배열);

의존성 배열 : effect가 의존하고 있는 배열

의존성 배열을 생략하면 컴포넌트가 업데이트 될 때 마다 호출



### useMemo()

Memoized value를 리턴하는 hook

Memoization : 최적화를 위해 사용하는 개념, 비용이 높은 연산량 많은 결과 저장해놨다가 다음에 다시 호출

빠른 렌더링 속도

렌더링이 일어나는 동안 실행



의존성 배열을 넣지 않을 경우, 매 렌더링마다 함수가 실행 됨

의존성 배열이 빈 배열일 경우, 컴포넌트 마운트 시에만 호출 됨



### useCallback()

useMemo() Hook과 유사하지만 값이 아닌 함수를 반환



동일한 역할을 하는 두 줄의 코드

useCallback(함수, 의존성 배열);

useMemo(() => 함수, 의존성 배열);



### useRef()

Reference를 사용하기 위한 hook

특정 컴포넌트에 접근할 수 있는 객체

refObject.current : 현재 참조하고 있는 Element



useRef() Hook은 내부의 데이터가 변경되었을 때 별도로 알리지 않는다



### Callback ref



### Hook의 규칙

1. Hook은 무조건 최상위 레벨에서만 호출해야 한다.

리액트 함수 component의 최상위 레벨

중첩된 컴포넌트에서 호출하면 안됨



2. Hook은 컴포넌트가 렌더링될 때 마다 매번 같은 순서로 호출되어야 한다.

리액트 함수 컴포넌트에서만 Hook을 호출해야 한다.



훅 규칙 강제하도록 하는 플러그인

eslint-plugin-react-hooks

https://www.npmjs.com/package/eslint-plugin-react-hooks



### Custom Hook 만들기

여러 컴포넌트에서 반복 사용되는 로직을 훅으로 만들어 재사용하기 위함



### Custom Hook을 만들어야 하는 상황



### Custom Hook 추출하기

이름이 use로 시작하고 내부에서 다른 Hook을 호출하는 하나의 자바스크립트 함수

단순한 함수와도 같지만 use로 시작해서 react hook이라는 것을 나타내줌

hook의 두가지 규칙 적용



### Custom Hook 사용하기

Custom Hook의 이름은 꼭 use로 시작해야 함

여러 개의 컴포넌트에서 하나의 Custom Hook을 사용할 때 컴포넌트 내부에 있는 모든 state와 effects는 전부 분리되어 있음

각 Custom Hook 호출에 대해서 분리된 state를 얻게 됨

각 Custom Hook의 호출 또한 완전히 독립적임



### Hook들 사이에서 데이터를 공유하는 방법







