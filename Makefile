SRC = $(filter-out math-helper.c, $(wildcard *.c))
TARGETS := $(SRC:.c=)
RUSTSRC := $(wildcard *.rs)
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
	rm -f *.o ${TARGET_PATHS} Cargo.toml

Cargo.toml:
	@echo [package]  > $@
	@echo 'name = "projecteuler"'  >> $@
	@echo 'version = "0.1.0"' >> $@
	@echo 'edition = "2021"' >> $@
	@echo >> $@
	@for item in ${RUSTSRC}; do \
		echo '[[bin]]' >> $@; \
		echo "name = \"$${item%.*}\""  >> $@; \
		echo "path = \"$$item\""  >> $@; \
		echo >> $@; \
	done
	
$(RUSTSRC): Cargo.toml
	@cargo build --release
	@$(patsubst %.rs, ./target/release/%, $@)
