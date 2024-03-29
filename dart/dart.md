## Hello world

print하고 ; 달아줘야 됨

Format이 자동으로 달아주는 거 없음 => dart에서 일부로 안 쓸 때가 있어서 그럼



## The Var Keyword

var은 updated될 수 있음

수정할 땐 같은 타입으로만 됨



### 변수를 만드는 2가지 방법

명시적으로 변수의 타입 지정

var 키워드 사용

=> 함수나 메소드 내부에 지역 변수를 선언할 때에는 var 사용, class에서 변수나 property를 선언할 떄에는 타입 지정

var을 쓰던 String을 쓰던 변수를 업데이트 할 수 있음



## Dynamic Type

변수 타입이 dynmic이면 

dynamic 변수를 뭔가를 하고 싶으면 type 확인 해야함

이상적으로는 피하는게 좋음, 진짜 필요할 때만



## Nullable Variables

null safety : 개발자가 null값을 참조할 수 없도록 하는 것

null 참조하면 런타임 에러 발생

언어에서 null을 삭제할 순 없음, 중요해서

dart에서는 어떤 변수가 null이 될 수 있음을 정확히 표시해야 함

```dart
void main() {
	String? nico = 'nico';
	nico = null
    if (nico != null) {
    }
    nico?.isNotEmpty;
}
```

null이 될 수 도 있게 하려면 ? 추가

null인지 check 해야함

기본적으로 모든 변수는 non-nullable임



## Final Variables

var 대신 final하면 변수 수정 불가 (const와 유사)



## Late Variables

```dart
void main() {
    late final String name;
    // do something, go to api
    name = 'nico';
}
```

데이터 없이 변수를 만들고 API에서 데이터를 받아 변수에 넣어줌

final 변수이기 때문에 딱 한번만 할당 가능

late로 하면 값 할당하기 전에 접근 불가능

대부분의 겨우에는 final 하겠지만 value 모를 때 도 있음



## Constant Variables

js나 typescript의 const와 다름

js const는 오히려 final과 유사



dart에서 const는 compile time constant를 만듬

compile time constant : const는 compile-time에 알고 있는 값이어야 함

```dart
void main() {
const API = fetchApi();
}
```

앱을 올리기전에 값을 알고 있으면 const

사용자가 화면에서 입력해야 하는 값이면 final 혹은 var로 해야됨

애을 컴파일해서 앱스토어에 올리기 전에 알고 있는 값 ex : max_allowed_price를 쓸 때는 const 쓰면 됨

compile time : 앱스토어에 올리기 전



## Recap

