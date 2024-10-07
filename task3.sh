#!/bin/bash

# Extract passengers from 2nd class who embarked at Southampton,
# replace male/female labels with M/F, and calculate the average age.

# Debugging: Print the filtered lines
echo "Filtered lines:"
csvcut -c Pclass,Embarked,Age titanic.csv | csvgrep -c Pclass -m 2 | csvgrep -c Embarked -m S | csvlook

# Process the filtered lines and print the last line
csvcut -c Pclass,Embarked,Age,Sex titanic.csv | csvgrep -c Pclass -m 2 | csvgrep -c Embarked -m S | \
csvformat -T | sed 's/\tmale\t/\tM\t/; s/\tfemale\t/\tF\t/' | \
awk -F'\t' '{if ($3 != "" && $3 != "NA") {sum += $3; count += 1}} END {if (count > 0) print "Average Age:", sum / count}'