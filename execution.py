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

import automate

class execution :
	def __init__(self, auto_arg, mot_arg):
		self.automate.auto = auto_arg
		self.mot = mot_arg
		self.suite = []
		self.bool = False
	
	# sous-fonction auxiliaire récursive
	def auxiliaire (self, etat, position):
	
		self.suite.append(etat)
		
		if (position == len(self.mot)):
			if self.automate.auto.est_final(etat):
				self.bool = True
			else
				self.suite.pop()
		
		else
			etats_suivants = self.automate.auto.image(etat, self.mot[position])
			etat_suivant = 0
						
			while( not(self.bool) and (etat_suivant<len(etats_suivants))):
				self.auxiliaire(etats_suivants[etat_suivant],position+1)
				etat_suivant = etat_suivant+1
				
			if not(self.bool):
				self.suite.pop()
			
				
		
	