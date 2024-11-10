#define DECLR_DIGIT_COUNT(TYPE) TYPE digit_count(TYPE);
#define DIGIT_COUNT(TYPE) \
TYPE digit_count(TYPE n) { \
  TYPE count = 0; \
  while (n > 0) { \
    count += 1; \
    n/=10; \
  } \
  return count; \
}

#define DECLR_TENPOW(TYPE) TYPE tenpow(TYPE);
#define TENPOW(TYPE) \
TYPE tenpow(int n) \
{ \
  TYPE out = 1; \
  for (; n ; --n) { \
    out*=10; \
  } \
  return out; \
}
