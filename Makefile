SRC = $(filter-out math-helper.c, $(wildcard *.c))
TARGETS := $(SRC:.c=)
CFLAGS := -Ofast

$(TARGETS): %: %.o math-helper.o
	${CC} ${CFLAGS} $^ -o $@ ${LDFLAGS}

math-helper.o: math-helper.c math-helper.h
	$(CC) -c $(CFLAGS) math-helper.c -o $@

%.o: %.c
	${CC} -c ${CFLAGS} $<

clean:
	rm -f *.o $(TARGETS)
