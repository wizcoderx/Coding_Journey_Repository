# Read in one character from STDIN.
# If the character is 'Y' or 'y' display "YES".
# If the character is 'N' or 'n' display "NO".
# No other character will be provided as input.
#url - https://www.hackerrank.com/challenges/bash-tutorials---getting-started-with-conditionals
read -n 1 character

if [[ "$character" == "Y" ]] || [[ "$character" == "y" ]]; then
    echo "YES"
elif [[ "$character" == "N" ]] || [[ "$character" == "n" ]]; then
    echo "NO"
fi
