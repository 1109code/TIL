sql 반

sql 교재에서 50% 이상 나옴

m : 1에서 나옴

데이터 정의 언어 delete 없었음

데이터를 삭제할 때

sql에 들어갈 수 있는 데이터 타입

insert into

n: 1에 필요한 관계 정의 fk

참조할 모델, 테이블 이름

on_delete 반드시 필요 ***



comment

article = models.Foreignkey(Artice, on_delete=models.CASCADE)

related_name 안썼을 때

comment_set



스키마, 레코드



where, like로 접근

교재 나와있는것만 따라해도 됨!

%로 필터링



sql로 삭제할 때

record 삭제할땐 뭘 써야되는지





db

M: N 을 하나로도 만들 수 있음

중계테이블 직접 만들어줘도 되고 직접 만들어도됨

M: N 은 self 있어서 꼭 두개 sql있을 필요 X

related manager를 사용할 수 있음

ascending 오름차순, descending 내림차순

shell_plus로 확인해보셈



sql에서 table이름 바꾸려면 어떻게?(change로 못바꿈!)

DDL 언어에 나옴

M: N self로 만들 수 있음



sql문 교재에 있는거 한번씩 실행 시켜보기



sql문 django orm 문을 sql로 sql을 django로 할 줄 알아야함

오늘 한 like 꼭 직접 해보고 가기

역참조 과정



많은 error를 보고 가셈