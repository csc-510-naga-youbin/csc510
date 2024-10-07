#!/bin/bash

# List files containing the word "sample" and at least 3 occurrences of the word "CSC510"
grep -l "sample" file* | while read -r file; do
  count=$(grep -o "CSC510" "$file" | wc -l)
  if [ "$count" -ge 3 ]; then
    echo "$file:$count"
  fi
done | sort -t: -k2,2nr | uniq | while IFS=: read -r file count; do
  size=$(stat -f%z "$file")
  echo "$file:$count:$size"
done | sort -t: -k2,2nr -k3,3nr | uniq | sed 's/file_/filtered_/' | cut -d: -f1