package Uninter;

public class Real extends Moeda {

	
	public Real(double valor) {
		this.valor = valor;
	}
	

	@Override
	public void info() {
		System.out.println("Real - " + valor); /* informa moeda e valor inseridos pelo usuário */
		
	}

	@Override
	public double converter() { /*como a moeda real não precisa de conversão, ela retorna ela mesmo*/
		return this.valor;
		
		
	}
	
	@Override 
	public boolean equals(Object objeto) { /* usado para auxiliar que o objeto no caso a moeda que foi inserida, a ser capturada pelo método remover*/
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		
		Real objetoReal = (Real) objeto;
		
		if(this.valor != objetoReal.valor) {
			return false;
		}
		
		return true;
		
	}
	
	
	

}
