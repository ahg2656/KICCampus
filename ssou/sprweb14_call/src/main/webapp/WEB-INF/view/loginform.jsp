<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="EUC-KR"%>
<%@taglib prefix="sform" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>�ڷ� �Է� - Spring tag </h2>
<sform:form commandName="command">
[i d] : <sform:input path="userid"/><br>
[pwd] : <sform:input path="passwd"/><br>
<input type="submit" value="����">
</sform:form>
<hr>
<form id="command" action="login" method="post">
[i d] : <input type="text" name="userid"><br>
[pwd] : <input type="text" name="passwd"><br>
<input type="submit" value="����">
</form>
</body>
</html>