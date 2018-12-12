import time
import os

"""
Cette bibliothèque donne la construction d'un arbre dictionnaire.
- Filtre : prend une chaine de caractère et fait le ménage dans les caractère spéciaux qu'elle peut contenir
- MonDico : prend en paramètre une langue et renvoie un arbre formé des lettres du dicto avec une case 'FINMOT' qui vaut true si c'est la fin du mot ou false sinon.

Si par exemple le dictionnaire contient cinq mots : a, aba, ac, acax et ajax alors l'abre que renvera la fonction 'MonDico', noté dans cet exemple X, sera

    b-------------a
   / FINMOT=False  FINMOT=True
  /
 /
a------------c---------------a---------------x
FINMOT=True  FINMOT=True     FINMOT=False    FINMOT=True
  \
   \
    j-------------a-------------x 
	FINMOT=False  FINMOT=False  FINMOT=True


	
Ou plus formellement
X['a'] est un tableau (=dict)
   - la case X['a']['FINMOT'] vaut True
   - la case X['a']['b'] est un tableau :
      - la case X['a']['b']['FINMOT'] vaut False
	  - la case X['a']['b']['a'] est un tableau :
         - X['a']['b']['a']['FINMOT'] vaut True
   - la case X['a']['c'] est un tableau :
      - la case X['a']['c']['FINMOT'] vaut True
      - la case X['a']['c']['a'] est un tableau :
	     - la case X['a']['c']['a']['FINMOT'] vaut False
	     - la case X['a']['c']['a']['x'] est un tableau :
	        - la case X['a']['c']['a']['x']['FINMOT'] vaut True
   - la case X['a']['j'] est un tableau :
      - la case X['a']['j']['FINMOT'] vaut False
      - la case X['a']['j']['a'] est un tableau :
	     - la case X['a']['j']['a']['FINMOT'] vaut False
	     - la case X['a']['j']['a']['x'] est un tableau :
	        - la case X['a']['j']['a']['x']['FINMOT'] vaut True	
"""

#Gestion des caractères accentué/spéciaux (FAIT)
def Filtre(txt) :
	res=""
	for c in txt.lower() :
		if(c=='à' or c=='â' or c=='ä' or c=='á' or c=='å') : res+='A'
		elif(c=='ç') : res+='C'
		elif(c=='é' or c=='è' or c=='ê' or c=='ë') : res+='E'
		elif(c=='ï' or c=='î' or c=='ì' or c=='í') : res+='I'
		elif(c=='ö' or c=='ò' or c=='ô' or c=='ø' or c=='ó') : res+='O'
		elif(c=='û' or c=='ü' or c=='ù' or c=='ú') : res+='U'
		elif(c=='æ') : res+='AE'
		elif(c=='œ') : res+='OE'
		elif(c=='ÿ') : res+='Y'
		elif(c=='ñ') : res+='N'
		elif(c=='ß') : res+='SS'
		elif(c=='0' or c=='1' or c=='2' or c=='3' or c=='4' or c=='5' or c=='6' or c=='7' or c=='8' or c=='9') : res+=''
		elif(c=='&') : res+=''
		elif(c=='-' or c==' ' or c=='/' or c=="'" or c=='.' or c=='?' or c=='!') : res+=''
		else : res+=c.upper()
	return res

#Création d'un arbre représentant le dictionnaire
#En paramètre la langue FR, ANG etc... (FAIT)
def MonDico(lang="FR") :
	try : lang=str(lang)
	except : lang="FR"
		
	Racine=dict()
	
	def constructBranche(mot):
		Arbre = Racine;
		for c in mot:
			#Si le cara c n'existe pas on le crée (permet en plus de gérer les répétitions éventuelles)
			if not (c in Arbre): 
				Arbre[c] = dict()
				Arbre[c]['FINMOT']=False
			#On avance dans l'arbre
			Arbre = Arbre[c]
		#Arrivé à la fin on marque que le mot est fini
		Arbre["FINMOT"] = True

	if(lang in {"ANG", "ALL", "ESP", "IT", "DAN", "NOR", "SWI", "NED"}) : dico = "Dictionnaires/Dictionnaire"+lang+".txt"
	else : dico = "Dictionnaires/DictionnaireFR.txt"
	
	with open(dico, "r") as f :
		for ligne in f.readlines() : 
			constructBranche(Filtre(ligne.strip()))
	return Racine
	

#La pertinence de d'un phrase est le nombre de mot 
#de la phrase présent dans l'arbre dictionnaire
#Calcul la pertinence d'une phrase avec l'arbre (FAIT)
def pertinence(phrase, arbre) :
	pert=0
	n=len(phrase)
	i=0
	while(i<n) :
		test=True
		j=i
		positionDico=arbre
		while(j<n and test) :
			cara=phrase[j]
			try : x=positionDico[cara]
			except : 
				test=False
				break
			if(x['FINMOT']) : pert+=1
			positionDico=x
			j+=1
		i+=1
	return pert
	
	
#Juste pour un affichage stylé, c'est gratuit (FAIT)
def affichageSympathique(lst_mess_pert, avant, avancement, temps) :
	os.system("cls")
	print(avant)

	x=" "
	i=0
	while(i<50) :
		x+='-'
		i+=1
	x+='\n|'
	i=0
	while(i<50) :
		if(i<avancement/2) : x+='+'
		else : x+=' '
		i+=1
	x+='| '+str(round(avancement, 2))+'%\n '
	i=0
	while(i<50) :
		x+='-'
		i+=1
	x+='\n'
	print(x)
	temps=int(temps)
	sec=temps%60
	min=(temps//60)%60
	heu=(temps//3600)
	print("Temps de calcul :", heu, "h", min, "min", sec, "s")
	
	print("Message par pertinence (pertinence|clef)")
	for i in lst_mess_pert : print("("+str(lst_mess_pert[i]["PERT"])+"|"+str(lst_mess_pert[i]["CLEF"])+") : "+lst_mess_pert[i]["MESS"][:50])
