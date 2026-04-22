#!/usr/bin/env bash
set -e

if [ -z "$GCC_LIB_PATH" ]; then
  for d in /nix/store/*-gcc-*-lib/lib; do
    if [ -f "$d/libatomic.so.1" ]; then
      arch=$(file -b "$d/libatomic.so.1.2.0" 2>/dev/null | grep -o 'ELF 64-bit' || true)
      if [ -n "$arch" ]; then
        GCC_LIB_PATH="$d"
        break
      fi
    fi
  done
fi

export LD_LIBRARY_PATH="${GCC_LIB_PATH}:${LD_LIBRARY_PATH}"
exec python web.py
