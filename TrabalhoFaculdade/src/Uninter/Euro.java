package Uninter;

public class Euro extends Moeda {

	public Euro(double valor) {
		this.valor = valor;
	}

	@Override
	public void info() {
		System.out.println("Euro - " + valor); /* informa moeda e valor inseridos pelo usuário */
		
	}

	@Override
	public double converter() {
		return this.valor * 5.39; //cotação referente ao dia 27/03
		
	}	
	
	
	@Override 
	public boolean equals(Object objeto) {   /* usado para auxiliar que o objeto no caso a moeda que foi inserida, a ser capturada pelo método remover*/
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		
		Euro objetoEuro = (Euro) objeto;
		
		if(this.valor != objetoEuro.valor) {
			return false;
		}
		
		return true;
		
		}
	
	}
	