void main() {

 int i = 12;

 var name = 'la';

 i = 1212121212;

 name = 'lalalala';

둘 다 수정 가능

dart공식 문서 : var 사용 권장

type 변수 선언은 class의 property를 작성할 때 사용하는게 권장

메소드나 작은 함수에서 사용할 땐 ㅍㅁㄱdl ska

어차피 컴파러가 이미 암

변수 수정을 원치 않으면 final사용

 final name2 = 'son';

 dynamic name3;

name이 어떤 값을 가질 지 모를 때

정확히 정해지지 않음

 const api_key = '12121212'; // 컴파일 할 때 알고 있음

final 은 compile 과정에서 선언할 수 있음

const는 compile 전에 알고 있어야함

null safety

기본적으로 dart의 모든 변수는 not nullable



null 일 수 도 있을 거 같으면 ? 추가

```dart
void main() {
	String? name = 'nico';
	name = null;
    if(name != null) {
        name?.isEmpty
    }
	name?.isEmpty;
}
```

late는 아직 어떤 데이터가 올지 모른다고 말해 주는 것

```dart
void main(0 {
	late final String name;
	name = '12';
	print(name);
})
```

late 하고 접근하기 전에 변수 할당 해야함

api에서 데이터 가져오는 것과 같이 아직 정의 안됐을 때 씀



# Basic Data Types

```dart
void main() {
  String name = "son";
  bool alive = true;
  int age = 12;
  double money = 69.99;
  num x = 12;
  x = 1.1;
}
```

모든 type은 object, class로 되어 있음

num 은 정수일 수 도 있고 실수 일 수 도 있음



## Lists

```dart
void main() {
  var numbers = [1, 2, 3, 4];
}
```

collection if 와 collection for 지원

list 요소 맨 뒤에 ,로 마무리 하면 보기 편해짐



### collection if

if로 존재할 수도 안할 수도 있는 요소를 가지고 만들 수 있음

```dart
void main() {
  var giveMeFive = true;
  List<int> numbers = [
    1,
    2,
    3,
    4,
    if (giveMeFive) 5,
  ];
  numbers.add(1);
  print(numbers);
  print(numbers.first);
  print(numbers.last);
}
```



## String Interpollation

큰 따옴표를 사용해도 되고 작은 따옴표 사용해도 되고 달러 기호 뒤에 변수 사용하면 됨

계산을 실행할 때의 문법은 조금 다름

단수히 변수를 담을 거면 $변수명 하면 됨

계산을 하고 싶으면 ${age + 2} 하면 됨

```dart
void main() {
  var name = 'son';
  var age = 10;
  var greeting = 'Hello everyone, my name is $name and I\'m ${age + 2}'';
  print(greeting);
}
```



## collection for

```dart
void main() {
  var oldFriends = ['nico', 'lynn'];
  var newFriends = [
    'son',
    'kwon',
    'kim',
    for (var friend in oldFriends) "하트 $friend",
  ];
  print(newFriends);
}
// [son, kwon, kim, 하트 nico, 하트 lynn]
```



## Maps

모든건 object로 부터 오기 때문에 object는 모든 타입임

```dart
void main() {
  var palyer = {
    'name': 'son',
    'xp': 19.99,
    'superpower': false,
  };
  Map<int, bool> player2 = {
    1: true,
    2: false,
    3: true,
  };
  Map<List<int>, bool> palyer3 = {
    [1, 2, 3, 5]: true,
  };
}
```

명시적, 암시적으로 정할 수 있음

Map으로 하면 명시적으로 알려줌

var쓰면 컴파일러가 유추함



## Sets

```dart
void main() {
  Set<int> numbers = {1, 2, 3, 4};
  numbers.add(1);
  numbers.add(1);
  numbers.add(1);
  print(numbers); // 1, 2, 3, 4

  List<int> numbers2 = [1, 2, 3, 4];
  numbers2.add(1);
  numbers2.add(1);
  numbers2.add(1);
  print(numbers2); // 1, 2, 3, 4, 1, 1, 1
}
```

sets는 unique하다는 차이점이 있음

list : python의 list와 유사

set : python의 tuple과 유사



## Defining a function

void : return 값이 없다

=> : return

```dart
String sayHello(String potato) => "Hello $potato nice to meet you";

void main() {
  print(sayHello('son'));
}
```

코드 한줄 밖에 없으면 fat arrow syntax 사용



## Named Parameters

```dart
String sayHello(String name, int age, String country) {
  return "Hello $name, you are $age, and you come from $country";
}

void main() {
  print(sayHello('son', 29, 'Korea'));
}
```

유저들이 요소들의 순서를 기억 못 할 수 있기 때문에 좋은 방법은 아님

=> Named Parameters 필요

순서를 기억하는게 아님

```dart
String sayHello(
    {String name = 'anon', int age = 99, String country = 'korea'}) {
  return "Hello $name, you are $age, and you come from $country";
}

void main() {
  print(sayHello(
    age: 12,
    country: 'korea',
    name: 'nico',
  ));
}
```

null 이면 어쩔건데??? (null safety)

=> default value 정하기



```dart
String sayHello({
  required String name,
  required int age,
  required String country,
}) {
  return "Hello $name, you are $age, and you come from $country";
}

void main() {
  sayHello(
    age: 12,
    country: 'korea',
    name: 'son',
  );
}
```

default를 정하고 싶지 않으면?

=> required : dart가 반드시 required parameter 필요하다고 인지



## Recap

positional parameter : 필수 parameter있으면 그냥 함수 못 부름

각자의 위치를 기억해야 함

name parameter : parameter 중괄호로 감싸고 선언

=> position이 중요한게 아니라 이름 명시하면 됨

순서는 상관 없어짐

required 쓰면 null 피할 수 있음

default값 지정



## Optional Positional Parameters

```dart
String sayHello(String name, int age, [String? country = 'korea']) =>
    'Hello $name, you are $age years old from $country';

void main() {
  var results = sayHello(
    'son',
    28,
  );
  print(results);
}
```



## QQ Operator

```dart
String capitalizeName(String? name) {
  if (name != null) {
    return name.toUpperCase();
  }
  return 'ANON';
}

void main() {
  capitalizeName('son');
  capitalizeName('son');
}
```

null 일지 모르는 값에 toUpperCase 할 수 없음

```dart
String capitalizeName(String? name) =>
    name != null ? name.toUpperCase() : 'ANON';

void main() {
  capitalizeName('son');
  capitalizeName('son');
}
```

```dart
String capitalizeName(String? name) => name?.toUpperCase() ?? 'ANON';

void main() {
  capitalizeName('son');
  capitalizeName('son');
}
```

```dart
void main() {
  String? name;
  name ??= 'son';
}
```



## Typedef

```dart
typedef ListOfInts = List<int>;

ListOfInts reverseListOfNumbers(ListOfInts list) {
  var reversed = list.reversed;
  return reversed.toList();
}

void main() {
  print(reverseListOfNumbers([1, 2, 3]));
}
```

```dart
typedef UserInfo = Map<String, String>;

String sayHi(UserInfo userInfo) {
  return "Hi ${userInfo['name']}";
}

void main() {
  sayHi({"ssdfdsfsdfds": 'nico'});
}
```



## Dart Class

Class 생성시는 명시적으로 변수 정의

new 할 필요 없음(해도되는데 안해도됨)

변수 변경을 원치 않으면 final

```dart
class Player {
  final String name = 'son';
  int xp = 1500;

  void sayHello() {
    print("Hi my name is $name");
  }
}

void main() {
  var player = Player();
  player.sayHello();
}
```

dart class에서는 this 쓸 필요 없음, this 써도 작동은 하는데 class method 내에서 this 쓸 필요 없음

class 내에 동일 변수명 있지 않은 이상



## Constructor

```dart
class Player {
  final String name;
  int xp;

  Player(this.name, this.xp);

  void sayHello() {
    print("Hi my name is $name");
  }
}

void main() {
  var player = Player("son", 1500);
  player.sayHello();
  var player2 = Player("kim", 2500);
  player2.sayHello();
}
```



## Named Constructor Parameters

positional parameter 너무 많으면 헷갈림

```dart
class Player {
  final String name;
  int xp;
  String team;
  int age;

  Player(
      {required this.name,
      required this.xp,
      required this.team,
      required this.age});

  void sayHello() {
    print("Hi my name is $name");
  }
}

void main() {
  var player = Player(
    name: "son",
    xp: 1200,
    team: 'blue',
    age: 12,
  );
  var player2 = Player(
    name: "kim",
    xp: 2500,
    team: 'blue',
    age: 12,
  );

  player.sayHello();
  player2.sayHello();
}
```





## Named Constructors

:(콜론) 문법으로 constructor 초기화 생성자 생성 가능

```dart
class Player {
  final String name;
  int xp, age;
  String team;

  Player(
      {required this.name,
      required this.xp,
      required this.team,
      required this.age});

  Player.createBluePlayer({
    required String name,
    required int age,
  })  : this.age = age,
        this.name = name,
        this.team = 'blue',
        this.xp = 0;

  Player.createRedPlayer(String name, int age)
      : this.age = age,
        this.name = name,
        this.team = 'red',
        this.xp = 0;

  void sayHello() {
    print("Hi my name is $name");
  }
}

void main() {
  var player = Player.createBluePlayer(
    name: "son",
    age: 12,
  );
  var player2 = Player.createRedPlayer('kim', 12);

  player.sayHello();
  player2.sayHello();
}
```



## Recap

```dart
class Player {
  final String name;
  int xp;
  String team;

  Player.fromJson(Map<String, dynamic> playerJson)
      : name = playerJson['name'],
        xp = playerJson['xp'],
        team = playerJson['team'];

  void sayHello() {
    print("Hi my name is $name");
  }
}

void main() {
  var apiData = [
    {
      "name": "son",
      "team": "red",
      "xp": 0,
    },
    {
      "name": "lynn",
      "team": "red",
      "xp": 0,
    },
    {
      "name": "dar",
      "team": "red",
      "xp": 0,
    },
  ];

  apiData.forEach((playerJson) {
    var player = Player.fromJson(playerJson);
    player.sayHello();
  });
}
```



## Cascade Notation

```dart
class Player {
  String name;
  int xp;
  String team;

  Player({
    required this.name,
    required this.xp,
    required this.team,
  });

  void sayHello() {
    print("Hi my name is $name");
  }
}

void main() {
  var son = Player(
    name: 'son',
    xp: 1200,
    team: 'red',
  );
  var potato = son
    ..name = 'kim'
    ..xp = 120000
    ..team = 'blue'
    ..sayHello();
}
```



## Enums

```dart
enum Team { red, blue }

enum XPLevel { beginner, medium, pro }

class Player {
  String name;
  XPLevel xp;
  Team team;

  Player({
    required this.name,
    required this.xp,
    required this.team,
  });

  void sayHello() {
    print("Hi my name is $name");
  }
}

void main() {
  var son = Player(
    name: 'son',
    xp: XPLevel.pro,
    team: Team.red,
  );
  var potato = son
    ..name = 'kim'
    ..xp = XPLevel.beginner
    ..team = Team.blue
    ..sayHello();
}
```



## Abstract classes

청사진(blueprint)

abstrct method는 상속받는 모든 클래스가 가지고 있어야 하는 메소드 정의

```dart
abstract class Human {
  void walk();
}

enum Team { red, blue }

enum XPLevel { beginner, medium, pro }

class Player extends Human {
  String name;
  XPLevel xp;
  Team team;

  Player({
    required this.name,
    required this.xp,
    required this.team,
  });

  void walk() {
    print('I\'m walking');
  }

  void sayHello() {
    print("Hi my name is $name");
  }
}

class Coach extends Human {
  void walk() {
    print('the coach is walking');
  }
}

void main() {
  var son = Player(
    name: 'son',
    xp: XPLevel.pro,
    team: Team.red,
  );
  var potato = son
    ..name = 'kim'
    ..xp = XPLevel.beginner
    ..team = Team.blue
    ..sayHello();
}
```



## Inheritance

super로 상위 클래스 메서드 접근

```dart
class Human {
  final String name;
  Human({required this.name});
  void sayHello() {
    print("Hi my name is $name");
  }
}

enum Team { blue, red }

class Player extends Human {
  final Team team;

  Player({required this.team, required String name}) : super(name: name);

  @override
  void sayHello() {
    super.sayHello();
    print('and I play for ${team}');
  }
}

void main() {
  var player = Player(
    team: Team.red,
    name: 'son',
  );

  player.sayHello();
}
```



## Mixins

생성자가 없는 클래스

```dart
class Strong {
  final double strengthLevel = 1500.99;
}

class QuickRunner {
  void runQuick() {
    print("ruuuuuuuun!");
  }
}

class Tall {
  final double height = 1.99;
}

enum Team { blue, red }

class Player with Strong, QuickRunner, Tall {
  final Team team;

  Player({
    required this.team,
  });
}

class Horse with Strong, QuickRunner {}

class Kid with QuickRunner {}

void main() {
  var player = Player(
    team: Team.red,
  );
}
```



