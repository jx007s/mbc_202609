<%@page import="java.util.HashMap"%>
<%@page import="model_p.StudDTO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String stId = request.getParameter("stId");
	System.out.println(stId);
    //StudDTO dto = new StudDTO("정좌성",36,false);
    
	//{"pname":"정우성","age":53,"marriage":"true"}
	
	HashMap<String, StudDTO> studs = new HashMap();
	studs.put("aaa", new StudDTO("정우성",46,true));
	studs.put("bbb", new StudDTO("정좌성",36,false));
	studs.put("ccc", new StudDTO("정남성",27,true));
	studs.put("ddd", new StudDTO("정중성",19,false));
	studs.put("eee", new StudDTO("북두신성",24,false));
%>
<%=studs.get(stId)%>