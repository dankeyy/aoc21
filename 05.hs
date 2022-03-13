import Data.List
import Data.Maybe (mapMaybe)
import Data.List.Split (splitOn)
import Control.Arrow ((&&&))

type Point = (Int, Int)


toCoordinateRange :: Bool -> [[Int]] -> Maybe [Point]
toCoordinateRange countDiagonals [x1:y1:_, x2:y2:_] =
  let base = Just $ zip (range x1 x2) (range y1 y2)
        where range start stop = [start, start + step ..stop]
                where step = signum $ stop - start
  in
    if countDiagonals || (x1 == x2 || y1 == y2)
    then base
    else Nothing

toCoordinateRange _ _ = Nothing


countOverlap :: [Point] -> Int
countOverlap = length . filter ((>=2) . length) . group . sort


parse :: String -> [[Int]]
parse x = map read . splitOn "," <$> splitOn " -> " x


solve :: Bool -> [String] -> Int
solve countDiagonals = countOverlap . concat . mapMaybe (toCoordinateRange countDiagonals . parse)


main :: IO ()
main = print . (solve False &&& solve True) . lines =<< readFile "05.txt"
