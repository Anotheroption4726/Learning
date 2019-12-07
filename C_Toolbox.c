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


long nombreLong = 1500000;
printf("%ld, %lx", nombreLong, nombreLong); /*Affiche 1500000 et 16e360 sans aller à la ligne*/


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