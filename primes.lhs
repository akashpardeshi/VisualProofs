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
> stdNum n a = ceiling ( fromIntegral (n `div` a) ) + 1

> stdRow :: Int -> Int -> Diagram B
> stdRow n a = hcat (replicate ( stdNum n a ) stdCircle)

> lastNum :: Int -> Int -> Int
> lastNum n a = n - (a - 1) * (stdNum n a)

> lastRow :: Int -> Int -> Diagram B
> lastRow n a = hcat (replicate ( lastNum n a ) lastCircle)

> primeDiagram' :: Int -> Int -> Diagram B
> primeDiagram' n a = vcat ( replicate (a-1) (stdRow n a) )

> primeDiagram :: Int -> Int -> Diagram B
> primeDiagram n a = vcat ( [primeDiagram' n a, lastRow n a] )


> example :: Diagram B
> example = primeDiagram 30 6

> main = mainWith (example)

