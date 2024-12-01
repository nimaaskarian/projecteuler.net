#!/usr/bin/env bash
last=$(fd -tf --max-depth 1 | grep '[0-9]' | grep -v '.txt' | tail -n 1 | sed 's/^0\+//')
last=${last%.*}
next=$((last+1))

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

 [ $FORMAT ] && printf "%04d%s\n" $next "$ARGS" || echo "$next$ARGS"
