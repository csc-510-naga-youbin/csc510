#!/bin/bash

# Step a: Extract 2nd class passengers who embarked at Southampton
gawk -F, '$3 == 2 && $13 ~/S/ {print $0}' titanic.csv > filtered_passengers.csv

# Step b: Replace male/female labels with M/F
sed -i 's/female/F/g; s/male/M/g' filtered_passengers.csv

# Step c: Calculate the average age of the filtered passengers
average_age=$(gawk -F, 'BEGIN {sum=0; count=0} $7 != "" && $7 != "Age" {sum += $7; count++} END {if (count > 0) print sum / count}' filtered_passengers.csv)

echo "Average age of filtered passengers: $average_age"
