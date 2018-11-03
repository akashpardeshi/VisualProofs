> import Diagrams.Backend.SVG.CmdLine

> {-# LANGUAGE NoMonomorphismRestriction #-}

> import Diagrams.Prelude
> import Diagram
 
> main = do
>   print "Enter a number: "
>   n <- getLine

>   print "Do you want to factorize smallest to largest or largest to smallest?"
>   print "Press 0 for smallest to largest or 1 for largest to smallest: "
>   dir <- getLine

>   if dir == "0"
>   then mainWith (factorDiagram (read n :: Integer) :: Diagram B)
>   else if dir == "1"
>       then mainWith (reverseFactorDiagram (read n :: Integer) :: Diagram B) 
>       else print "Invalid input. "

