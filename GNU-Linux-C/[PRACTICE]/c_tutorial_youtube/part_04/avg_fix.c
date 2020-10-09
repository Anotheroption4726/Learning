#include <stdio.h>


int main(void)
{
	int totalNumbers = 0, inputValue, totalValue = 0;	//if you don't want to set the zero values, delare this variables as global variables aka outside of main() 
	float average;

	printf("How many numbers do you want to compute?\n");
	scanf("%d", &totalNumbers);

	if (totalNumbers > 0)
	{
		for (int i = 1; i <= totalNumbers; i++)
		{
			printf("Input number %d\n", i);
			scanf("%d", &inputValue);

			if (inputValue > 0)
			{
				totalValue += inputValue;
			}
			else
			{
				i--;
			}
		}

		average = (float)totalValue/totalNumbers;
		printf("Average is %f\n", average);
	}

	return(0);
}