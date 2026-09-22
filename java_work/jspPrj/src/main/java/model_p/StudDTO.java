package model_p;

public class StudDTO {

	String pid, pname;
	int age;
	boolean marriage;
	
	public StudDTO(String pname, int age, boolean marriage) {
		super();
		this.pname = pname;
		this.age = age;
		this.marriage = marriage;
	}
	
	public StudDTO() {
		// TODO Auto-generated constructor stub
	}
	
	public String getPid() {
		return pid;
	}

	public void setPid(String pid) {
		this.pid = pid;
	}

	public String getPname() {
		return pname;
	}

	public void setPname(String pname) {
		this.pname = pname;
	}

	public int getAge() {
		return age;
	}

	public void setAge(int age) {
		this.age = age;
	}

	public boolean isMarriage() {
		return marriage;
	}

	public void setMarriage(boolean marriage) {
		this.marriage = marriage;
	}

	@Override
	public String toString() {
		return "{\"pname\":\"" + pname + 
				"\",\"pid\":\"" + pid + 
				"\",\"age\":" + age + 
				",\"marriage\":" + marriage + "}";
	}
	
	
	
}
