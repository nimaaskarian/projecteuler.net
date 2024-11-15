SRC = $(filter-out math-helper.c, $(wildcard *.c))
TARGETS := $(SRC:.c=)
CFLAGS := -Ofast
BIN := bin
TARGET_PATHS := $(patsubst %, ${BIN}/%, $(TARGETS))

$(TARGETS): %: ${BIN}/%
	@exec 2>&1; ./$(BIN)/$@

$(TARGET_PATHS): ${BIN}/%: %.o math-helper.o 
		@exec 2>&1; ${CC} ${CFLAGS} $^ -o $@ ${LDFLAGS}

math-helper.o: math-helper.c math-helper.h
	@exec 2>&1; $(CC) -c $(CFLAGS) math-helper.c -o $@

%.o: %.c
	@${CC} -c ${CFLAGS} $< 1>&2

clean:
	rm -f *.o ${TARGET_PATHS}
