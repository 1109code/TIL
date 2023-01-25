import 'package:drift/drift.dart';

class Schedules extends Table {
  // PRIMARY KEY
  IntColumn get id => integer().autoIncrement()();

  // 내용
  TextColumn get content => text()();

  // 일정 날짜
  DateTimeColumn get date => dateTime()();

  // 시작 시간
  IntColumn get startTime => integer()();

  // 끝 시간
  IntColumn get endTime => integer()();

  // Category Color Table ID
  IntColumn get colorId => integer()();

  // 생성날짜
  // 값을 넣어주면 넣어준 값으로 배정되긴 함
  DateTimeColumn get createdAt => dateTime().clientDefault(
        () => DateTime.now(),
      )();
}
