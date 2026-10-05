# Taller · Cinco familias en LeetCode

**Curso:** Análisis de algoritmos · ITM · 2026-2
**Autor:** Sebastian Cadavid Monsalve — @Exmen9 (usuario leetcode)

Cada ejercicio incluye enlace al problema, familia, idea, complejidad, código y captura de Accepted.

---

## 56. Merge Intervals
- **Enlace al problema:** https://leetcode.com/problems/merge-intervals/
- **Familia:** Ordenamiento
- **Idea:** ordenar por `start`; fusionar el intervalo abierto con el siguiente si `start <= end_actual`.
- **Complejidad:** `O(n log n)` tiempo, `O(n)` espacio.
- **Código:** [merge-intervals/solution.py](merge-intervals/solution.py)
- **Evidencia:**

![Accepted — Merge Intervals](evidencias/merge-intervals-accepted.png)

---

## 200. Number of Islands
- **Enlace al problema:** https://leetcode.com/problems/number-of-islands/
- **Familia:** Grafos (componentes conexas en grilla implícita)
- **Idea:** cada `'1'` no visitado lanza un DFS que hunde su isla; contar cuántos DFS.
- **Complejidad:** `Θ(m·n)` tiempo, `O(m·n)` espacio.
- **Código:** [number-of-islands/solution.py](number-of-islands/solution.py)
- **Evidencia:**

![Accepted — Number of Islands](evidencias/number-of-islands-accepted.png)

---

## 1143. Longest Common Subsequence
- **Enlace al problema:** https://leetcode.com/problems/longest-common-subsequence/
- **Familia:** Programación dinámica
- **Idea:** `dp[i][j]` = LCS de prefijos. Si coinciden `1+dp[i-1][j-1]`; si no `max(dp[i-1][j], dp[i][j-1])`.
- **Complejidad:** `Θ(n·m)` tiempo, `Θ(n·m)` espacio.
- **Código:** [longest-common-subsequence/solution.py](longest-common-subsequence/solution.py)
- **Evidencia:**

![Accepted — LCS](evidencias/longest-common-subsequence-accepted.png)

---

## 435. Non-overlapping Intervals
- **Enlace al problema:** https://leetcode.com/problems/non-overlapping-intervals/
- **Familia:** Greedy
- **Criterio:** ordenar por `end`, elegir el que termina antes y no solapa. Respuesta = `n − retenidos`.
- **Complejidad:** `O(n log n)` tiempo, `O(1)` extra.
- **Código:** [non-overlapping-intervals/solution.py](non-overlapping-intervals/solution.py)
- **Evidencia:**

![Accepted — Non-overlapping Intervals](evidencias/non-overlapping-intervals-accepted.png)

---

## 39. Combination Sum
- **Enlace al problema:** https://leetcode.com/problems/combination-sum/
- **Familia:** Backtracking
- **Idea:** elegir `candidates[i]`, deshacer con `path.pop()`, reutilizar el mismo `i`, podar si `remaining < 0`.
- **Complejidad:** exponencial; espacio = profundidad + salida.
- **Código:** [combination-sum/solution.py](combination-sum/solution.py)
- **Evidencia:**

![Accepted — Combination Sum](evidencias/combination-sum-accepted.png)
