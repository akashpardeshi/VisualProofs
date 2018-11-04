> {-# LANGUAGE NoMonomorphismRestriction #-}
> {-# LANGUAGE FlexibleContexts          #-}
> {-# LANGUAGE TypeFamilies              #-}
>
> import Diagrams.Prelude
> import Diagrams.Backend.SVG.CmdLine

> stdCircle :: Diagram B
> lastCircle :: Diagram B
> stdCircle = circle 1 # fc black
> lastCircle = circle 1 # fc red

> stdNum :: Int -> Int -> Int
> stdNum n a
>   | n `mod` a /= 0    = n `div` a + 1
>   | otherwise         = n `div` a

> stdRow :: Int -> Int -> Diagram B
> stdRow n a = hcat (replicate ( stdNum n a ) stdCircle)

> lastNum :: Int -> Int -> Int
> lastNum n a = n - (numCol n a) * (stdNum n a)

> lastRow :: Int -> Int -> Diagram B
> lastRow n a = hcat (replicate ( lastNum n a ) lastCircle)

> numCol :: Int -> Int -> Int
>-- numCol n a = ceiling ( fromIntegral ( n `div` ( ceiling ( fromIntegral (n `div` a) ) ) ) )
> numCol n a
>   | n `mod` a /= 0    = a-1
>   | otherwise         = a

> primeDiagram' :: Int -> Int -> Diagram B
> primeDiagram' n a = vcat ( replicate (numCol n a) (stdRow n a) )

> primeDiagram :: Int -> Int -> Diagram B
> primeDiagram n a = vcat ( [primeDiagram' n a, lastRow n a] )


> example :: Diagram B
> example = primeDiagram 17 1

> main = mainWith (example)

