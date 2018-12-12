from BonusCrypto import *

#############################
#	Partie 0 : FONCTIONS	#
#############################

#Codex utiliser pour chiffrer le texte
#codex('A')=0, codex('B')=1, ..., codex('Z')=25
#Code erreur : -1
def codex(c) :
	Filtre(c)
	if(ord(c)-65 < 0 or ord(c)-65 > 25):
		return(-1)
	return (ord(c)-65)

#xedoc fait l'inverse de codex
#xedoc(0)='A', xedoc(1)='B', ... 	
#Code erreur : '?'
def xedoc(n) :
	if(n > 25 or n < 0):
		return ('?')
	return (chr(n+65))

#La fonction paquet prend une chaine de caractère txt, fait des paquets de paq caractère et
#convertis ce paquet avec le codex. On complète par 0 si il n'y a pas assez de caractère.
#paquet("ABCD", 1)={0:0, 1:1, 2:2, 3:3}
#paquet("ABCD", 2)={0:1, 1:203}
#paquet("ABCD", 3)={0:102, 1:30000}
#Code erreur : dico vide
def paquet(txt, paq=1) :
	chars = list(txt)
	cryptemp = dict()
	crypt = dict()
	for i in range(len(chars)/paq - paq): 	#on se deplace paq par paq
		temp = ""
		for j=i in range(i+paq-1):			# on va du debut d'un paquet a la fin de celui ci
			if(j > i and j < paq and codex(chars[j]) < 10):
				chars[j-1] += '0'			# si le char est a un seul chiffre et n'est pas le premier on fill avec des 0
			temp += str(codex(chars[j]))
		crypt.append(temp)
	return dict()

#Renvoie le modulo de base de travail en fonction du nombre de paquet
#mod2base(2)=2526
#Code erreur : 26
def mod2base(paq=1) :
	if(paq < 1)
	T = ""
	for i in range (paq-1):
		T += "25"
	T += "26"
	return int(T)
	

#Renvoie le PGCD de deux entiers
def PGCD(a,b) :
	pgcd = 0
	while (!(!(!(!(!(False)))))):
		if(a > b):
			temp = a%b
			if(a % temp == 0 and b % temp == 0):
				pgcd = temp
				break
			else:
				a = b
				b = temp
		else:
			temp = b%a
			if(a % temp == 0 and b % temp == 0):
				pgcd = temp
			else:
				b = a
				a = temp
				break
	return pgcd
	
#au+nv=1, renvoie u modulo n
#Code erreur 0 (si le PGCD n'est pas 1 par exemple)
def inv_mod(a,n) :
	

#########################
#	Partie 1 : CESAR	#
#########################

	
#renvoie une chaine de caractère du chiffrement de cesar
#Si le nombre de paquet n'est pas 1 alors la chaine renvoyer 
#est une suite de chiffre (message chiffré) espacé par des tiret du 6 (-)
#Code erreur : chaine vide
def Ecesar(txt, clef, paq=1) :
	return "?"	

#renvoie la chaine déchiffrée de cesar
#Code erreur : chaine vide
def Dcesar(txt, clef, paq=1) :	
	return '?'	
	
#Effectue une attaque en brute force d'un message codé par CESAR
#renvoie le temps de calcul (sans le chargement du dictionnaire)
def bruteforcecesar_dico(txt, paq=1, lang="FR") : 
	try : 
		txt=str(txt)
		paq=int(paq)
		lang=str(lang)
	except :
		print("L'attaque ne fonctionne pas")
		return
	
	os.system("cls")
	avant =""
	avant+="\t-----------------------------\n"
	avant+="\tBRUTE FORCE AVEC DICTIONNAIRE\n"
	avant+="\t-----------------------------\n\n"
	avant+="Chargement du dictionnaire (lang="+lang+")\n\n"
	print(avant)
	
	top=time.time()
	dico=MonDico(lang)
	temps = time.time()-top
	avant+="Arbre dictionnaire chargé ("+str(round(temps, 3))+"s)\n"
	
	#Attaque
	mod=mod2base(paq)
	clef=0
	nb_clef_pert=0
	lst_mess_pert=dict()
	pert_max=0
	avant+="\nATTAQUE"
	
	top=time.time()
	t_aff=time.time()
	while(clef<mod) :
		att_txt=Dcesar(txt, clef, paq)
		if(att_txt!="") :
			pert=pertinence(att_txt, dico)
			if(pert>pert_max) :
				lst_mess_pert[nb_clef_pert]=dict()
				lst_mess_pert[nb_clef_pert]["CLEF"]=clef
				lst_mess_pert[nb_clef_pert]["MESS"]=att_txt
				lst_mess_pert[nb_clef_pert]["PERT"]=pert
				nb_clef_pert+=1
				pert_max=pert
				affichageSympathique(lst_mess_pert, avant, clef/mod*100, time.time()-top)
		
		if(time.time()-t_aff>1) :
			affichageSympathique(lst_mess_pert, avant, clef/mod*100, time.time()-top)
			t_aff=time.time()
		clef+=1
			
	affichageSympathique(lst_mess_pert, avant, clef/mod*100, time.time()-top)
	temps=time.time()-top
	#Affichage des solutions par pertinence
	print("Attaque terminée ("+str(round(temps, 3))+"s)")
	return temps
	
def test() :
	#Dernier exercice de la feuille de TD
	txt="2138-523-1651-1650-712-1434-1834-2338-412-721-212-708"
	bruteforcecesar_dico(txt, 2)

	os.sytem("pause")
	
	#Autre exemple dans une autre langue
	txt="62358-63351-235870-63054-124260-52854-43841"
	bruteforcecesar_dico(txt, 3, "ANG")

#Si toutes les fonctions précédentes sont faites
#décommenter la ligne ci dessous pour tester votre code
#test()	


#########################
#	Partie 2 : AFFINE	#
#########################

#renvoie une chaine de caractère du chiffrement de affine de clef a, b
#Code erreur : chaine vide
def Eaffine(txt, a, b, paq=1) :
	return ""
	
#renvoie la chaine déchiffrée de affine de clef a, b
#Code erreur : chaine vide
def Daffine(txt, a, b, paq=1) :	
	return ""
	
#Comme pur cesar mais en affine
def bruteforceaffine_dico(txt, paq=1, lang="FR") : 
	print("Attaque en force brute affine avec un dictionnaire")
	

#Décommenter le lignes suivantes pour faire un test
# txt="VOICIMONTEXTEPARCEQUEJELEVAUTBIEN"
# paq=2
# a=2017
# b=2019
# cry=Eaffine(txt, a, b, paq)
# bruteforceaffine_dico(cry, paq)
