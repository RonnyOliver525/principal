package Uninter;

public abstract class Moeda { /* classe mãe de todas as moedas */
		
	double valor;
	
	
	public abstract void info(); 
	
	public abstract double converter(); /* Método genérico que dá origem à conversão das moedas para real. */
	
		
	
	
}
