> {-# LANGUAGE FlexibleContexts      #-}
> {-# LANGUAGE MultiParamTypeClasses #-}
 
> module Diagram where
 
> import           Data.Char        (digitToInt)
> import           Data.List.Split  (chunksOf)
> import           Data.Maybe       (listToMaybe)
> import           Diagrams.Prelude
 
> primeLayout :: (Renderable (Path V2 n) b, TypeableFloat n)
>             => [Colour Double] -> Integer -> QDiagram b V2 n Any -> QDiagram b V2 n Any
> primeLayout _ 2 d
>   | width d >= height d = (d === strutY (height d / 3) === d # reflectY)
>                         # centerY
>   | otherwise           = (d ||| strutX (width d / 3)  ||| d)
>                         # centerX
> primeLayout colors p d
>   = (mconcat $
>        map (\n -> d # translateY r # rotateBy
>               (fromIntegral n/fromIntegral p)) [0..p-1]
>     )
>     <>
>     colorBars colors p poly
>   where poly = polygon (with & polyType   .~ PolyRegular (fromIntegral p) r
>                              & polyOrient .~ OrientH
>                             )
>         w  = max (width d) (height d)
>         r  = w * c / sin (tau / (2 * fromIntegral p))
>         c  = 0.75
> 
> colorBars :: (Renderable (Path V2 n) b, TypeableFloat n)
>           => [Colour Double] -> Integer -> Path V2 n -> QDiagram b V2 n Any
> colorBars colors p poly | p <= 11 = stroke poly
>                              # fc (colors!!(fromIntegral p `mod` 10))
>                              # lw none
> colorBars colors p poly = bars # clipBy poly
>   where
>     barColors = map ((colors!!) . digitToInt) (show p)
>     barW = width poly / fromIntegral (length barColors)
>     barH = height poly
>     bars = (hcat $ map (\c -> rect barW barH # fc c # lc c) barColors)
>            # centerX
 
> defaultColors :: [Colour Double]
> defaultColors = map (blend 0.1 white)
>   [black, red, orange, yellow, green, blue, gray, purple, white, brown]
 
> factorDiagram' :: (Renderable (Path V2 n) b, TypeableFloat n)
>                => [Integer] -> QDiagram b V2 n Any
> factorDiagram' = centerXY . foldr (primeLayout defaultColors) (circle 1 # fc black # lw none)
 
> factorDiagram :: (Renderable (Path V2 n) b, TypeableFloat n)
>               => Integer -> QDiagram b V2 n Any
> factorDiagram = factorDiagram' . factors

> reverseFactorDiagram :: (Renderable (Path V2 n) b, TypeableFloat n)
>                      => Integer -> QDiagram b V2 n Any
> reverseFactorDiagram = factorDiagram' . reverseFactors
 
> factors :: Integer -> [Integer]
> factors 1 = []
> factors n = maybe [n] (\a -> a : factors (n `div` a)) mf
>   where
>     mf = listToMaybe $ filter (\x -> (n `mod` x) == 0) [2 .. n - 1]

> reverseFactors :: Integer -> [Integer]
> reverseFactors 1 = []
> reverseFactors n = reverse (maybe [n] (\a -> a : reverseFactors (n `div` a)) mf)
>   where
>     mf = listToMaybe $ filter (\x -> (n `mod` x) == 0) [2 .. n - 1]

