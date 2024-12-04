#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define uint unsigned long long
#include "math-helper.h"

#define UPPER 10000

bool is_lyrchrel(uint n) {
  for (uint i = 0; i < 50; ++i) {
    printf("self %llu\n", n);
    n += reverse_num(n);
    printf("rev %llu\n", n);
    if (is_palindrome(n)) {
      return false;
    }
  }
  return true;
}

int main(int argc, char *argv[])
{
  unsigned int count = 0;
  for (uint n = 1; n < UPPER; ++n) {
    if (is_lyrchrel(n)) {
      printf("%llu\n", n);
      count+=1;
    }
  }
  printf("%u\n", count);
  return EXIT_SUCCESS;
}
