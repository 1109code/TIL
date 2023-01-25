import 'package:flutter/material.dart';
import 'package:hello_world/const/colors.dart';

class ScheduleCard extends StatelessWidget {
  final int startTime;
  final int endTime;
  final String content;
  final Color color;

  const ScheduleCard({
    super.key,
    required this.startTime,
    required this.endTime,
    required this.content,
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        border: Border.all(
          width: 1,
          color: PRIMARY_COLOR,
        ),
        borderRadius: BorderRadius.circular(
          8,
        ),
      ),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        // 가장 높은 애 기준으로 칸 배정
        child: IntrinsicHeight(
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              _Time(
                startTime: startTime,
                endTime: endTime,
              ),
              const SizedBox(
                width: 16,
              ),
              _Content(
                content: content,
              ),
              const SizedBox(
                width: 16,
              ),
              _Category(
                color: color,
              )
            ],
          ),
        ),
      ),
    );
  }
}

class _Time extends StatelessWidget {
  final int startTime;
  final int endTime;

  const _Time({
    required this.startTime,
    required this.endTime,
  });

  @override
  Widget build(BuildContext context) {
    const textStyle = TextStyle(
      fontWeight: FontWeight.w600,
      color: PRIMARY_COLOR,
      fontSize: 16,
    );

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // 최소 두개 글자, 남는 공간을 0으로 채우기
        Text(
          '${startTime.toString().padLeft(2, '0')}:00',
          style: textStyle,
        ),
        Text(
          '${endTime.toString().padLeft(2, '0')}:00',
          style: textStyle.copyWith(
            fontSize: 10,
          ),
        ),
      ],
    );
  }
}

class _Content extends StatelessWidget {
  final String content;

  const _Content({
    required this.content,
  });

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Text(
        content,
      ),
    );
  }
}

class _Category extends StatelessWidget {
  final Color color;

  const _Category({
    required this.color,
  });

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        color: color,
        shape: BoxShape.circle,
      ),
      width: 16,
      height: 16,
    );
  }
}
