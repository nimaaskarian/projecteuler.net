#include <stdbool.h>
#include <stdio.h>

int encode(int n) {
  int value = 0;
  int count = 0;
  while (n) {
    value += 2 << (n % 10);
    n /= 10;
    count+=1;
  }
  return value + (2<<count);
}

inline bool six_multiples_has_same_digits(int n) {
  int n_e = encode(n);
  for (int k = 2; k <= 6; k++) {
    if (encode(k*n) != n_e) 
      return false;
  }
  return true;
}

int main(int argc, char *argv[])
{
  int n = 1;
  while (1) {
    if (six_multiples_has_same_digits(n))
      break;
    n+=1;
  }
  printf("%d\n", n);
  return 0;
}
