#include <stdio.h>
#include <stdbool.h>

#include "math-helper.h"
DECLR_TENPOW(int);
DECLR_DIGIT_COUNT(int);

int truncate(int n, int count, int digit_count) {
  if (digit_count) {
    return n/tenpow(digit_count-count);
  }
  return n%tenpow(count);
}

bool is_prime(int n) {
  if (n == 2) return true;
  if (n % 2 == 0) return false;
  for (int i = 3; i*i <= n; i+=2) {
    if (n%i == 0) return false;
  }
  return n > 1;
}

bool is_truncatable(int n) {
  int count = digit_count(n);
  for (int i = 1; i < count; ++i) {
    if (!is_prime(truncate(n, i, 0))) {
      return false;
    }
    if (!is_prime(truncate(n, i, count))) {
      return false;
    }
  }
  return is_prime(n);
}

int main () {
  int count = 0;
  int sum = 0;
  for (int n = 23; ;) {
    if (is_truncatable(n)) {
      count+=1;
      sum+=n;
      if (count == 11) break;
    }
    if (n%10 == 3) {
      n+=4;
    } else {
      n+=6;
    }
  }
  printf("%d\n", sum);
  return 0;
}

