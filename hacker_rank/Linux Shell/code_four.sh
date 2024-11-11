#Given two integers, X and Y, find their sum, difference, product, and quotient.
read -p "Enter the first integer X" X
read -p "Enter the first integer Y" Y

sum=$((X+Y))
difference=$((X-Y))
product=$((X*Y))
quotient=$((X/Y))

echo $sum
echo $difference
echo $product
echo $quotient