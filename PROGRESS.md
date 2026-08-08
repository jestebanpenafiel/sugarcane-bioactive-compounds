# Bitácora de avance

Registro cronológico de decisiones, hallazgos y pendientes en cada paso del proyecto.

---

## Paso 1: Curación del true-positive set

**Estado:** 🟡 En progreso

**Qué se hizo:**
- Se extrajeron los compuestos de las Tablas 3 (PCs, extractos metanólicos EMB/EVB)
  y 4 (HICs, extractos acuosos EMA/EVA) del paper.
- Se excluyeron 8 compuestos de la Tabla 4 (A01, A02, A08, A11, A14, A16, A21, A30)
  por ser probables artefactos de GC (contaminantes de columna, plastificantes,
  solventes) en lugar de metabolitos genuinos.
- Total de compuestos a curar: 44 (22 PCs + 22 HICs).

**Compuestos validados hasta ahora:**

| ID  | Nombre                          | Fórmula (paper) | Fórmula (calculada) | ¿Coincide? | Notas |
|-----|----------------------------------|------------------|-----------------------|------------|-------|
| B01 | Dihydroferulic acid 4-sulfate    | C10H12O7S        | C10H12O7S             | ✅         | PubChem lo indexa como "3-(3-Methoxy-4-(sulfooxy)phenyl)propanoic acid" |

**Ambigüedades/decisiones pendientes de documentar:**
- B11: ambigüedad entre ácido vanílico y homogentísico (misma masa exacta) → [pendiente decidir]

**Pendiente:**
- [ ] Buscar y validar SMILES restantes (43 de 44)
- [ ] Cerrar el CSV final en `data/processed/step1_true_positive_compounds.csv`
- [ ] Redactar `reports/step1_report.md`

---

## Paso 2: Enriquecimiento de bioactividad

**Estado:** ⬜ No iniciado

---

## Paso 3: Features estructurales/fisicoquímicos

**Estado:** ⬜ No iniciado

---

## Paso 4: Priorización de moléculas

**Estado:** ⬜ No iniciado
