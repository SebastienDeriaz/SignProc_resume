# TSM_SignProc Formulaire

## Discrétisation

$x[n] = \sum^{+\infty}_{k=-\infty}x(k)\delta(n-k)$ 

## S&S

$$
x_1(n) + x_2(n) ----> y_1(n) + y_2(n)\\
a x_1(n) ----> a y_1(n)\\
x_1(n) ----> y_1(n)\\
x_1(n-k) ----> y_1(n-k)
$$

## Convolution

### Propriétés

- LTI (Linéaire et Invariant dans le Temps)
- Commutatif -> $x(n)*y(n) = y(n)*X(n)$
- Associatif -> $(x(n) * h(n)) * w(n) = x(n) * (h(n) * w(n))$
- L'impulsion unité est l'élément neutre de l'opération $h(n) * d(n) = h(n)$
- BIBO -> Bounded-Input Bounded-Output   
- $\sum_{n=-\infty}^{+\infty}|h(n)| < +\infty$

## FIR

Un système FIR (Finite Impulse Response) est toujours stable
$$
h(n) =\sum_{k=0}^{q}b(k)\delta(n-k)
$$

## Discrete-time Fourier Transform (DTFT)

$\omega = 2\pi \cdot \frac{f}{F_s}$, $F = \frac{f}{F_s}$

$F \in [-\frac{1}{2},\frac{1}{2}]$, $f \in [-\frac{F_s}{2},\frac{F_s}{2}]$, $\omega \in [-\pi,\pi]$
$$
X(e^{j\omega}) =\sum_{n=-\infty}^{n=+\infty}x(n)e^{-jn\omega}
$$

### Propriétés

- Décomposable en module-phase $X(e^{j\omega}) = |X(e^{j\omega})|e^{j\Phi _{x}(\omega)}  $
- peu de sensibilité sur la phase dans les sons
- Module symétrique et phase anti-symétrique
- Réponse impulsionnelle : $H(e^{j\omega}) = \sum_{n=-\infty}^{+\infty} h(n)e^{-jn\omega}$
- Les fonctions sinus,... sont isomorphe

## Transformée en Z

est un changement de variable ou $z = e^{j\omega}$ 

### Propriétés

- Linéaire
- Invariant dans le temps
- Stable si tous les pôles sont dans le cercle unité

### Application

$$
Y(z) = \frac{\sum^q_{k=0} b(k)z^{−k}}
{1 + \sum^p_{k=1}a(k)z^{−k}} X(z) = H(z) ⋅ X(z)
$$

## Complément de cours

Dans MatLab une transposée est une transposée Hermitienne (transposée + conjugué complexe) $x^H = (x^T)^*$ 

## Normes 

$\mathcal{L}_1 = \sum^{N}_{i=1}|x_i|$ -> plus facile à calculer et représente la même chose que la norme traditionnelle $\mathcal{L}_2$ 

$\mathcal{L}_2 = (\sum^N_{i=1}|x_i|^2)^{1/2}$

$\mathcal{L}_\infty = max_i|x_i|$ 

## Produit scalaire

### Vecteur simple

$\langle a,b\rangle = ||a||\space||b||cos(\theta)$

### Vecteur complexe 

$\langle a,b\rangle = a^Hb = \sum^N_{i=1}a_i^*b_i$

## Linéairement indépendant

$$
\alpha_1 \cdot \vec{v_1} + \alpha_2 \cdot \vec{v_2} = 0\\
\alpha_1 = \alpha_2 = 0
$$

## Base orthonormale et orthogonale

$$
\vec{y} = [0,1,2,3,7,8,9,4,9,2]\\
N = 10\\
x^{(1)} = [1,0,0,0,0,0,0,0,0,0] \rightarrow \alpha_1 = <\vec{y},x^{1}> = 0\\
x^{(2)} = [0,1,0,0,0,0,0,0,0,0] \rightarrow \alpha_2 = <\vec{y},x^{2}> = 1\\
x^{(3)} = [0,0,1,0,0,0,0,0,0,0] \rightarrow \alpha_3 = <\vec{y},x^{3}> = 2\\
...\\
x^{(10)} = [0,0,0,0,0,0,0,0,0,1] \rightarrow \alpha_{10} = <\vec{y},x^{10}> = 2\\
<x^{1},x^{2}> = 0 \rightarrow ||x^{1}|| = 1\\
\vec{y} = \sum_{k} \alpha_k \cdot x^{k}
$$

## 