#include "decrypt.h"
#define MAXLEN 1024

int main() {
	unsigned char *str = (unsigned char *)malloc(sizeof(char)*1024);
	unsigned char *code;

	code = new unsigned char(2);
	str[10] = '\0';

	printf("Please input your Ciphertext (less than 1024 latter)\n");
	for (int i = 0; i < 1025; i++)
	{
		scanf("%c", str + i);
		if (str[i] == '\n')
		{
			str[i] = '\0';
			break;
		}
	}
	printf("your ciphertext is \"%s\"\n", str);
	int str_length = count_str_len(str);
	char str_ori[str_length];
	for (int i = 0; i < str_length; i++)
	{
		str_ori[i] = str[i];	
	}

	printf("the plaintext may be:\n");
	for (int i = 0; i < 26; i++)
	{
		code = new unsigned char(i + 65);
		code[1] = '\0';
		for (int j = 0; j < str_length; j++)
		{
			str[j] = str_ori[j];
		}
		Decrypt(str, code);
		if (i < 10)
		{
			printf(" %d %s\n", i, str);
		}
		else {
			printf("%d %s\n", i, str);
		}
	}

	scanf("%c", str);
	return 0;
}