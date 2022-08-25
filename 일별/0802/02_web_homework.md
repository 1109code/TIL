# 1. Semantic Tag

> header / section / footer

# 2. input Tag

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <form action="">
    <div class="input-group">
      <label for="username">USERNAME : 
        <input type="text" name="username" id="username" autofocus>
      </label>
    </div>

    <div class="input-group">
      <label for="password">PWD : 
        <input type="text" name="password" id="password" autofocus>
        <input type="submit" value="로그인">
      </label>
    </div>
    
  </form>
</body>
</html>
```

# 3. 크기 단위

> rem

# 4. 선택자

> 자손 결합자의 경우 div의 모든 하위 항목의 p에 대해 상속을 하는 반면
>
> 자식 셜합자의 경우 div의 바로 아래 항목의 p에 대해서만 상속을 진행한다.