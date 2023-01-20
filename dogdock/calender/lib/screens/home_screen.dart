import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:table_calendar/table_calendar.dart';
import 'package:intl/date_symbol_data_local.dart';

// eventLoader에 쓰일 임의 clas

class Event {
  String title;

  Event(this.title);
}

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

  // 이벤트 리스트
  Map<DateTime, List<Event>> events = {
    DateTime.utc(2023, 1, 20): [Event('title'), Event('title2')],
  };

  List<Event> getEventsForDay(DateTime day) {
    return events[day] ?? [];
  }

  List<String> days = ['_', '월', '화', '수', '목', '금', '토', '일'];

  DateTime focusedDay = DateTime.now();

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
      body: Padding(
        padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 20),
        child: Column(
          children: [
            const SizedBox(
              height: 30,
            ),
            Row(
              // mainAxisAlignment: MainAxisAlignment.center,
              children: const [
                Text(
                  "짬뽕이의 캘린더",
                  style: TextStyle(
                    fontSize: 18,
                    fontWeight: FontWeight.w600,
                    color: Colors.deepPurple,
                  ),
                ),
                Icon(Icons.expand_more)
              ],
            ),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 20),
              child: TableCalendar(
                locale: 'ko_KR',
                firstDay: DateTime.utc(2020, 10, 10),
                lastDay: DateTime.utc(2025, 10, 10),
                focusedDay: focusedDay,
                daysOfWeekHeight: 30,
                // headerVisible: false,
                onDaySelected: (DateTime selectedDay, DateTime focusedDay) {
                  setState(() {
                    this.selectedDay = selectedDay;
                    this.focusedDay = focusedDay;
                  });
                },
                onPageChanged: (focusedDay) {
                  focusedDay = focusedDay;
                },
                selectedDayPredicate: (DateTime day) {
                  return isSameDay(selectedDay, day);
                },
                headerStyle: HeaderStyle(
                    decoration: const BoxDecoration(
                      color: Color.fromRGBO(100, 92, 170, 1),
                    ),
                    leftChevronIcon: const Icon(
                      Icons.chevron_left,
                      color: Colors.white,
                    ),
                    rightChevronIcon: const Icon(
                      Icons.chevron_right,
                      color: Colors.white,
                    ),
                    titleCentered: true,
                    titleTextFormatter: (date, locale) =>
                        DateFormat.yMMMMd(locale).format(date),
                    formatButtonVisible: false,
                    titleTextStyle: const TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.w400,
                      color: Colors.white,
                    ),
                    headerPadding: const EdgeInsets.symmetric(
                      vertical: 0,
                    )),
                calendarStyle: const CalendarStyle(
                  tableBorder: TableBorder(
                    // top: BorderSide(
                    //   color: Colors.purple,
                    // ),
                    // bottom: BorderSide(
                    //   color: Colors.purple,
                    // ),
                    // left: BorderSide(
                    //   color: Colors.purple,
                    // ),
                    // right: BorderSide(
                    //   color: Colors.purple,
                    // ),
                    horizontalInside: BorderSide(
                      color: Colors.lightBlue,
                    ),
                    verticalInside: BorderSide(
                      color: Colors.lightBlue,
                    ),
                  ),
                ),
                eventLoader: getEventsForDay,
                // calendarBuilders: CalendarBuilders(
                //   dowBuilder: (context, day) {
                //     return Center(child: Text(days[day.weekday]));
                //   },
                //   markerBuilder: (context, date, events) {
                //     DateTime toDate = DateTime(date.year, date.month, date.day);
                //     if (isSameDay(toDate, _events[toDate])) {
                //       return Container(
                //         width: MediaQuery.of(context).size.width * 0.11,
                //         decoration: const BoxDecoration(
                //           color: Colors.lightBlue,
                //           shape: BoxShape.circle,
                //         ),
                //       );
                //     }
                //     return null;
                //   },
                // ),
              ),
            ),),
          ],
        ),
      ),
    );
  }
}
