#include <stdio.h>
#include <string.h>

void vulnerable_function(char *input)
{
	char buffer[100];
	strcpy(buffer, input);
	printf("Received Input: %s\n", buffer)
}


int main()
{
	char input[256];
	printf("Enter some text: ");
	fgets(input, 256, stdin);
	vulnerable_function(input);
	return 0;
}
