<%@page import="java.util.HashMap"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	//비동기로 접근하는 모든 출처에서 허용
	// 기본 형태는 다른 서버에서 접근하는 것을 보안상의 이유로 차단
	response.setHeader("Access-Control-Allow-Origin", "*");
	//~~~~/01_st.jsp?pid=aaa&age=32
	/*
	01_st.jsp : 페이지
	pid=aaa&age=32 : parameter (쿼리) - URL 로 데이터 요청시 필요한 변수를 전달
	
	내장객체 : request 를 이용하여 parameter 확인
	*/
	
	String pid = request.getParameter("pid");
	System.out.println("pid : "+pid);
	String age = request.getParameter("age");
	System.out.println("age : "+age);
	
	HashMap<String, String> studs = new HashMap();
	
	studs.put("aaa","장동건");
	studs.put("bbb","장서건");
	studs.put("ccc","장남건");
	studs.put("ddd","장중건");
	studs.put("eee","북두신건");
	
%>
<%=studs.get(pid)%>