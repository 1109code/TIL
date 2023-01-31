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
      backgroundColor: Colors.white,
      floatingActionButton: renderFloatingActionButton(),
      // SafeArea : UI 화면안에 잘 들어오게
      body: Column(
        children: [
          Calendar(focusedDay: focusedDay),
        ],
      ),
    );
  }

  renderFloatingActionButton() {
    return Container(
      decoration: BoxDecoration(
        shape: BoxShape.circle,
        border: Border.all(
            color: const Color.fromARGB(255, 100, 92, 170),
            width: 3,
            style: BorderStyle.solid),
      ),
      width: 48,
      height: 48,
      child: FloatingActionButton.small(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => const ScheduleScreen()),
          );
        },
        // focusColor: Colors.black,
        backgroundColor: Colors.white,
        child: const Icon(
          Icons.add,
          color: Color.fromARGB(255, 100, 92, 170),
          size: 40,
        ),
      ),
    );
  }
}
