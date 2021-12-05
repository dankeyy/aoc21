import Data.List
import Data.List.Split
import Data.Maybe

parse :: String -> [[Int]]
parse x = map read . splitOn "," <$> splitOn " -> " x


toCoordinateRange :: [[Int]] -> Maybe [(Int, Int)] --[[3,2], [2,3]] -> Just [(2,2),(2,3),(3,2),(3,3)]
toCoordinateRange xs | null xs || any null xs = Nothing
toCoordinateRange [x1:y1:_, x2:y2:_]
  | x1 /= x2 && y1 /= y2 = Nothing
  | otherwise            = Just [(x, y) | x <-[bottomX..topX], y <- [bottomY..topY]]
  where
    (bottomX, topX) = (min x1 x2, max x1 x2)
    (bottomY, topY) = (min y1 y2, max y1 y2)


countOverlap :: [(Int, Int)] -> Int
countOverlap = length . filter ((>1). length) . group . sort

solve :: [String] -> Int
solve = countOverlap . concat . mapMaybe (toCoordinateRange . parse)

x = ["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9", "3,4 -> 1,4", "0,0 -> 8,8", "5,5 -> 8,2"]

main :: IO ()
main = print . solve . lines =<< readFile "05.txt"
