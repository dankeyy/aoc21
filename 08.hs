import Data.List.Split ( splitOn )
import Data.Maybe ( catMaybes )
import Data.Functor.Compose ( Compose (Compose, getCompose) )
import Control.Arrow ( (&&&) )
import qualified Data.Map as M
import qualified Data.Set as S

---------------------------------------------------------------------------------------------------------------------------------

countUniques :: String -> Int
countUniques line = length $ filter ((`elem` [2, 4, 3, 7]) . length) values
  where (_:values:_) = words <$> splitOn " | " line

p1 = sum . map countUniques
---------------------------------------------------------------------------------------------------------------------------------

interpretLine :: String -> Int
interpretLine line = read $ catMaybes $ (`M.lookup` mapping) <$> values
  where
    (signalPatterns:values:_) = getCompose $ S.fromList <$> Compose (words <$> splitOn " | " line)

    uniql n = head $ filter ((==n) . S.size) signalPatterns
    four = uniql 4
    seven = uniql 3

    inCommon a b = length $ S.intersection a b
    uniqlc47 len c4 c7 = head $ filter (\x -> length x == len && x `inCommon` four == c4 && x `inCommon` seven == c7) signalPatterns

    mapping = M.fromList [(uniqlc47 6 3 3, '0'), (uniql 2, '1'), (uniqlc47 5 2 2, '2'), (uniqlc47 5 3 3, '3'), (four, '4'),
                          (uniqlc47 5 3 2, '5'), (uniqlc47 6 3 2, '6'), (seven, '7'), (uniql 7, '8'), (uniqlc47 6 4 3, '9')]


p2 = sum . map interpretLine
---------------------------------------------------------------------------------------------------------------------------------

main :: IO ()
main = print . (p1 &&& p2) . lines =<< readFile "08.txt"
