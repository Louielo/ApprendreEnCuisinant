import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Properties;
import java.util.Random;

import org.apache.log4j.BasicConfigurator;

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

		BasicConfigurator.configure();
    	// création d'un objet Properties
    	Properties props = new Properties();
    	props.setProperty("ner.useSUTime", "false");
    	// définition du pipeline
    	props.setProperty("annotators", "tokenize, ssplit, parse, lemma, ner");
    	// paramétrage pour le français
    	props.setProperty("props", "StanfordCoreNLP-french.properties");
    	props.setProperty("tokenize.language","French");
    	props.setProperty("parse.model","edu/stanford/nlp/models/lexparser/frenchFactored.ser.gz");
    	props.setProperty("pos.model","edu/stanford/nlp/models/postagger/french/french.tagger");
    	props.setProperty("tokenize.verbose","false"); // True = affiche les tokens
    	// création du pipeline
    	StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

    	// Lance le pipeline sur une chaine de caractères qu'on récup dans le fichier recette
    	String text = new String(Files.readAllBytes(Paths.get("recette.txt")));

    	// créer une annotation vide avec le texte
    	Annotation document = new Annotation(text);
    	// lance l'annotation sur le texte
    	pipeline.annotate(document);

    	// Obtenir la liste des phrases
    	List<CoreMap> sentences = document.get(CoreAnnotations.SentencesAnnotation.class);
    	for (CoreMap sentence : sentences) {
    	 // obtenir l'arbre d'analyse de chaque phrase
    	edu.stanford.nlp.trees.Tree parseTree = sentence.get(TreeAnnotation.class);

    	 // Ecrire l'arbre
    	 //System.out.println(parseTree);		//phrase entière
    	 
    	 // traitement des tokens
    	 
	    	 for (CoreLabel token: sentence.get(TokensAnnotation.class)) {
	    		 String pos = token.get(PartOfSpeechAnnotation.class);
	    		 String newtoken = token.toString();
		    	 
	    		 for (int i = 0; i < newtoken.length(); i++) {		// on supprime à partir des tirets pour ne pas avoir "chocolat -3" mais "chocolat"
	 	            if (newtoken.charAt(i) == '-') {
	 	            	newtoken = newtoken.substring(0, i);
	 	            }
	 	        }
	    	 
		    	 if (pos.equals("N")||pos.equals("NC")&&newtoken.length()>1) {	// si le pos est N alors on enregistre le token dans le fichier nom
		    		 // System.out.println(newtoken+" : "+pos);
		    		 // fnoms.ecrire(newtoken.toLowerCase());
		    	     // ici on append newtoken.toLowerCase() à un tableau
		    		 listnom.add(newtoken.toLowerCase());

		    	 } else if (pos.equals("V")||pos.equals("VINF")&&newtoken.length()>1) {	// si le pos est N alors on enregistre le token dans le fichier verbe
		    		 // System.out.println(newtoken+" : "+pos);
		    		 //fverbes.ecrire(newtoken.toLowerCase());
		    		 listverb.add(newtoken.toLowerCase());
		    	
		    		 
		    	 } else if (pos.equals("ADJ")&&newtoken.length()>1) {	// si le pos est N alors on enregistre le token dans le fichier verbe
		    		 // System.out.println(newtoken+" : "+pos);
		    		 //fverbes.ecrire(newtoken.toLowerCase());
		    		 listadj.add(newtoken.toLowerCase());
		    	
		    	 } else if (pos.equals("ADV")&&newtoken.length()>1) {	// si le pos est N alors on enregistre le token dans le fichier verbe
		    		 // System.out.println(newtoken+" : "+pos);
		    		 //fverbes.ecrire(newtoken.toLowerCase());
		    		 listadv.add(newtoken.toLowerCase());
		    		 
		    	 }else {
		    		 // System.out.println(pos);
		    	 }
	    	 }
	    	 	// ne pas inclure mot d'une ou deux lettres
    	}
    	
	    // On génère un chiffre random pour choisir au hasard un des noms
	    int rand_n = rand.nextInt(listnom.size());// en mettant length du tab nom
	    fnoms.ecrire(listnom.get(rand_n));
	    // On génère un chiffre random pour choisir au hasard un des verbes
	    int rand_v = rand.nextInt(listverb.size());
	    fverbes.ecrire(listverb.get(rand_v));
	    int rand_adj = rand.nextInt(listadj.size());
	    fadjectifs.ecrire(listadj.get(rand_adj));
	    int rand_adv = rand.nextInt(listadv.size());
	    fadverbes.ecrire(listadv.get(rand_adv));
    	//Ã©criture du fichier
	    fadjectifs.fermer();
	    fadverbes.fermer();
    	fnoms.fermer();
    	fverbes.fermer();
    	
    }

}
