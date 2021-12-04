import Data.List
import Data.Ord
import Data.Char
import Control.Arrow


main :: IO ()
main = print . (p1 &&& p2) . lines =<< readFile "03.txt"


p1 :: [String] -> Int
p1 table = gamma * epsilon
  where
    transposed = transpose table
    gamma = binaryStringToInt $ map mostCommon transposed
    epsilon =  binaryStringToInt $ map leastCommon transposed


p2 :: [String] -> Int
p2 table = oxygen * co2
  where
    filterNonPrefix :: (String -> Char) -> [String] -> String
    filterNonPrefix commonality lines
      | any null lines  = []
      | otherwise = let commonBit = commonality (head <$> lines)
                    in  commonBit : filterNonPrefix commonality [bits | (bit:bits) <- lines, commonBit == bit]

    oxygen = binaryStringToInt $ filterNonPrefix mostCommon table
    co2    = binaryStringToInt $ filterNonPrefix leastCommon table


binaryStringToInt :: String -> Int
binaryStringToInt = foldl' (\acc d -> acc * 2 + digitToInt d) 0


mostCommon, leastCommon :: String -> Char
mostCommon bits  = head $ maximumBy (comparing length) $ group $ sort bits-- countToBinaryString 1 . count
leastCommon bits = head $ minimumBy (comparing length) $ group $ sort bits -- countToBinaryString 0 . count




-- my other approach to counting. problematic on leastCommon
-- count :: String -> (Int, Int) -- style "1101" to (3,0)
-- count s = (ones, zeros)
--   where
--     ones = length $ filter (== '1') s
--     zeros = length s - ones

-- countToBinaryString :: Int -> (Int, Int) -> Char
-- countToBinaryString criteria (x, y)
--   | x > y = if criteria == 1 then '1' else '0'
--   | x < y = if criteria == 1 then '0' else '1'
--   | otherwise = case criteria of
--                 1 -> '1'
--                 0 -> '0'

--                 _ -> error "bad criteria"
-- mostCommon bits  = countToBinaryString 1 . count
-- leastCommon bits = countToBinaryString 0 . count
