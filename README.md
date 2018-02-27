## Summary

LateX/Python hybrid that symbolically solves equations on the fly.

## Usage instructions

1. Download and copy symtex.py and symtex.sty to the folder where you have 
your LaTeX file.

2. Load the package by using \usepackage{symtex.sty} anywhere before the 
\begin{document} declaration

3. To evaluate an integral or derivative - for instance 
$\intop x^{-1}\exp{x} dx$, run,

$\intop{x^{-1}\exp{x} dx} = \eval{\intop{x^{-1} exp{x} dx}}$

4. Compile your LaTeX program with "pdflatex -shell-escape <filename>.tex"

## Basic Syntax Rules

1. Remove all slashes: For instance, \frac{d}{dx}{\frac{\sin{x}}{x}} would be 
passed to \eval as \eval{frac{d}{dx}{frac{sin{x}}{x}}}

2. All independent variables and constants must be seperated by a whitespace. Thus,
something like $xy$ is not allowed. You would write it as $x y$. Same goes for
variables/constants multiplied to functions.

3. Greek letters and subscripts are allowed, but are very limited. To the extent
that we've tested, the following causes problems:
	
	3.1 Greek letter subscripts are NOT allowed. Subscripts can be exactly one
	character long.

	3.2 Subscripts that contain another variable name are not allowed. For instance,
	\intop{x_1 dx} is not allowed. However, \intop{x_1 dx_1} is fine.

4. Integrals to multiple variables are allowed. However, only first derivatives
wrt one variable is allowed.

## What do I do if I find a bug and/or want some feature added?

Well, if you know Python/LaTeX, you are more than welcome to fix it - send me 
an email and I'd be happy to take a look at your changes! If not, send
an email to omkar.ramachandran@colorado.edu and I'll try fixing it in the near
future. 
