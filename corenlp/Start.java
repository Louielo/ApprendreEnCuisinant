import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Properties;

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
		// TODO Auto-generated method stub
		List<String> noms = new ArrayList<>();
    	FichierW fnoms = new FichierW("noms.txt");
    	FichierW fverbes = new FichierW("verbes.txt");
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
    	 System.out.println(parseTree);		//phrase entière
    	 
    	 // traitement des tokens
    	 
	    	 for (CoreLabel token: sentence.get(TokensAnnotation.class)) {
	    	 String pos = token.get(PartOfSpeechAnnotation.class);
	    	 String newtoken = token.toString();
		    	 
	    		 for (int i = 0; i < newtoken.length(); i++) {
	 	            if (newtoken.charAt(i) == '-') {
	 	            	newtoken = newtoken.substring(0, i);
	 	            }
	 	        }
 		 
	    	 
	    	 
		    	 if (pos.equals("N")||pos.equals("NC")) {	// si le pos est N alors on enregistre le token dans le fichier nom
		    		 

		    		 System.out.println(newtoken+" : "+pos);
		    		 fnoms.ecrire(newtoken.toLowerCase());

		    	 } else if (pos.equals("V")||pos.equals("VINF")) {	// si le pos est N alors on enregistre le token dans le fichier verbe
		    		 System.out.println(newtoken+" : "+pos);
		    		 fverbes.ecrire(newtoken.toLowerCase());
		    	 }else {
		    		 // System.out.println(pos);
		    	 }
	    	 }
	    	 	// ne pas inclure mot d'une ou deux lettres
    	}

    	//Ã©criture du fichier
    	fnoms.fermer();
    	fverbes.fermer();
    	
    }

}
