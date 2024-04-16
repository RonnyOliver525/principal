package Uninter;

import java.util.ArrayList;

public class Cofrinho {
	
	private ArrayList<Moeda> listaMoedas;
	
	public Cofrinho() {
		this.listaMoedas = new ArrayList<>();
	}
	
	public void adicionar (Moeda moeda) {
		this.listaMoedas.add(moeda);
		
	}
	
	public void remover (Moeda moeda) {
		this.listaMoedas.remove(moeda);
	}
	
	
	public void listagemMoedas () {
		if (this.listaMoedas.isEmpty()) {
			System.out.println("Não existe moeda no cofre!"); /* retorno do método caso não exista moeda alguma inserida */
			return;
		}
		
		for (Moeda moeda : this.listaMoedas) {
			moeda.info();
		}
	}
	
	public double totalConvertido () {  /* precisei usar IF para caso ele esteja vazio ele não retorne nada e o FOR para quando o total sofrer acréscimo de uma nova moeda   */ 
		if (this.listaMoedas.isEmpty()) {
			return 0;	
		}
	
		double valorCumulativo = 0;
		
		for(Moeda moeda : this.listaMoedas ) {
			valorCumulativo = valorCumulativo + moeda.converter();
		}
		
		return valorCumulativo;
		
	}
	
	
	
}
	
	

