import 'package:hello_world/component/calendar.dart';
import 'package:hello_world/component/schedule_bottom_sheet.dart';
import 'package:hello_world/component/schedule_card.dart';
import 'package:hello_world/component/today_banner.dart';
import 'package:hello_world/const/colors.dart';
import 'package:flutter/material.dart';
import 'package:hello_world/database/drift_database.dart';
import 'package:get_it/get_it.dart';
import 'package:hello_world/model/schedule_with_color.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  DateTime selectedDay = DateTime.utc(
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
            ),
            const SizedBox(
              height: 8,
            ),
            _ScheduleList(
              selectedDate: selectedDay,
            ),
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
            return ScheduleBottomSheet(
              selectedDate: selectedDay,
            );
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
  final DateTime selectedDate;

  const _ScheduleList({
    Key? key,
    required this.selectedDate,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Padding(
        padding: const EdgeInsets.symmetric(
          horizontal: 8,
        ),
        // 스크롤 가능
        child: StreamBuilder<List<ScheduleWithColor>>(
            stream: GetIt.I<LocalDatabase>().watchSchedules(
              selectedDate,
            ),
            builder: (context, snapshot) {
              print(snapshot.data);
              if (!snapshot.hasData) {
                return const Center(child: CircularProgressIndicator());
              }
              if (snapshot.hasData && snapshot.data!.isEmpty) {
                return const Center(
                  child: Text('스케줄이 없습니다.'),
                );
              }

              return ListView.separated(
                itemCount: snapshot.data!.length,
                separatorBuilder: (context, index) {
                  return const SizedBox(
                    height: 8,
                  );
                },
                itemBuilder: (context, index) {
                  final scheduleWithColor = snapshot.data![index];

                  return Dismissible(
                    key: ObjectKey(scheduleWithColor.schedule.id),
                    direction: DismissDirection.endToStart,
                    onDismissed: (DismissDirection direction) {
                      GetIt.I<LocalDatabase>()
                          .removeSchedule(scheduleWithColor.schedule.id);
                    },
                    child: GestureDetector(
                      onTap: () {
                        showModalBottomSheet(
                          context: context,
                          // 최대로 올라감
                          isScrollControlled: true,
                          builder: (_) {
                            return ScheduleBottomSheet(
                              selectedDate: selectedDate,
                              scheduleId: scheduleWithColor.schedule.id,
                            );
                          },
                        );
                      },
                      child: ScheduleCard(
                        startTime: scheduleWithColor.schedule.startTime,
                        endTime: scheduleWithColor.schedule.endTime,
                        content: scheduleWithColor.schedule.content,
                        color: Color(
                          int.parse(
                            'FF${scheduleWithColor.categoryColor.hexCode}',
                            radix: 16,
                          ),
                        ),
                      ),
                    ),
                  );
                },
              );
            }),
      ),
    );
  }
}
