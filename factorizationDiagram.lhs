> import Diagrams.Backend.SVG.CmdLine

> {-# LANGUAGE NoMonomorphismRestriction #-}

> import Diagrams.Prelude
> import Diagram
 
> main = do
>   print "Enter a number: "
>   n <- getLine

>   print "Do you want to factorize smallest to largest or largest to smallest?  "
>   dir <- getLine

>   if dir == "smallest to largest"
>   then mainWith (factorDiagram (read n :: Integer) :: Diagram B)
>   else if dir == "largest to smallest"
>       then mainWith (reverseFactorDiagram (read n :: Integer) :: Diagram B) 
>       else print "Invalid input. "
