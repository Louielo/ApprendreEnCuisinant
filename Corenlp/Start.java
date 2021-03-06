package Corenlpfinal;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;
import java.util.Random;

//import org.apache.log4j.BasicConfigurator;	// Parfois utile pour r�gler certains bugs

import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.CoreAnnotations.PartOfSpeechAnnotation;
import edu.stanford.nlp.ling.CoreAnnotations.TokensAnnotation;
import edu.stanford.nlp.pipeline.Annotation;
import edu.stanford.nlp.pipeline.StanfordCoreNLP;
import edu.stanford.nlp.trees.TreeCoreAnnotations.TreeAnnotation;
import edu.stanford.nlp.util.CoreMap;


public class Start {

	
	public static void main(String[] args) throws IOException {
		FichierW fnoms = new FichierW("noms.txt");
    	FichierW fverbes = new FichierW("verbes.txt");
    	FichierW fadjectifs = new FichierW("adjectifs.txt");
    	FichierW fadverbes = new FichierW("adverbes.txt");
    	List<String> listnom = new ArrayList<String>();
    	List<String> listverb = new ArrayList<String>();
    	List<String> listadj = new ArrayList<String>();
    	List<String> listadv = new ArrayList<String>();
    	// instance pour avoir un int 
        Random rand = new Random(); 

		//BasicConfigurator.configure();      // Ligne de code qui parfois corrige certain bugs
    	// cr�ation d'un objet Properties
    	Properties props = new Properties();
    	props.setProperty("ner.useSUTime", "false");
    	// d�finition du pipeline
    	props.setProperty("annotators", "tokenize, ssplit, parse, lemma, ner");
    	// param�trage pour le fran�ais
    	props.setProperty("props", "StanfordCoreNLP-french.properties");
    	props.setProperty("tokenize.language","French");
    	props.setProperty("parse.model","edu/stanford/nlp/models/lexparser/frenchFactored.ser.gz");
    	props.setProperty("pos.model","edu/stanford/nlp/models/postagger/french/french.tagger");
    	props.setProperty("tokenize.verbose","false"); // True = affiche les tokens
    	// cr�ation du pipeline
    	StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

    	System.out.println("Lancement du pipeline sur la recette...");

    	// Lance le pipeline sur une chaine de caract�res qu'on r�cup dans le fichier recette
    	String text = new String(Files.readAllBytes(Paths.get("recette.txt")));
    	
    	
    	// cr�er une annotation vide avec le texte
    	Annotation document = new Annotation(text);
    	// lance l'annotation sur le texte
    	pipeline.annotate(document);

    	// Obtenir la liste des phrases
    	List<CoreMap> sentences = document.get(CoreAnnotations.SentencesAnnotation.class);
    	for (CoreMap sentence : sentences) {

    	 // Ecrire l'arbre
    	 //System.out.println(parseTree);		//phrase enti�re
    	 
    	 // traitement des tokens 
    	
	    	 for (CoreLabel token: sentence.get(TokensAnnotation.class)) {
	    		 String pos = token.get(PartOfSpeechAnnotation.class);
	    		 String newtoken = token.toString();
		    	 
	    		 for (int i = 0; i < newtoken.length(); i++) {		// on supprime � partir des tirets pour ne pas avoir "chocolat -3" mais "chocolat"
	 	            if (newtoken.charAt(i) == '-') {
	 	            	newtoken = newtoken.substring(0, i);
	 	            }
	 	        }
	    		 // On fait attention de ne pas r�cup�rer les mots d'une seule lettre car il ne serait pas tr�s int�ressant de les prononcer
		    	 if (pos.equals("N")||pos.equals("NC")&&newtoken.length()>1) {	// si le pos est N alors on enregistre le token dans le fichier nom
		    		 listnom.add(newtoken.toLowerCase());

		    	 } else if (pos.equals("V")||pos.equals("VINF")&&newtoken.length()>1) {	// si le pos est N alors on enregistre le token dans le fichier verbe
		    		 listverb.add(newtoken.toLowerCase());	    	
		    		 
		    	 } else if (pos.equals("ADJ")&&newtoken.length()>1) {	// si le pos est N alors on enregistre le token dans le fichier verbe
		    		 listadj.add(newtoken.toLowerCase());
		    	
		    	 } else if (pos.equals("ADV")&&newtoken.length()>1) {	// si le pos est N alors on enregistre le token dans le fichier verbe
		    		 listadv.add(newtoken.toLowerCase());
		    		 
		    	 }
	    	 }
    	}
    	
	    // On g�n�re un chiffre random pour choisir au hasard un des noms
	    int rand_n = rand.nextInt(listnom.size());// en mettant length du tab nom
	    fnoms.ecrire(listnom.get(rand_n));
	    // On g�n�re un chiffre random pour choisir au hasard un des verbes
	    int rand_v = rand.nextInt(listverb.size());
	    fverbes.ecrire(listverb.get(rand_v));
	    int rand_adj = rand.nextInt(listadj.size());
	    fadjectifs.ecrire(listadj.get(rand_adj));
	    int rand_adv = rand.nextInt(listadv.size());
	    fadverbes.ecrire(listadv.get(rand_adv));
    	//Ecriture du fichier
	    fadjectifs.fermer();
	    fadverbes.fermer();
    	fnoms.fermer();
    	fverbes.fermer();
    	System.out.println("Fichiers �crits");
    	
    }

}
