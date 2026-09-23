<%@page import="model_p.StudDTO"%>
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
	case "insert":
		StudDTO dto = new StudDTO();
		dto.setPid(request.getParameter("pid"));
		dto.setPname(request.getParameter("pname"));
		dto.setAge(Integer.parseInt(request.getParameter("age")));
		dto.setMarriage(request.getParameter("marriage").equals("1"));
		int cnt = new StudDAO().insert(dto);
		//System.out.println(dto);
		data = cnt;
		break;
	}
	
%>    
<%=data%>