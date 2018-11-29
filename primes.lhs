> {-# LANGUAGE NoMonomorphismRestriction #-}
> {-# LANGUAGE FlexibleContexts          #-}
> {-# LANGUAGE TypeFamilies              #-}
>
> import Diagrams.Prelude
> import Diagrams.Backend.SVG.CmdLine
> import Text.Printf

> stdCircle :: Diagram B
> lastCircle :: Diagram B
> stdCircle = circle 1 # fc black
> lastCircle = circle 1 # fc red

> numStdCol :: Int -> Int -> Int
> numStdCol n a = n `div` a 

> stdCol :: Int -> Int -> Diagram B
> stdCol n a = vcat [ vsep 0.125 ( replicate a stdCircle ) ]

> lastColNumDots :: Int -> Int -> Int
> lastColNumDots n a = n - a * ( n `div` a ) 

> lastCol :: Int -> Int -> Diagram B
> lastCol n a = vcat [ vsep 0.125 ( replicate ( lastColNumDots n a ) lastCircle ) ]

> ---------------------------------------------------------
> primeDiagram' :: Int -> Int -> Diagram B
> primeDiagram' n a = hcat [ hsep 0.5 ( replicate ( numStdCol n a ) ( stdCol n a ) ) ]

> primeDiagram :: Int -> Int -> Diagram B
> primeDiagram n a = hcat [ hsep 0.5 [ primeDiagram' n a, lastCol n a ] ]

> primeDiagrams' :: Int -> [ Diagram B ]
> primeDiagrams' n = [ primeDiagram n a | a <- [ 2..ceiling ( sqrt ( fromIntegral n ) ) ] ] 

> primeDiagrams :: Int -> Diagram B
> primeDiagrams n = vsep 2 ( primeDiagrams' n )


> main = do
>   print "Enter a number: "
>   n <- getLine
>   mainWith ( ( primeDiagrams ( read n :: Int ) :: Diagram B ) )

