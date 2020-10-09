#include <stdio.h>


int main(void)
{
	int totalNumbers = 0, inputValue, totalValue = 0, valueIsRead; 
	float average;

	printf("Input some values\n");
	valueIsRead = scanf("%d", &inputValue);

	while (valueIsRead > 0)
	{
		if (inputValue > 0)
		{
			totalNumbers ++;
			totalValue += inputValue;
		}

		valueIsRead = scanf("%d", &inputValue);
	}

	// In UNIX terminal, press "ctrl+d" to quit "scanf()" hence returning a value of 0 to "valueIsRead" thus ending the loop

	average = (float)totalValue/totalNumbers;
	printf("Average is %f\n", average);

	return(0);
}