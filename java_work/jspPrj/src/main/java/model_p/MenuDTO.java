package model_p;

public class MenuDTO {

	String kind, pname;
	int price;
	boolean delivery;
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
