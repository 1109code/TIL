import 'package:dogdoc_calendar/component/calendar.dart';
import 'package:dogdoc_calendar/screen/schedule_screen.dart';
import 'package:flutter/material.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  // 선택한 날짜 초기화
  DateTime selectedDay = DateTime.utc(
    DateTime.now().year,
    DateTime.now().month,
    DateTime.now().day,
  );

  // 보여줄 월
  DateTime focusedDay = DateTime.now();

  @override
  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;
    double width = screenSize.width;
    double height = screenSize.height;

    return Scaffold(
      floatingActionButton: renderFloatingActionButton(),
      // SafeArea : UI 화면안에 잘 들어오게
      body: SafeArea(
        child: Column(
          children: [
            Calendar(focusedDay: focusedDay),
          ],
        ),
      ),
    );
  }

  FloatingActionButton renderFloatingActionButton() {
    return FloatingActionButton(
      onPressed: () {
        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const ScheduleScreen()),
        );
      },
      backgroundColor: const Color(0xFF033B0B),
      child: const Icon(
        Icons.add,
        color: Colors.white,
      ),
    );
  }
}
