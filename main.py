# -*- coding: utf-8 -*-
from PIL import Image
import sys
import dual_gradient
import seam_carving

def main():	
	chemin = str(sys.argv[1])
	k = int(sys.argv[2])
	kp = int(sys.argv[3])
	if(k < 0):
		print("Votre troisième argument est invalide : argument négatif")
		quit()
	if(kp < 0):
		print("Votre quatrième argument est invalide : argument négatif")
		quit()
	im = Image.open(chemin)
	if(k > 100):
		print("Votre troisième argument est invalide : dépassement de la taille de l'image")
		quit()
	if(kp > 100):
		print("Votre quatrième argument est invalide : dépassement de la taille de l'image")
		quit()
	img = dual_gradient.gradient(im)
	compteur = (k/100)*im.size[1]
	while compteur>0:
		im, img = seam_carving.vertical_carving(im,img)
		compteur-=1
	compteur = (kp/100)*im.size[0]
	while compteur>0:
		im, img = seam_carving.horizontal_carving(im,img)
		compteur-=1
	im.save("result.jpg") 
if __name__ == "__main__":
    main()
