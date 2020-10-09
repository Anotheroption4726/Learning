#include <stdio.h>

int main(void)
{
	char initial_1, initial_2, initial_3;
	int age;

	printf("Enter your initials, followed by your age: ");
	scanf("%c %c %c %d", &initial_1, &initial_2, &initial_3, &age);
	printf("My initials are %c%c%c and my age is %d.\n", initial_1, initial_2, initial_3, age);
	
    return(0);
}
