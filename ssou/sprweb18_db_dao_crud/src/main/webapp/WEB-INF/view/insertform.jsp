<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="EUC-KR"%>
<%@ taglib prefix="sform" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
** �ڷ� �߰� **<br>
<sform:form commandName="command">
�� �� �� : <sform:input path="id"/><br>
��й�ȣ : <sform:input path="passwd"/><br>
ȸ �� �� : <sform:input path="name"/><br>
<input type="submit" value="�߰�">
</sform:form>
</body>
</html>