#Your task is to use for loops to display only odd natural numbers from  1 to  9 .
# Loop through numbers from 1 to 9
for num in {1..9}
do
  # Check if the number is odd
  if (( $num % 2 == 1 )); then
    echo $num
  fi
done