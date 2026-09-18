<%@page import="java.util.ArrayList"%>
<%@page import="model_p.MenuDTO"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	//기본데이터
	ArrayList<MenuDTO> menus = new ArrayList();
	menus.add(new MenuDTO("양식","스파게티",9000,true));
	menus.add(new MenuDTO("중식","자장면",8500,true));
	menus.add(new MenuDTO("일식","초밥",13000,false));
	menus.add(new MenuDTO("한식","돼지국밥",10000,false));
	menus.add(new MenuDTO("분식","떡볶이",5000,true));

	String service = "pre";	//지금 업무

	Object res = null;	//최종 리턴

	if(request.getParameter("service")!=null){
		
		service = request.getParameter("service");
	}
	
	if(service.equals("sch")){	//서비스가 메뉴검색이라면
		int menuNo = 3;
		//System.out.println(request.getParameter("menuNo"));
		if(request.getParameter("menuNo")!=null){
					//문자열 -> int 로 변환
			menuNo = Integer.parseInt(request.getParameter("menuNo"));
		}

		res = menus.get(menuNo);
	}
	
	else if(service.equals("pre")){	//서비스가 초기데이터가져오기라면
		String ttt = "[";
		for(MenuDTO mm : menus){
			//  각 원소를 "원소값",  형태로 변환하여 반환할 문자열에 결합
			ttt+="\""+mm.getPname()+"\",";
		}	
		//마지막 , 삭제
		ttt = ttt.substring(0,ttt.length()-1);
		
		ttt+="]";
		
		res = ttt;
		
		//System.out.println(res);
	}
	
%>

<%=res %>
