import time

def benchmark(callable,*args, avg=None):
    start = time.time()
    try:
        out = callable(*args)
    except KeyboardInterrupt:
        print("Interrupted. Exiting...")
        exit(0)
    end = time.time()
    print(callable.__name__,end - start, end="")
    if avg is not None:
        avg[0] += 1
        avg[1] += end - start
        print(", average: ", avg[1]/avg[0], end="")
    print()
    return out

def s_iter2int(iter):
    return int("".join(iter))

def iter2int(iter):
    return sum(map(lambda ix: ix[1]*10**ix[0], enumerate(reversed(iter))))

