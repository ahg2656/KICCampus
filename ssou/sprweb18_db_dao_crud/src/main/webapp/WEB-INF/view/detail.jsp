<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>Insert title here</title>
</head>
<body>
* ȸ�� �󼼺��� *<br>
<table>
	<tr><td>�� �� �� : ${member.id}</td></tr>
	<tr><td>��й�ȣ : ${member.passwd}</td></tr>
	<tr><td>ȸ �� �� : ${member.name}</td></tr>
	<tr><td>�� �� �� : ${member.reg_date}</td></tr>
	<tr>
		<td colspan="2">
			<a href="list">���</a>
			<a href="update?id=${member.id}">����</a>
			<a href="delete?id=${member.id}">����</a>
		</td>
	</tr>
</table>
</body>
</html>