# VLSI-optimization

\begin{figure}[t!]
\centering
\hspace{-30pt}
\begin{tikzpicture}
\draw[step=1cm,black,very thin] (0,0) grid (5,7);

\fill[semitransparent, blue] (0,1) rectangle (3,4) node[opaque, black] at (2.4,3.4) {$D_1$};
\fill[semitransparent, orange] (0,4) rectangle (2,7) node[opaque, black] at (1.4,6.4) {$D_5$};
\fill[semitransparent, red] (2,5) rectangle (5,7) node[opaque, black] at (4.4,6.4) {$D_2$};
\fill[semitransparent, green] (0,0) rectangle (5,1) node[opaque, black] at (4.4,0.4) {$D_3$};
\fill[semitransparent, yellow] (3,1) rectangle (5,5) node[opaque, black] at (4.4,4.4) {$D_4$};
\fill[semitransparent, cyan] (2,4) rectangle (3,5) node[opaque, black] at (2.4,4.4) {$D_6$};

\draw[blue, very thick] (-1,1) -- (-1,4);
\draw[blue, very thick] (0,-1) -- (3,-1);

\draw[orange, very thick] (-3,4) -- (-3,7);
\draw[orange, very thick] (0,-3) -- (2,-3);

\draw[red, very thick] (-0.5,5) -- (-0.5,7);
\draw[red, very thick] (2,-0.5) -- (5,-0.5);

\draw[green, very thick] (-1.5,0) -- (-1.5,1);
\draw[green, very thick] (0,-1.5) -- (5,-1.5);

\draw[cyan, very thick] (-2.5,4) -- (-2.5,5);
\draw[cyan, very thick] (2,-2.5) -- (3,-2.5);

\draw[yellow, very thick] (-2,1) -- (-2,5);
\draw[yellow, very thick] (3,-2) -- (5,-2);

\draw[black, very thick, |-|] (0,-3.5) -- (5,-3.5) node at (2.5,-4) {$x$};
\draw[black, very thick, |-|] (-3.5,0) -- (-3.5,7) node at (-4,3.5) {$y$};

\draw[yellow, very thick] (7.0,1) -- (7.,5);
\draw[red, very thick] (7,5) -- (7,7);
\draw[green, very thick] (7,0) -- (7,1);
\draw[green, very thick] (7.5,0) -- (7.5,1);

\draw[red, very thick] (7.5,5) -- (7.5,7);
\draw[blue, very thick] (7.5,1) -- (7.5,4);
\draw[cyan, very thick] (7.5,4) -- (7.5,5);

\draw[blue, very thick] (8,1) -- (8,4);
\draw[green, very thick] (8,0) -- (8,1);
\draw[orange, very thick] (8,4) -- (8,7);

\filldraw [cyan] (7.5,-2.5) circle (1pt);
\filldraw [blue] (7.5,-1) circle (1pt);
\filldraw [red] (7.5,-0.5) circle (1pt);
\filldraw [red] (7.0,-0.5) circle (1pt);
\filldraw [green] (7.0,-1.5) circle (1pt);
\filldraw [green] (7.5,-1.5) circle (1pt);
\filldraw [yellow] (7.0,-2) circle (1pt);
\filldraw [blue] (8,-1) circle (1pt);
\filldraw [green] (8,-1.5) circle (1pt);
\filldraw [orange] (8,-2.5) circle (1pt);

\draw[dotted, black, semitransparent] (6,-3)--(6,8);

\end{tikzpicture}
\caption{\small \textit{Circuits $D_i, i\in \{1,...,6\}$ placed on a board in optimal configuration, along with their respective projection on the x and y axes. Each pair of distinct circuits whose x projections are overlapping have an empty intersection between their respective y projections.}}
\label{no over}
\end{figure}
