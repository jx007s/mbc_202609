package basic_p;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class MemberMain {

	public static void main(String[] args) throws Exception {

		//1. JDBC 드라이버 로딩    
		Class.forName("com.mysql.cj.jdbc.Driver");
		

		String url = "jdbc:mysql://localhost:3306/mbc_db?characterEncoding=utf-8";
		//            jdbc:mysql://[ip]:[port]/[db이름]?characterEncoding=utf-8
		String user = "mbc_user";
		String pw = "1234";
		
		//2. DB 연결 객체 생성
		Connection con = DriverManager.getConnection(url, user, pw);
		
		
		//3. 쿼리문을 실행하기위한 객체생성
		Statement stmt = con.createStatement();
		
		String sql = "SELECT * FROM member";

		//4. 쿼리 실행
		ResultSet rs = stmt.executeQuery(sql);
		
		//5. 쿼리 실행 결과 사용
		while(rs.next()) {
			String ttt = rs.getString("pid")+"\t";
			ttt += rs.getString("pname")+"\t";
			ttt += rs.getInt("age")+"\t";
			ttt += rs.getInt("marriage")==0 ? "미혼" : "기혼";
			
			System.out.println(ttt);
		}
		
		
		//6. 쿼리문 실행객체 종료
		rs.close();
		stmt.close();
		
		
		//7. DB 연결 객체 닫기
		con.close();

	}

}

/*
DB 계정명 : test_user
DB명 : test_db
table명 : menu
id, 종류, 이름, 가격, 배달

java : MenuMain 
 * */

