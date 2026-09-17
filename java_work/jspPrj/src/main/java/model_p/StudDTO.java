package model_p;

public class StudDTO {

	String pname;
	int age;
	boolean marriage;
	
	public StudDTO(String pname, int age, boolean marriage) {
		super();
		this.pname = pname;
		this.age = age;
		this.marriage = marriage;
	}

	@Override
	public String toString() {
		return "{\"pname\":\"" + pname + 
				"\",\"age\":\"" + age + 
				"\",\"marriage\":\"" + marriage + "\"}";
	}
	
	
	
}
