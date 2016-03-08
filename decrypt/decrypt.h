#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define DECRYPT_ERROR 1
#define DECRYPT_OK 0

int count_str_len(unsigned char * str);
int ToLowerCase(unsigned char *str);
int Decrypt(unsigned char * str, unsigned char *code);