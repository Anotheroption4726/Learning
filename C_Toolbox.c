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

float nombre = 2.5f;
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