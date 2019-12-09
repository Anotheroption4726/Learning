#include <stdio.h>
//	«Standard Input/Output Header» ou «En-tête Standard d'Entrée/Sortie», est l'en-tête de la bibliothèque 
//	standard du C déclarant les macros, les constantes et les définitions de fonctions utilisées dans les 
//	opérations d'entrée/sortie.

#define MAX 10
//Constante?




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
	exemples: 'a', 'b', 'c', '2'
	min : -128
	max : 127
	unsigned max : 255
*/

int nombreEntier = 10;
/*  taille: 4 octets/bytes
	exemples: 16(decimal), 020(octal), 0x10(hexadecimal)
	min : -2147483648
	max : 2147483647
	unsigned max : 4294967295
*/

float nombreRationnel = 2.5f;
/*  taille: 4 octets/bytes
	exemples: 0.00225, 2.25e-3
*/

double nombreDouble = 2.0745;
/*  taille: 8 octets/bytes
	tout float est considéré comme étant un double par le compilateur si l'on ne rajoute pas de "f" après sa valeur
*/

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
/*_TYPE CASTING____________________________________________________*/

float f;
int i = 10;
f = (float) i;	/*assigned 10.0 to f*/

f = 3.14;
i = (int) f;	/*assigned 3 to i. doesn't round the number*/




/*
/*
/*_ARRAYS__________________________________________________________*/

int values[100];
char name[25];

int values[4] = {0, 1, 2, 3};						//Array size 4. Index from 0 to 3
char greeting[5] = {'h', 'e', 'l', 'l', 'o'};		//Array size 5. Index from 0 to 4
char name[] = {'f', 'r', 'e', 'd'};					//Array size 4. Index from 0 to 3
int bigarray[] = {[0] = 1, [1] = 10, [999] = 0};	//Array size 1000. Index from 0 to 999

int values[2][2];
int values[2][2] = {{0,1},{1,0}};
int values[2][2] = {0,1,1,0};




/*
/*
/*_INPUT/OUTPUT____________________________________________________*/

/*

Symboles/Spécificateurs de format :

- %p : addresse pointeur (en hexadécimal)


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


printf("%", );
scanf("%", &);

printf("Hello World!\n");	/*Affiche "Hello World!" puis saute une ligne*/


int entier;
printf("%d", entier);		/*Affiche 0 sans aller à la ligne*/

char caractere = 'A';
printf("%c\n", caractere);	/*Affiche "A" puis saute une ligne*/


int entier_1 = 10;
int entier_2 = 12;

printf("%d\n%d\n", entier_1, entier_2);	/*Affiche 10 puis saute une ligne. Affiche 12 puis saute une ligne*/


char caractere = 'C';
int entier = 8;
printf("Le caractère selectionné est %c\n", 'B');			/*Affiche "Le caractère selectionné est B" puis saute une ligne*/
printf("Caractère: %c\nEntier: %d\n", caractere, entier);
/*Affiche:
	Le caractère selectionné est B
	Caractère: C
	Entier: 8
*/


int nombreHexadecimal = 10;
printf("%x\n", nombreHexadecimal);				//Affiche "a" car "10" en héxadécimal équivaut à "a" ou "000A"


long nombreLong = 1500000;
printf("%ld, %lx", nombreLong, nombreLong); 	/*Affiche 1500000 et 16e360 sans aller à la ligne*/


float nombreRationnel = 12.1234;
double nombreDouble = 12.123456789;
long double nombreDoubleLong = 15.5;

printf("%f", nombreRationnel);							/*Affiche 12.123400 sans aller à la ligne*/
printf("%f", nombreDouble);								/*Affiche 12.123457 sans aller à la ligne*/
printf("%e", nombreRationnel);							/*Affiche 1.212340e+01 sans aller à la ligne*/
printf("%e", nombreDouble);								/*Affiche 1.212346e+01 sans aller à la ligne*/
printf("%lu\n", (unsigned long)sizeof(nombreDouble));	/*Affiche 8 puis saute une ligne*/
printf("%Le", nombreDoubleLong);						/*Affiche 1.550000e+01 sans aller à la ligne*/

/*Pour pouvoir traiter correctement les arguments du type long double, il faut utiliser les spécificateurs %Lf et %Le.*/


