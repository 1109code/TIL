import 'package:dogdoc_calendar/component/date_picker.dart';
import 'package:dogdoc_calendar/component/schedule_edit_bollean.dart';
import 'package:dogdoc_calendar/component/schedule_edit_walk.dart';
import 'package:flutter/material.dart';

class ScheduleScreen extends StatelessWidget {
  const ScheduleScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: const [
          DatePicker(),
          ScheduleEditWalk(),
          SizedBox(
            height: 30,
          ),
          ScheduleEditBollean(),
        ],
      ),
    );
  }
}
