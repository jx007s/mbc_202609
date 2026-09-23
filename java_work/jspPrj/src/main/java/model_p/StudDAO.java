package model_p;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.ArrayList;

public class StudDAO {
	
	String url = "jdbc:mysql://localhost:3306/mbc_db?characterEncoding=utf-8";
	String user = "mbc_user";
	String pw = "1234";
	
	Connection con = null;
	Statement stmt =  null;
	String sql =  null;
	ResultSet rs =  null;
		
	public StudDAO() {
		
		try {
			//1. JDBC 드라이버 로딩    
			Class.forName("com.mysql.cj.jdbc.Driver");
			
			//2. DB 연결 객체 생성
			con = DriverManager.getConnection(url, user, pw);
				
			//3. 쿼리문을 실행하기위한 객체생성
			stmt = con.createStatement();
			
			System.out.println("DAO 생성");
			
		} catch (Exception e) {
			System.out.println("DAO 생성 실패");
			close();
		}	
	}
	
	
	public ArrayList<StudDTO> list(){
		ArrayList<StudDTO> res = new ArrayList();
		
		try {
			sql = "SELECT * FROM member";

			//4. 쿼리 실행
			rs = stmt.executeQuery(sql);
			
			//5. 쿼리 실행 결과 사용
			while(rs.next()) {
				StudDTO dto = new StudDTO();
				dto.setPid(rs.getString("pid"));
				dto.setPname( rs.getString("pname"));
				dto.setAge(rs.getInt("age"));
				dto.setMarriage(rs.getInt("marriage")==1);
				res.add(dto);
			}
			
		} catch (Exception e) {
			
		}finally {
			close();
		}
		
		
		return res;
	}
	
	
	
	
	public StudDTO detail(String pid){
		StudDTO dto = null;
		
		try {
			sql = "SELECT * FROM member where pid = '"+pid+"'";

			//4. 쿼리 실행
			rs = stmt.executeQuery(sql);
			
			//5. 쿼리 실행 결과 사용
			if(rs.next()) {
				dto = new StudDTO();
				dto.setPid(rs.getString("pid"));
				dto.setPname( rs.getString("pname"));
				dto.setAge(rs.getInt("age"));
				dto.setMarriage(rs.getInt("marriage")==1);
				
			}
			
		} catch (Exception e) {
			
		}finally {
			close();
		}

		return dto;
	}
	
	
	public int insert(StudDTO dto){
		
		int res = 0;
		
		try {
			sql = "insert into member (pid, pname, age, marriage) values ("+
					" '"+dto.getPid()+"','"+dto.getPname()+
					"', "+dto.getAge()+", "+ ( dto.isMarriage() ? 1 : 0) +")";

			//4. 쿼리 실행
			res = stmt.executeUpdate(sql);
			
		} catch (Exception e) {
			e.printStackTrace(); //에러 확인
		}finally {
			close();
		}

		return res;
	}
	
	
	
	
	public void close() {
		
		if(rs!=null) 	try {	rs.close();		} catch (Exception e) { }
		if(stmt!=null) 	try {	stmt.close();	} catch (Exception e) { }
		if(con!=null) 	try {	con.close();		} catch (Exception e) { }
		
	}
		
}