int entier;
char caractere;

scanf("%d", &entier);					/*Récupère un input clavier en int et l'insère dans la variable "entier"*/
scanf("%c %d", &caractere, &entier);	/*Récupère deux inputs clavier, le premier en char et le deuxième en int. On les insère dans leurs variables respectives*/

printf("Inputs selectionnés: %c%d.\n", caractere, entier);	/*Affiche les valeurs récupérées dans la console*/




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
/*_POINTERS________________________________________________________*/

int* nombreEntier;
int *nombreEntier_1;
int * nombreEntier_2;
int* nombreEntier_1, nombreEntier_2;


int nombreEntier;
int* p_nombreEntier;
p_nombreEntier = &nombreEntier;


int* p_nombreEntier, nombreEntier;
nombreEntier = 5;
p_nombreEntier = &nombreEntier;


int nombreEntier = 8;
printf("Address of variable nombreEntier: %d\n", &nombreEntier);
//On remarquera que les valeurs changent à chaque fois que l'on relance le programme car l'adresse est différente pour chaque 
//itération.

//!!! ATTENTION!!! Utiliser un %d est fortement déconseillé pour manipuler une addresse mémoire.
//On ne peut pas trop prédire ce qui va en sortir (résultat négatif par exemple).


int nombreEntier;
printf("Address of variable nombreEntier: %p\n", &nombreEntier);		//Affiche l'addresse mémoire de la variable nombreEntier


int nombreEntier;
int* p_nombreEntier = &nombreEntier;
printf("Address of variable nombreEntier: %p\n", p_nombreEntier);		//Affiche l'addresse mémoire de la variable nombreEntier


int* p_nombreEntier, nombreEntier;
nombreEntier = 3;
p_nombreEntier = &nombreEntier;
printf("%d\n", nombreEntier);											//Affiche "3"
printf("Address of variable nombreEntier: %p\n", p_nombreEntier);		//Affiche l'addresse mémoire de la variable nombreEntier


int* p_nombreEntier, nombreEntier;
nombreEntier = 6;
p_nombreEntier = &nombreEntier;
printf("%d\n", *p_nombreEntier);										// Affiche "6"

//Here, the address of "nombreEntier" is assigned to the "p_nombreEntier" pointer. To get the value stored in that address, we used "*p_nombreEntier".
//Note: In the above example, "p_nombreEntier" is a pointer, not "*p_nombreEntier". You cannot and should not do something like *p_nombreEntier = &nombreEntier;
//By the way, * is called the dereference operator (when working with pointers). It operates on a pointer and gives the value stored in that pointer.


int* p_nombreEntier, nombreEntier;
nombreEntier = 7;
p_nombreEntier = &nombreEntier;
*p_nombreEntier = 1;
printf("%d\n", *p_nombreEntier);										// Affiche "1"
printf("%d\n", nombreEntier);											// Affiche "1"


int* p_nombreEntier, nombreEntier;
nombreEntier = 7;
p_nombreEntier = &nombreEntier;
p_nombreEntier = 1;														//Programme ne marche pas: Segmentation fault (core dumped)
printf("%d\n", *p_nombreEntier);
printf("%d\n", nombreEntier);


int nombreEntier = 10;
int* p_nombreEntier = &nombreEntier; 
printf("Address of variable nombreEntier: %p\n", (void *)&nombreEntier);	//Affiche l'addresse mémoire de la variable nombreEntier
printf("Address of variable nombreEntier: %lu\n", p_nombreEntier);			//Affiche l'addresse mémoire de la variable nombreEntier sous forme long unsigned (non recommandé)

//void * est un pointeur sur un type non définit. Ce type de pointeur est utilisé, lorsque le type de pointeur qui lui affecté change suivant les 
//situations. On peut réutiliser les données se trouvant à l'adresse pointée par ce type de pointeur, en faisant un casting.

//Une addresse mémoire peut s'afficher en valeur int (ou autre). En fonction du compilateur, le format spécifié sera donc lu mais affichera un 
//message d'alerte lors de la compilation




/*
/*
/*_OPERATORS_______________________________________________________*/

