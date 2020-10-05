{- Project Euler: Problem 1
 - If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 - Find the sum of all the multiples of 3 or 5 below 1000.
 -}

sumOfMultiples :: [Integer] -> Integer -> Integer
sumOfMultiples mults limit =
    sum[i| i <- [1..(limit-1)], or (map (\x -> i `mod` x == 0) mults)]
   
main = do
    let answer = sumOfMultiples [3,5] 1000
    print answer
