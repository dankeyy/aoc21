import Data.List
import Data.Maybe
import Data.List.Split
import Control.Arrow

type Point = (Int, Int)
type CountDiagonals = Bool

parse :: String -> [[Int]]
parse x = map read . splitOn "," <$> splitOn " -> " x

toCoordinateRange :: CountDiagonals -> [[Int]] -> Maybe [Point]
toCoordinateRange countDiagonals [x1:y1:_, x2:y2:_]
  | not countDiagonals = if x1 == x2 || y1 == y2 then base else Nothing
  | otherwise = base
  where base = Just $ zip (range x1 x2) (range y1 y2)
        range start stop = [start, start + step ..stop]
          where step = signum $ stop - start
toCoordinateRange _ _ = Nothing

countOverlap :: [Point] -> Int
countOverlap = length . filter ((>=2) . length) . group . sort

solve :: CountDiagonals -> [String] -> Int
solve countDiagonals = countOverlap . concat . mapMaybe (toCoordinateRange countDiagonals . parse)

main :: IO ()
main = print . (solve False &&& solve True) . lines =<< readFile "05.txt"

-- (0 0) (1 0) (2 0) (3 0) (4 0)
-- (0 1) (1 1) (2 1) (3 1) (4 1)
-- (0 2) (1 2) (2 2) (3 2) (4 2)
-- (0 3) (1 3) (2 3) (3 3) (4 3)
-- (0 4) (1 4) (2 4) (3 4) (4 4)

-- x = ["0,9 -> 5,9", "8,0 -> 0,8", "9,4 -> 3,4", "2,2 -> 2,1", "7,0 -> 7,4", "6,4 -> 2,0", "0,9 -> 2,9", "3,4 -> 1,4", "0,0 -> 8,8", "5,5 -> 8,2"]