/*

*ARITHMETIC

	- + : addition

	- - : substraction

	- / : division

	- * : multiplication
    
    - % : modulo
    
    - -- : decrement (post and pre)
    
    - ++ : increment (post and pre)


*ASSIGNMENT

These all perform an arithmetic operation on the value and assign the result to the value:

   counter = counter + 1; 

can be reduced to:

	counter += 1;           

    - = : equals
    
    - *= : multiply
    
    - /= : divide
    
    - %= : modulus
    
    - += : add
    
    - -= : subtract
    
    - <<= : left shift
    
    - >>= : right shift
    
    - &= : bitwise AND
    
    - ^= : bitwise exclusive OR (XOR)
    
    - |= : bitwise inclusive OR


*LOGICAL/RELATIONAL

    - == : equal to
    
    - != : not equal to
    
    - > : greater than
     
    - < : less than
    
    - >= : greater than or equal to
    
    - <= : less than or equal to
    
    - && : logical AND
    
    - || : logical OR
    
    - ! :ogical NOT


*BITWISE
    
    - & : AND (Binary operator)
    
    - | : inclusive OR
    
    - ^ : exclusive OR
    
    - << : shift left

    - >> : shift right
    
    - ~ : one's complement


*OTHER

    - sizeof() : size of objects and data types. "strlen()" may also be of interest.
    
    - & : Address of (Unary operator)
        
    - * : pointer (Unary operator)
    
    - ? : conditional expressions
    
    - : : conditional expressions
    
    - , : Series operator


*PRECEDENCES

- Precedence 1 : () [] -> .
	use: pointers, separators
	associativity: left to right

- Precedence 2 : ! ~ ++ -- + - * & (type) sizeof
	use: unary operations
	associativity: right to left

- Precedence 3 : * / %
	use: binary operations
	associativity: left to right

- Precedence 4 : + -
	use: binary operations
	associativity: left to right

- Precedence 5 : << >>
	use: bit-shift
	associativity: left to right

- Precedence 6 : < <= > >=
	use: logical comparison
	associativity: left to right

- Precedence 7 : != ==
	use: logical comparison
	associativity: left to right

- Precedence 8 : &
	use: bitwise mask
	associativity: left to right

- Precedence 9 : ^
	use: bitwise mask
	associativity: left to right

- Precedence 10 : |
	use: bitwise mask
	associativity: left to right

- Precedence 11 : &&
	use: logical AND
	associativity: left to right

- Precedence 12 : ||
	use: logical OR
	associativity: left to right

- Precedence 13 : ?:
	use: if/else
	associativity: right to left

- Precedence 14 : += -= *= /= %= &= ^= |= <<= >>= =
	use: compact operators
	associativity: right to left

- Precedence 15 : .
	use: separator
	associativity: left to right


A variable (in logical sense) is either TRUE or FALSE. Variable is FALSE if it is zero. Variable is TRUE if it is non-zero.

	int x = 7;				TRUE
	double z = 0.0001;		TRUE
	char abc = 0x00;		FALSE
	char x = 'a';			TRUE
	float b = 0.0;			FALSE

*/




/*
/*
/*_LOOPING AND BRANCHING______________________________________________*/

int i;

for (i = 10; i >= 0; i--)
{
	print("%d\n", i);
}


int cnt 10;

while (cnt >= 0)
{
	print("%d\n", cnt);
	cnt--;
}

do
{
	print("%d\n", cnt--);
} while (cnt >= 0);


/*
break; can be used to break out of a loop
continue; is used to bypass the rest of the loop and begin the next iteration
*/




/*
/*
/*_READING/WRITTING FILES__________________________________________*/

int nombreEntier;
FILE *filePointer_read;
FILE *filePointer_write;

filePointer_read = fopen("fileToRead.txt", "r");
filePointer_write = fopen("fileToWrite.txt", "w");

if(filePointer_read == NULL)
{
	printf("Could not open file.\n");
	return(0);
}

if(filePointer_write == NULL)
{
	printf("Could not open output.txt for writting.\n");
	return(0);
}

fscanf(filePointer_read, "%d", &nombreEntier);						//lis la première information de type int située dans le fichier et l'insère dans la variable "nombreEntier"
fprintf(filePointer_write, "nombreEntier is: %d\n", nombreEntier);	//Insertion de l'information dans un autre fichier

fclose(filePointer_read);
fclose(filePointer_write);