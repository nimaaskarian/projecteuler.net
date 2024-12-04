#include <stdbool.h>
#include "math-helper.h"

DIGIT_COUNT(uint);
TENPOW(uint);

uint intpow(uint a, uint b)
{
  uint out = 1;
  while (b) {
    out *= a;
    b--;
  }
  return out;
}

uint nth_digit_left(uint num,uint n,uint base)
{
  return (num%intpow(base, n))/intpow(base,(n-1));
}

bool is_palindrome(uint n)
{
  if (n < 10) {
    return false;
  }
  uint k = digit_count(n);
  for (uint i = 0; i < k; ++i) {
    uint rev = nth_digit_left(n,k-i, 10);
    uint cur = nth_digit_left(n,i+1, 10);
    if (rev != cur) {
      return false;
    }
  }
  return true;
}

uint reverse_num(uint n)
{
  if (n < 10) {
    return n;
  }
  uint k = digit_count(n);
  uint out = 0;
  for (int i = k-1; i >= 0; --i) {
    out += (n%10) * intpow(10, i);
    n/=10;
  }
  return out;
}
