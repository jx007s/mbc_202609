<%@page import="java.util.ArrayList"%>
<%@page import="model_p.MenuDTO"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%

	int menuNo = 3;
	System.out.println(request.getParameter("menuNo"));
	if(request.getParameter("menuNo")!=null){
				//문자열 -> int 로 변환
		menuNo = Integer.parseInt(request.getParameter("menuNo"));
	}
	
	
	ArrayList<MenuDTO> menus = new ArrayList();
	menus.add(new MenuDTO("한식","비빔밥",9000,true));
	menus.add(new MenuDTO("중식","자장면",8500,true));
	menus.add(new MenuDTO("일식","초밥",13000,false));
	menus.add(new MenuDTO("한식","돼지국밥",10000,false));
	menus.add(new MenuDTO("분식","떡볶이",5000,true));
	
	MenuDTO now = menus.get(menuNo);
%>

<%=now %>
