package model_p;

public class MenuDTO {

	String kind, pname;
	int price;
	boolean delivery;
	
	
	//켭슐화
	public String getPname() {
		return pname;
	}
	public MenuDTO(String kind, String pname, int price, boolean delivery) {
		
		this.kind = kind;
		this.pname = pname;
		this.price = price;
		this.delivery = delivery;
	}
	@Override
	public String toString() {
		return	"{\"kind\":\"" +  kind + 
				"\",\"pname\":\""  + pname + 
				"\",\"price\":\"" +  price + 
				"\",\"delivery\":\"" +  delivery  + "\"}";
	}
	
	
}
