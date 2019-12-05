#include <stdio.h>

int main(void)
{
	char caractere;
	int entier;

	printf("Veuillez entrer un caractère puis un nombre entier :\n");
	scanf("%c %d", &caractere, &entier);
	printf("Caractère: %c\nEntier: %d\n", caractere, entier);
	
    return(0);
}
