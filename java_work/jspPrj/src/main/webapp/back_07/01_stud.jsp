<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	//모든 출처에서의 접근 허용
	response.setHeader("Access-Control-Allow-Origin", "*");

	//스크립틀릿 : _jspService() 메소드구간 - 자동호출
	String pname = "장동건";
	int age = 56;
	boolean marriage = true;
%>
<!-- 표현식 : html 문서에 java 코드 출력 -->
<%=pname%>