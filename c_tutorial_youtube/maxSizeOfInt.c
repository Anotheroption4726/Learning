#include <stdio.h>

int main(void)
{
	int testInt = 2147483649;
	printf("2147483649 doesn't fit into int value, that's why we get %d\n instead", testInt);
	return 0;
}