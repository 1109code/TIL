import 'package:flutter/material.dart';
import 'package:table_calendar/table_calendar.dart';

class Calendar extends StatefulWidget {
  const Calendar({super.key});

  @override
  State<Calendar> createState() => _CalendarState();
}

// https://medium.flutterdevs.com/display-dynamic-events-at-calendar-in-flutter-22b69b29daf6
class _CalendarState extends State<Calendar> {
  // 오늘 날짜
  DateTime selectedDay = DateTime(
    DateTime.now().year,
    DateTime.now().month,
    DateTime.now().day,
  );

  // 이벤트 간격 일정 유지
  Map<DateTime, List<dynamic>>? _events;
  List<dynamic> _selectedEvents;
  // 내가 보고 있는 날짜
  DateTime focusedDay = DateTime.now();

  @override
  void initState() {
    super.initState();
    _events = {};
    _selectedEvents = [];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.white,
        centerTitle: true,
        title: const Text(
          "DOG DAK",
          style: TextStyle(
            fontSize: 24,
            color: Colors.black54,
          ),
        ),
      ),
      // 달력 불러오기
      body: TableCalendar(
        // 언어 설정
        locale: 'ko_KR',
        // 필수값 (시작, 마지막, 오늘 날짜)
        firstDay: DateTime.utc(2021, 1, 1),
        lastDay: DateTime.utc(2030, 12, 31),
        focusedDay: focusedDay,
        headerStyle: const HeaderStyle(
          decoration: BoxDecoration(
            color: Color.fromRGBO(100, 92, 170, 1),
          ),
          // 2주단위로 바꾸는 버튼 안보이게
          formatButtonVisible: false,
          // 제목 중앙정렬
          titleCentered: true,
          // 제목 스타일
          titleTextStyle: TextStyle(
            fontSize: 18,
            fontWeight: FontWeight.w800,
            color: Colors.white,
          ),
          // Chevron
          leftChevronIcon: Icon(
            Icons.chevron_left,
            color: Colors.white,
            // size: 30,
          ),
          rightChevronIcon: Icon(
            Icons.chevron_right,
            color: Colors.white,
            // size: 30,
          ),
        ),
        // 요일 디자인
        daysOfWeekHeight: 35,
        daysOfWeekStyle: const DaysOfWeekStyle(
            // 평일
            weekdayStyle: TextStyle(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.w600,
            ),
            // 주일
            weekendStyle: TextStyle(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.w600,
            ),
            decoration: BoxDecoration(color: Color.fromRGBO(195, 177, 228, 1))),
        // 달력 일 디자인
        calendarStyle: CalendarStyle(
          // 휴일 디자인
          holidayTextStyle: const TextStyle(color: Colors.red),
          // 오늘 디자인
          todayDecoration: BoxDecoration(
            shape: BoxShape.circle,
            border: Border.all(
              width: 4,
              color: const Color.fromRGBO(100, 92, 170, 0.9),
            ),
          ),
          todayTextStyle: const TextStyle(
            color: Colors.black,
          ),
          // 선택 요일 디자인
          selectedDecoration: const BoxDecoration(
            shape: BoxShape.circle,
            color: Color.fromRGBO(100, 92, 170, 0.5),
          ),
          selectedTextStyle: const TextStyle(
            color: Colors.black,
          ),
          tableBorder: const TableBorder(
            verticalInside: BorderSide(
              color: Color.fromRGBO(100, 92, 170, 0.3),
            ),
            horizontalInside: BorderSide(
              color: Color.fromRGBO(100, 92, 170, 0.3),
            ),
          ),
        ),
        // 달력에서 일자 선택 시
        onDaySelected: (DateTime selectedDay, DateTime focusedDay) {
          // 선택한 날짜를 초기화 하고, 보고있는 날짜도 변경
          setState(() {
            this.selectedDay = selectedDay;
            this.focusedDay = focusedDay;
          });
        },

        // onDaySelected: (date, events, holidays) {
        //   setState(() {
        //     _selectedEvents = events;
        //   });
        // },
        // 선택한 날짜의 색상을 변경
        selectedDayPredicate: (DateTime day) {
          return isSameDay(selectedDay, day);
        },
        calendarBuilders: CalendarBuilders(
          selectedBuilder: (context, date, events) => Container(
            margin: const EdgeInsets.all(4),
            alignment: Alignment.center,
            decoration: BoxDecoration(
              color: Colors.purple,
              borderRadius: BorderRadius.circular(10),
            ),
            child: Text(
              date.day.toString(),
              style: const TextStyle(color: Colors.white),
            ),
          ),
          todayBuilder: (context, date, events) => Container(
              margin: const EdgeInsets.all(4),
              alignment: Alignment.center,
              decoration: BoxDecoration(
                color: Colors.orange,
                borderRadius: BorderRadius.circular(10),
              ),
              child: Text(
                date.day.toString(),
                style: const TextStyle(
                  color: Colors.white,
                ),
              )),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        backgroundColor: Colors.black,
        onPressed: _showAddDialog,
        child: const Icon(Icons.add),
      ),
    );
  }
}
