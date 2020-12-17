

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class FichierW {
	private PrintWriter pw;
	
	// constructeur
	public FichierW(String nom) {  //il faut avoir les droits en création pour écrire un fichier du coup on utilise un try catch, pouvoir gerer ce qu'il va se passer en cas d'erreur
		try {
			pw = new PrintWriter(
					new BufferedWriter(
							new FileWriter(nom)));
			//le fichier est pret pour l'écriture
		} catch(IOException e) {
			System.out.println("Impossible d'ouvrir le fichier "+nom);
		}
	
	}
	
	public void fermer() {
		pw.close();
	}
	
	public boolean ecrire(String ligne) {
		try {
			pw.println(ligne);
			return true;
		} catch (Exception e) {
			return false;
		}
		
	}
}
