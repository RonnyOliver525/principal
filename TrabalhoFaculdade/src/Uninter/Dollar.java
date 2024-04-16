package Uninter;

public class Dollar extends Moeda {

	public Dollar(double valor) {
		this.valor = valor;
	}

	@Override
	public void info() {
		System.out.println("Dollar - " + valor); /* informa moeda e valor inseridos pelo usuário */
		
	}

	@Override
	 public double converter() {
		return this.valor * 4.98;    //cotação referente ao dia 27/03//
	
	
	}
	
	@Override 
	public boolean equals(Object objeto) {       /* usado para auxiliar que o objeto no caso a moeda que foi inserida, a ser capturada pelo método remover  */
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		
		Dollar objetoDollar = (Dollar) objeto;
		
		if(this.valor != objetoDollar.valor) {
			return false;
		}
		
		return true;
	
	}

}
