#include <stdio.h>

int sum(int n, int k) {
  n /= k;
  return k * n * (n+1) / 2;
}

int main(int argc, char *argv[]) {
  printf("%d\n", sum(999, 5)+sum(999,3)-sum(999,15));
  return 0;
}
