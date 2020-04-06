<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core"  prefix="c" %>
<%@ taglib uri="/WEB-INF/tld/jaketag2.tld" prefix="bean" %>
<%@ page import="java.util.Date" %>
<%@ page import="com.jake.tag2.UserInfo" %>
<%@ page import="java.text.SimpleDateFormat" %>
<% UserInfo userInfo = new UserInfo();
SimpleDateFormat formatter= new SimpleDateFormat("yyyy-MM-dd 'at' HH:mm:ss z");
Date date = new Date();
userInfo.setBirthday(formatter.format(date));
request.setAttribute("userInfo",userInfo);
%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>新規 JSP tag テスト</title>
</head>
<body>
<p>日付：</p>
<%= userInfo.getBirthday() %>
<p>c:outタグより取得</p>
<c:out value="${userInfo.birthday}"/>
<!--<c:out value="<b>Hello</b>" escapeXml="false"/> -->
<p>自定義タグで変換</p>
 <bean:write name="userInfo1"  property="birthday"   format="yyyy/MM/dd"/>
 <bean:write name="userInfo2" 
 property="birthday"  
 format="yyyy/MM/dd"/>
</body>
</html>