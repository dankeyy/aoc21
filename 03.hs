import Data.List (foldl', maximumBy, minimumBy, group, sort, transpose)
import Data.Ord (comparing)
import Data.Char (digitToInt)
import Control.Arrow ((&&&))


binToDec :: String -> Int
binToDec = foldl' (\acc d -> acc * 2 + digitToInt d) 0


mostCommon, leastCommon :: String -> Char
mostCommon bits  = head . maximumBy (comparing length) . group $ sort bits
leastCommon bits = head . minimumBy (comparing length) . group $ sort bits


p1 :: [String] -> Int
p1 table = gamma * epsilon
  where
    transposedTable = transpose table
    gamma   = binToDec $ map mostCommon  transposedTable
    epsilon = binToDec $ map leastCommon transposedTable


p2 :: [String] -> Int
p2 table = oxygen * co2
  where
    filterNonPrefix :: (String -> Char) -> [String] -> String
    filterNonPrefix commonality lines
      | any null lines  = []
      | otherwise = let commonBit = commonality (head <$> lines)
                    in  commonBit : filterNonPrefix commonality [bits | (bit:bits) <- lines, commonBit == bit]

    oxygen = binToDec $ filterNonPrefix mostCommon  table
    co2    = binToDec $ filterNonPrefix leastCommon table


main :: IO ()
main = print . (p1 &&& p2) . lines =<< readFile "03.txt"
