#############################
## execution d'un automate ##
#############################

# on fait une classe specifique pour l'execution de l'automate.
# ceci va nous permettre d'implémenter l'execution pas à pas de l'automate.

# la classe va prendre comme arguments :
#	- l'automate
#	- le mot avec lequel on va executer l'automate.

# la classe automate doit vérifier si le mot est reconnu par l'automate 
# (elle renvoie un booleen)
# et la cas échéant va renvoyer la suite des états à visiter pour que le mot soit accepté.

from automate import *

class execution :
	def __init__(self, auto_arg, mot_arg):
	
		# l'automate utilisé :
		self.auto = auto_arg
		
		# le mot passé en argument :
		self.mot = mot_arg
		
		# la suite des états a parcourir pour que le mot soit reconnu
		self.suite_etats = []
		
		# la n_iemme case ce cette liste renvoie 1 si la n_iemme transition
		# est une epsilon transition
		self.suite_epsilon = []
		
		# ce booléen nous dit si le mot est reconnu par l'automate.
		self.bool=False
	
# on arrive à la fin du mot :
	def fin_de_mot(self):
		return((len(self.suite_etats)-sum(self.suite_epsilon))==len(self.mot)+1)
		
# on est au début du mot :
	def debut_de_mot(self):
		return (self.suite_etats==[])
		
# changement du booléen :
	def changement_bool(self):
		self.bool=self.auto.est_final(self.suite_etats[len(self.suite_etats)-1])
			
# etat actuel de l'automate :
	def etat_actuel(self):
		return self.suite_etats[len(self.suite_etats)-1]
			
# actuelle lettre du mot :
	def lettre_actuelle(self):
		return self.mot[(len(self.suite_etats)-sum(self.suite_epsilon))-1]
			
#les états possibles à tester :
	def etats_possibles(self):
		if self.debut_de_mot():
			return self.auto.initial
		else :
			return self.auto.image(self.etat_actuel(),self.lettre_actuelle()) 
			
# on peut tenter un déplacement par epsilon-transition :
	def tentative_epsilon(self) :
		return ((not(self.bool)) and not(len(self.suite_etats)==0) and((len(self.suite_epsilon)==0) or (self.suite_epsilon[len(self.suite_epsilon)-1]==0)))
			
# la fonction d'execution (grosse et récursive):
	def execute(self):

		# cas d'arrêt : on est à la fin du mot 	
		if self.fin_de_mot():
			self.changement_bool()
		
		# sinon, on progresse dans le mot en testant 
		#les différents états possibles:
		else :
			for etat in self.etats_possibles():
				self.suite_etats.append(etat)
				self.suite_epsilon.append(0)
				self.execute()
				if self.bool : 
					break
				else:
					self.suite_etats.pop()
					self.suite_epsilon.pop()
			
			# on regarde si ça a marché et si non, 
			#on essaie avec des epsilon transitions :
			if self.tentative_epsilon() :
				for etat in (self.auto.image_epsilon(self.etat_actuel())):
					self.suite_etats.append(etat)
					self.suite_epsilon.append(1)
					self.execute()
					if self.bool : 
						break
					else:
						self.suite_etats.pop()
						self.suite_epsilon.pop()
			
						
			
		
		
		
			
			