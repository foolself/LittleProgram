#include "decrypt.h"

int count_str_len(unsigned char *str) {
	int i = 0;
	int str_length = 0;
	while(str[i] != '\0') {
		str_length++;
		i++;
	}
	return str_length;
}

int Decrypt(unsigned char *str, unsigned char *code) {
	if (str == NULL || code == NULL)
		return DECRYPT_ERROR;
	int i = 0;
	int str_length = count_str_len(str);

	if (str_length > 1024)
	{
		printf("plaintext length more than 1024\n");
		return DECRYPT_ERROR;
	}
	else if (code[1] != '\0') {
		printf("the key should be only one latter\n");
		return DECRYPT_ERROR;
	}

	if (ToLowerCase(str) != 0)
	{
		printf("error to tran plaintext to lower\n");
		return DECRYPT_ERROR;
	}

	if (ToLowerCase(code) != 0)
	{
		printf("error to tran the key to lower\n");
		return DECRYPT_ERROR;
	}

	int key = code[0] -97;
	for (i = 0; i < str_length; i++)
	{
		str[i] -= key;
		if (str[i] < 97)
			str[i] += 26;
	}

	return DECRYPT_OK;
}

int ToLowerCase(unsigned char *str) {
	if (str == NULL)
		return 0;

	int i = 0;

	for (i = 0; str[i] != '\0'; i++)
	{
		if (str[i] > 64 && str[i] < 91)
			str[i] += 32;
		else if (str[i] > 96 && str[i] < 123)
			;
		else {
			printf("you may inputed a char not latter\n");
			return 1;
		}
	}
	return 0;
}