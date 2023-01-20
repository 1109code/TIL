import 'package:flutter/material.dart';
import 'package:hello_world/component/calendar.dart';
import 'package:hello_world/component/schedule_bottom_sheet.dart';
import 'package:hello_world/component/schedule_card.dart';
import 'package:hello_world/component/today_banner.dart';
import 'package:hello_world/const/colors.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  DateTime selectedDay = DateTime(
    DateTime.now().year,
    DateTime.now().month,
    DateTime.now().day,
  );
  DateTime focusedDay = DateTime.now();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: renderFloatingActionButton(),
      body: SafeArea(
        child: Column(
          children: [
            Calendar(
              selectedDay: selectedDay,
              focusedDay: focusedDay,
              onDaySelected: onDaySelected,
            ),
            const SizedBox(
              height: 8,
            ),
            TodayBanner(
              selectedDay: selectedDay,
              scheduleCount: 3,
            ),
            const SizedBox(
              height: 8,
            ),
            const _ScheduleList(),
          ],
        ),
      ),
    );
  }

  FloatingActionButton renderFloatingActionButton() {
    // 버튼 누르면 아래에서 올라오게
    return FloatingActionButton(
      onPressed: () {
        // 아래에서 올라오는 페이지(기본이 최대 사이즈의 반만큼 차지)
        showModalBottomSheet(
          context: context,
          // 최대로 올라감
          isScrollControlled: true,
          builder: (_) {
            return const ScheduleBottomSheet();
          },
        );
      },
      backgroundColor: PRIMARY_COLOR,
      child: const Icon(
        Icons.add,
      ),
    );
  }

  onDaySelected(DateTime selectedDay, DateTime focusedDay) {
    setState(() {
      this.selectedDay = selectedDay;
      this.focusedDay = selectedDay;
    });
  }
}

class _ScheduleList extends StatelessWidget {
  const _ScheduleList({
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Padding(
        padding: const EdgeInsets.symmetric(
          horizontal: 8,
        ),
        // 스크롤 가능
        child: ListView.separated(
          itemCount: 100,
          separatorBuilder: (context, index) {
            return const SizedBox(
              height: 8,
            );
          },
          itemBuilder: (context, index) {
            return ScheduleCard(
              startTime: 8,
              endTime: 14,
              content: '프로그래밍 공부, $index',
              color: Colors.red,
            );
          },
        ),
      ),
    );
  }
}
