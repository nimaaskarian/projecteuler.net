#!/usr/bin/env bash
help(){
  echo "Usage: $0 -f append-strings"
}

ARGS=""
while [[ $# -gt 0 ]]; do
  case $1 in
    -f|--format)
      FORMAT="1"
      shift
      ;;
    -l|--lang)
      HAS_LANG="1"
      shift
      ;;
    -*|--*)
      echo "Unknown option $1"
      exit 1
      ;;
    *)
      ARGS+="$1"
      shift
      ;;
  esac
done

if [ "$HAS_LANG" ]; then
  last=$(fd -tf --max-depth 1 '[0-9]+.\w+' --exclude "*.txt" | grep "$ARGS" | tail -n 1 | sed 's/^0\+//')
  else
  last=$(fd -tf --max-depth 1 '[0-9]+.\w+' --exclude "*.txt" | tail -n 1 | sed 's/^0\+//')
fi
last=${last%.*}
next=$((last+1))


[ $FORMAT ] && printf "%04d%s\n" $next "$ARGS" || echo "$next$ARGS"
