import 'package:dogdoc_calendar/screen/home_screen.dart';
import 'package:flutter/material.dart';
import 'package:intl/date_symbol_data_local.dart';

void main() async {
  // 날짜 한글 포매팅
  await initializeDateFormatting();

  runApp(
    const MaterialApp(
      home: HomeScreen(),
    ),
  );
}
