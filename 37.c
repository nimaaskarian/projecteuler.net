#include <stdio.h>
#include <stdbool.h>

#include "math-helper.h"
DECLR_TENPOW(int);
DECLR_DIGIT_COUNT(int);

int truncate(int n, int count, bool is_left) {
  if (is_left) {
    return n/tenpow(digit_count(n)-count);
  }
  return n%tenpow(count);
}

bool is_prime(int n) {
  for (int i = 2; i*i <= n ; ++i) {
    if (n%i == 0) return false;
  }
  return n > 1;
}

bool is_truncatable(int n) {
  for (int i = 1; i < digit_count(n); ++i) {
    if (!is_prime(truncate(n, i, false))) {
      return false;
    }
    if (!is_prime(truncate(n, i, true))) {
      return false;
    }
  }
  return is_prime(n);
}

int main () {
  int count = 0;
  for (int n = 23; ;) {
    if (is_truncatable(n)) {
      printf("%d\n", n);
      count+=1;
      if (count == 11) break;
    }
    if (n%10 == 3) {
      n+=4;
    } else {
      n+=6;
    }
  }
  return 0;
}

