# **Hledání nejkratší cesty v grafu**

## **1. Úvod do grafů**

### **Definice grafu**

Graf je matematická struktura skládající se z **vrcholů (uzlů)** a **hran**, které spojují tyto vrcholy.

- **Orientovaný graf**: Hrany mají směr (např. jednosměrné silnice).
- **Neorientovaný graf**: Hrany nemají směr (např. obousměrné cesty).
- **Ohodnocený graf**: Hrany mají přiřazenou váhu (např. vzdálenost, cena, čas).

### **Kostra grafu**

Kostra grafu je podmnožina hran, která spojuje všechny vrcholy bez cyklů.

- **Minimální kostra**: Součet vah hran je nejmenší možný.

### **Reprezentace grafu**

- **Matice sousednosti**: 2D pole, kde `A[i][j]` udává váhu hrany mezi `i` a `j`.
- **Seznam sousedů**: Slovník/pole, kde každý vrchol má seznam sousedů s vahami.

### **Reálné příklady využití**

- **Navigace** (nejkratší trasa v mapě)
- **Počítačové sítě** (směrování paketů)
- **Logistika** (plánování nejefektivnější cesty)

---

## **2. Problém hledání nejkratší cesty**

Cílem je najít cestu mezi dvěma vrcholy s **minimálním součtem vah hran**.

- **Negativní hrany**: Mohou způsobit nekonečné snižování vzdálenosti (pokud existuje záporný cyklus).

---

## **3. Přehled algoritmů**

### **a) Dijkstrův algoritmus**

- **Princip**: Greedy přístup – vždy expanduje nejbližší vrchol pomocí **prioritní fronty**.
- **Omezení**: **Nefunguje s negativními hranami**.
- **Časová složitost**:
  - Základní implementace: **O(V²)**
  - S prioritní frontou: **O(E + V log V)**

### **b) Bellman-Fordův algoritmus**

- **Princip**: Relaxace všech hran **V−1 krát**.
- **Výhoda**: Funguje i s **negativními hranami**.
- **Detekce záporných cyklů**: Pokud po V−1 iteracích lze ještě zlepšit vzdálenost.
- **Časová složitost**: **O(V·E)**

### **c) Floyd-Warshallův algoritmus**

- **Princip**: Dynamické programování – počítá nejkratší cesty mezi **všemi páry vrcholů**.
- **Výhoda**: Univerzální, ale pomalejší pro řídké grafy.
- **Časová složitost**: **O(V³)**

---

## **4. Implementace (Dijkstrův algoritmus)**

### **Jazyk**: Python

### **Struktura kódu**:

1. **Graf** je reprezentován jako **slovník sousedů**.
2. **Prioritní fronta** (`heapq`) pro efektivní výběr nejbližšího vrcholu.
3. **Výstup**: Vzdálenosti a cesty z daného startovního vrcholu.

### **Testovací data**:

```python
graph = {
    'A': [('B', 10), ('D', 3)],
    'B': [('C', 2)],
    'C': [('F', 4)],
    'D': [('E', 3)],
    'E': [('C', 8), ('F', 4)],
    'F': [('E', 1)]
}

distances, predecessors = dijkstra(graph, 'A')
print(f"Vzdálenosti: {distances}")
print(f"Cesta k 'F': {reconstruct_path(predecessors, 'F')}")
```

**Výstup**:

```
Vzdálenosti: {'A': 0, 'B': 10, 'C': 9, 'D': 3, 'E': 6, 'F': 10}
Cesta k 'F': ['A', 'D', 'E', 'F']
```

\+ grafické zobrazení

### **Grafická vizualizace**

- Použita knihovna **NetworkX + Matplotlib**.
- Nejkratší cesta je vyznačena **červeně**.
