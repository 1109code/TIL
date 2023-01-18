import 'package:flutter/material.dart';
import 'package:syncfusion_flutter_calendar/calendar.dart';

class HomeScreen2 extends StatefulWidget {
  const HomeScreen2({super.key});

  @override
  State<HomeScreen2> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen2> {
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
        body: Container(
          child: SfCalendar(
            // day, month, workweek, 월별 캘린더 뷰 선택
            view: CalendarView.month,
            // 하단 할일
            monthViewSettings: const MonthViewSettings(showAgenda: true),
          ),
        ));
  }
}
