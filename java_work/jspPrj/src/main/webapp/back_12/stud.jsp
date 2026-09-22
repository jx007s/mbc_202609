<%@page import="model_p.StudDAO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String service = "list";
	if(request.getParameter("service")!=null){
		service = request.getParameter("service");
	}
	System.out.println(service);
	
	Object data = null;
	switch(service){
	case "list":
		data = new StudDAO().list();
		break;
	case "detail":
		data = new StudDAO().detail(request.getParameter("pid"));
		break;
	}
	
%>    
<%=data%>