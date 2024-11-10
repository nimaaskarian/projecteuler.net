#include <stdio.h>
#include "math-helper.h"
TENPOW(long double);

int main() {
  printf("%Lf\n", tenpow(30));
  return 0;
}
