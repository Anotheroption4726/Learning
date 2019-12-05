/*
/*
/*_HELLO WORLD PROGRAM_____________________________________________*/

#include <stdio.h>

int main(void)
{
	printf("Hello World!\n");
	return 0;
}




/*
/*
/*_VARIABLES_______________________________________________________*/

char lettre = 'A';
/*  taille: 1 octet/byte
	exemples: 'a', 'b', 'c', '2'  */

int nombreEntier = 10;
/*  taille: 4 octets/bytes
	exemples: 16(decimal), 020(octal), 0x10(hexadecimal)  */

float nombreRationnel = 2.5f;
/*  taille: 4 octets/bytes
	exemples: 0.00225, 2.25e-3  */

double nombreDouble = 2.0745;
/*  taille: 8 octets/bytes
	tout float est considéré comme étant un double par le compilateur si l'on ne rajoute pas de "f" après sa valeur  */

/*
	-long, long long: increases memory size of variable. can be used with int, double
	-short: reduces memory size of variable. takes half space on some systems
	-signed, unsigned: specifies if negative numbers are used or not. int or char

	-examples:
	short
	short int
	signed short
	signed short int
	unsigned short
	unsigned short int
	unsigned short int
	signed
	signed int
	unsigned
	unsigned int
	unsigned int
	long
	long int
	signed long
	signed long int
	unsigned long
	unsigned long int
	unsigned long int
	long long
	long long int
	signed long long
	signed long long int
	unsigned long long
	unsigned long long int
*/




/*
/*
/*_TAILLE DE TYPE/OPERATEUR________________________________________*/

sizeof(nomDeVariable)	/*Récupère la taille mémoire (en bytes) de la variable nomDeVariable*/

printf("%lu\n", sizeof(char));	/*Affiche 1*/
printf("%lu\n", sizeof(int));	/*Affiche 4*/
printf("%lu\n", sizeof(float));	/*Affiche 4*/
printf("%lu", sizeof(double));	/*Affiche 8*/

/*When sizeof() is used with an expression, it returns the size of the expression:*/
int a = 0; 
double d = 10.21; 
printf("%lu", sizeof(a + d));	/*Affiche 8*/




/*
/*
/*_TYPE CASTING____________________________________________________*/

float f;
int i = 10;
f = (float) i;	/*assigned 10.0 to f*/

f = 3.14;
i = (int) f;	/*assigned 3 to i. doesn't round the number*/




/*
/*
/*_INPUT/OUTPUT____________________________________________________*/

/*

Symboles/Spécificateurs de format :


*NOMBRES ENTIERS

- %d ou %i : entier relatif (type int)

- %u : entier naturel, unsigned (type int)

- %o : entier exprimé en octal (type int)

- %x : entier exprimé en hexadécimal (type int)


*NOMBRES RATIONNELS

- %f : rationnel en notation décimale (type double)

- %e : rationnel en notation scientifique (type double)


*CARACTERES

- %c : caractère (type int)

- %s : chaîne de caractères (type char*)

*/


printf("Hello World!\n");	/*Affiche "Hello World!" puis saute une ligne*/


int entier = 4;
printf("%d", entier);		/*Affiche 4 sans aller à la ligne*/

char caractere = 'A';
printf("%c\n", caractere);	/*Affiche "A" puis saute une ligne*/

int entier_1 = 10;
printf("%d\n", entier_1);	/*Affiche 10 puis saute une ligne*/

int entier_2 = 12;
printf("%i\n", entier_2);	/*Affiche 12 puis saute une ligne*/


long nombreLong = 1500000;
printf("%ld, %lx", nombreLong, nombreLong); /*Affiche 1500000 et 16e360 sans aller à la ligne*/


float nombreRationnel = 12.1234;
double nombreDouble = 12.123456789;
long double nombreDoubleLong = 15.5;

printf("%f", nombreRationnel);		/*Affiche 12.123400 sans aller à la ligne*/
printf("%f", nombreDouble);			/*Affiche 12.123457 sans aller à la ligne*/
printf("%e", nombreRationnel);		/*Affiche 1.212340e+01 sans aller à la ligne*/
printf("%e", nombreDouble);			/*Affiche 1.212346e+01 sans aller à la ligne*/
printf("%Le", nombreDoubleLong);	/*Affiche 1.550000e+01 sans aller à la ligne*/

/*Pour pouvoir traiter correctement les arguments du type long double, il faut utiliser les spécificateurs %Lf et %Le.*/
