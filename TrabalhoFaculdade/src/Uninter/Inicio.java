package Uninter;

import java.util.Scanner;

public class Inicio {
	
	private Scanner scan;
	private Cofrinho cofrinho;
	
	
	
	public Inicio() {
		scan = new Scanner(System.in);
		cofrinho = new Cofrinho();
	}
	
	public void exibirMenuPrincipal() {
		System.out.println("--------- Cofrinho --------- by Ronny Wallace ");
		System.out.println();
		System.out.println("1-Adicionar moeda: ");
		System.out.println("2-Remover moeda: ");
		System.out.println("3-Listar moedas: ");
		System.out.println("4-Calcular valor total convertido para real: ");
		System.out.println("0-Encerrar: ");
		
		String opcao = scan.next();
		
		System.out.println(opcao);
	
		switch (opcao) {
			case "0":
				System.out.println("Programa finalizado! Obrigado por usar este programa ; )!! ");
				break;
				
			case "1":
				exibirMenuAdicionarMoedas(); /* método criado para deixar o código mais clean e mais funcional */
				System.out.println();
				exibirMenuPrincipal();
				break;
				
			case "2":
			    exibirMenuRemoverMoedas(); /* semelhante ao método do 'case 1', invoca o método exibirMenuRemoverMoedas */
			    System.out.println();
			    exibirMenuPrincipal();
			    break;
				
			case "3":
				cofrinho.listagemMoedas(); /*invoca o método contador de moedas da classe cofrinho*/
				System.out.println();
				exibirMenuPrincipal();
				break; 
				
			case "4":
				double valorConvertido = cofrinho.totalConvertido(); /* invoca o métodod de conversão de moedas da classe cofrinho */
				String valorConvertidoTexto = String.format("%,2f", valorConvertido); /* uma formatação da saída de dados para o usuário */
				valorConvertidoTexto = valorConvertidoTexto.replace(".",",");
				System.out.println("O valor total convertido para real: " + valorConvertidoTexto);
				System.out.println();
				exibirMenuPrincipal();
				break;
				
				
				
			default: 
				System.out.println("Opção inválida! ");
				exibirMenuPrincipal();
			break;
		}
		
	}
	
	private void exibirMenuAdicionarMoedas() { /*método para exibir submenu de adicionar moedas*/ 
		System.out.println("Escolha a Moeda: ");
		System.out.println("1 - Real: ");
		System.out.println("2 - Dollar: ");
		System.out.println("3 - Euro: ");
		
		int tipoMoeda = scan.nextInt();
		
		System.out.println("Digite o valor da moeda: ");
		
		String valorStringMoeda = scan.next();
		
		valorStringMoeda = valorStringMoeda.replace(",",".");
		double valorMoeda = Double.parseDouble(valorStringMoeda); /* estas duas linhas servem para evitar erro de ponto e vírgula na hora da inserção de dados*/
		
		Moeda moeda = null; 
		
		if (tipoMoeda == 1) {
			moeda = new Real(valorMoeda);
		} else if (tipoMoeda == 2) {
			moeda = new Dollar(valorMoeda);
		} else if (tipoMoeda == 3) {
			moeda = new Euro(valorMoeda);
		} else {
			System.out.println("Não existe essa moeda! ");
			exibirMenuPrincipal();
		}
		
		cofrinho.adicionar(moeda);
	    System.out.println("Moeda adicionada com sucesso! ");	
	
	}
  private void exibirMenuRemoverMoedas() { /* método para simplificar a opção remover moedas */
	  System.out.println("Escolha a Moeda: ");
		System.out.println("1 - Real: ");
		System.out.println("2 - Dollar: ");
		System.out.println("3 - Euro: ");
		
		int tipoMoeda = scan.nextInt();
		
		System.out.println("Digite o valor da moeda: ");
		
		String valorStringMoeda = scan.next();
		
		valorStringMoeda = valorStringMoeda.replace(",",".");
		double valorMoeda = Double.parseDouble(valorStringMoeda);
		
		Moeda moeda = null; 
		
		if (tipoMoeda == 1) {
			moeda = new Real(valorMoeda);
		} else if (tipoMoeda == 2) {
			moeda = new Dollar(valorMoeda);
		} else if (tipoMoeda == 3) {
			moeda = new Euro(valorMoeda);
		} else {
			System.out.println("Não existe essa moeda! ");
			exibirMenuPrincipal();
		}
		
		cofrinho.remover(moeda);
	    
  }
  	
}

