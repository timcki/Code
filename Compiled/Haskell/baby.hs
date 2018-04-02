doubleMe x = x + x
doubleUs x y = doubleMe x + doubleMe y
doubleSmallNumber x = if x > 100
                        then x
                        else x*2
boomBangs xs = [ if x < 10 then "BOOM!" else "BANG!" | x <- xs, odd x]
removeNonUppercase::[Char] -> [Char]
removeNonUppercase str = [ s | s <- str, s `elem` ['A'..'Z']]
factorial :: Integer -> Integer
factorial x = product [1..x]
