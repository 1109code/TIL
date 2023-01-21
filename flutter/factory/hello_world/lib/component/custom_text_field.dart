import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:hello_world/const/colors.dart';

class CustomTextField extends StatelessWidget {
  final String label;
  // true - 시간, false - 내용
  final bool isTime;
  final FormFieldSetter<String> onSaved;

  const CustomTextField({
    super.key,
    required this.label,
    required this.isTime,
    required this.onSaved,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          label,
          style: const TextStyle(
            color: PRIMARY_COLOR,
            fontWeight: FontWeight.w600,
          ),
        ),
        if (isTime) renderTextField(),
        if (!isTime) Expanded(child: renderTextField()),
      ],
    );
  }

  Widget renderTextField() {
    return TextFormField(
      // 폼에서 save함수 불렀을 때 실행
      onSaved: onSaved,
      // null이 return 되면 에러가 없다.
      // 에러가 있으면 에러를 String 갑승로 리턴해준다.
      validator: (String? val) {
        if (val == null || val.isEmpty) {
          return '값을 입력해주세요';
        }
        if (isTime) {
          // int.parse : string으로 변환
          int time = int.parse(val);

          if (time < 0) {
            return '0 이상의 숫자를 입력해주세요.';
          }

          if (time > 24) {
            return '24 이하의 숫자를 입력해주세요.';
          }
        } else {
          if (val.length > 500) {
            return '500자 이하의 글자를 입력해주세요.';
          }
        }
        return null;
      },
      // 커서 색
      cursorColor: Colors.grey,
      // 줄 바꿈
      maxLines: isTime ? 1 : null,
      expands: !isTime,
      // maxLength: 500,
      // 키보드 변경
      keyboardType: isTime ? TextInputType.number : TextInputType.multiline,
      inputFormatters: isTime
          ? [
              // 숫자만 쓸 수 있게
              FilteringTextInputFormatter.digitsOnly,
            ]
          : [],
      decoration: InputDecoration(
        // 아래 경계선 제거
        border: InputBorder.none,
        // 이걸 해야 색을 넣을 수 있음
        filled: true,
        fillColor: Colors.grey[300],
      ),
    );
  }
}
