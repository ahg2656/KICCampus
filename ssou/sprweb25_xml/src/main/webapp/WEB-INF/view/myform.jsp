<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="member" method="post">
이름 : <input type="text" name="name"><br>
나이 : <input type="text" name="age"><br>
<input type="submit" value="확인">
</form>
<br>
<form action="member_xml" method="post">
이름 : <input type="text" name="name" value="tom"><br>
나이 : <input type="text" name="age" value="24"><br>
<input type="submit" value="확인">
</form>
</body>
</html>