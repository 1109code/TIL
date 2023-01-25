import 'package:flutter/material.dart';
import 'package:hello_world/const/colors.dart';
import 'package:table_calendar/table_calendar.dart';

class Calendar extends StatelessWidget {
  final DateTime? selectedDay;
  final DateTime focusedDay;
  final OnDaySelected? onDaySelected;

  const Calendar({
    super.key,
    this.selectedDay,
    required this.focusedDay,
    required this.onDaySelected,
  });

  @override
  Widget build(BuildContext context) {
    // 계속 사용할 박스 데코
    final defaultBoxDeco = BoxDecoration(
      borderRadius: BorderRadius.circular(6),
      color: Colors.grey[200],
    );
    final defaultTextStyle = TextStyle(
      color: Colors.grey[600],
      fontWeight: FontWeight.w700,
    );

    return TableCalendar(
      locale: 'ko_KR',
      // 보여줘야 할 날짜
      focusedDay: focusedDay,
      firstDay: DateTime(1800),
      // 마지막 날짜
      lastDay: DateTime(3000),
      // 헤더
      headerStyle: const HeaderStyle(
        formatButtonVisible: false,
        titleCentered: true,
        titleTextStyle: TextStyle(
          fontWeight: FontWeight.w700,
          fontSize: 16,
        ),
      ),
      calendarStyle: CalendarStyle(
        // 오늘 날짜 하이라이트
        isTodayHighlighted: false,
        // 날짜 들어있는 컨테이너 데코
        defaultDecoration: defaultBoxDeco,
        weekendDecoration: defaultBoxDeco,
        selectedDecoration: BoxDecoration(
          color: Colors.white,
          borderRadius: BorderRadius.circular(6),
          border: Border.all(
            color: PRIMARY_COLOR,
            width: 1,
          ),
        ),
        defaultTextStyle: defaultTextStyle,
        weekendTextStyle: defaultTextStyle,
        // 나머지 값들은 그대로 하고 새로운 것만 덮어쓰기
        selectedTextStyle: defaultTextStyle.copyWith(
          color: PRIMARY_COLOR,
        ),
        // 바깥 날짜 데코
        outsideDecoration: const BoxDecoration(
          shape: BoxShape.rectangle,
        ),
      ),
      // 선택된 날짜 초기화, 선택할 때 실행됨
      onDaySelected: onDaySelected,
      // 선택됐는지 비교, 선택한 날짜와 해당 연원일이 일치하면 선택 했다고 판단
      selectedDayPredicate: (DateTime date) {
        if (selectedDay == null) {
          return false;
        }
        return date.year == selectedDay!.year &&
            date.month == selectedDay!.month &&
            date.day == selectedDay!.day;
      },
    );
  }
}
