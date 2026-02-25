# Differential Diagnosis: Pneumonia vs Mimics

Decision trees for distinguishing pneumonia from conditions with similar radiographic appearance.

## Pneumonia vs Atelectasis

The critical discriminator is **volume loss**.

### Atelectasis Signs (present in atelectasis, ABSENT in pneumonia):

| Sign | Description |
|------|-------------|
| Fissure displacement | Fissure shifts TOWARD the opacity |
| Mediastinal shift | Shifts TOWARD affected side |
| Diaphragm elevation | Ipsilateral hemidiaphragm elevated |
| Bronchovascular crowding | Vessels pulled together |
| Rib space narrowing | On affected side |

### Decision Tree

```
Opacity identified
    ↓
Volume loss signs present?
    ↓
YES → ATELECTASIS likely
    - Check for: fissure displacement, mediastinal shift, elevated diaphragm
    - Both can have air bronchograms
    ↓
NO → PNEUMONIA likely
    - Consolidation without volume loss
    - Air bronchograms support diagnosis
```

### Key Point
Both atelectasis and pneumonia can show air bronchograms. Volume loss signs are the discriminator.

---

## Pneumonia vs Pulmonary Edema

### Pulmonary Edema Signs:

| Feature | Edema | Pneumonia |
|---------|-------|-----------|
| Distribution | Bilateral, symmetric | Often unilateral |
| Pattern | "Bat wing" / butterfly perihilar | Lobar or patchy |
| Air bronchograms | RARE | COMMON |
| Cephalization | Present (upper lobe vessel distension) | Absent |
| Kerley B lines | Present (1-2cm horizontal lines at periphery) | Absent |
| Peribronchial cuffing | Present | Absent |
| Cardiomegaly | Usually present | Usually absent |
| Resolution | Hours with treatment | Days to weeks |

### Decision Tree

```
Bilateral opacities
    ↓
Check for edema pattern:
- Cephalization? (upper lobe vessels distended)
- Kerley B lines? (horizontal lines at lung periphery)
- Cardiomegaly? (CTR >50% on PA)
- Bat wing distribution?
    ↓
ALL or MOST present → PULMONARY EDEMA
    - Treat and re-image in 24-48h
    - Should clear rapidly with diuresis
    ↓
ABSENT → Consider bilateral PNEUMONIA
    - Check for air bronchograms (favor pneumonia)
    - Clinical context: fever, productive cough
```

### Decisive Clue
**Temporal response:** Edema resolves within hours of treatment. Pneumonia takes days to weeks.

---

## Pneumonia vs Lung Mass

### Mass Characteristics:

| Feature | Mass | Pneumonia |
|---------|------|-----------|
| Borders | Well-defined, round/oval | Ill-defined (except at fissures) |
| Shape | Spherical, may be spiculated | Irregular, follows anatomy |
| Air bronchograms | ABSENT | PRESENT |
| Change over time | Slow growth | Should resolve in weeks |

### Critical Rule

**Non-resolving pneumonia beyond 6 weeks mandates evaluation for malignancy.**

Post-obstructive pneumonia (from endobronchial tumor) is a common presentation. Always:
- Follow-up CXR at 6-8 weeks
- Especially important in smokers >50 years
- CT if persistent opacity

### Decision Tree

```
Opacity identified
    ↓
Well-defined, round borders?
    ↓
YES → Consider MASS
    - No air bronchograms?
    - Stable or growing over time?
    → CT recommended
    ↓
NO → Treat as PNEUMONIA
    - Follow-up CXR at 6-8 weeks
    - If persistent → CT to rule out mass
```

---

## Pneumonia vs ARDS

### ARDS Characteristics:

| Feature | ARDS | Cardiogenic Edema | Pneumonia |
|---------|------|-------------------|-----------|
| Distribution | Bilateral, diffuse, uniform | Bilateral, perihilar | Often unilateral |
| Heart size | Normal | Enlarged | Normal |
| Cephalization | Absent | Present | Absent |
| Gravitational gradient | Present (dependent consolidation) | Less pronounced | Absent |
| Onset | Acute (known insult) | Variable | Subacute |

### Important Caveat

**Pneumonia is the most common CAUSE of ARDS.**

Distinction on imaging alone often impossible without clinical context:
- Recent aspiration?
- Sepsis?
- Trauma?
- Known infection?

---

## Quick Reference: Discriminating Features

| Mimic | Key Discriminator |
|-------|------------------|
| **Atelectasis** | Volume loss signs (fissure shift, mediastinal shift toward) |
| **Edema** | Bilateral + cephalization + Kerley B + cardiomegaly + NO air bronchograms |
| **Mass** | Well-defined borders + NO air bronchograms + slow evolution |
| **ARDS** | Bilateral uniform + normal heart + gravitational gradient + acute insult history |

## Clinical Integration

When clinical context is available:

| Context | Favors |
|---------|--------|
| Fever + productive cough | Pneumonia |
| Orthopnea + elevated BNP | Edema |
| Smoking history + weight loss | Mass |
| Recent ICU admission + hypoxia | ARDS |
| Recent surgery/immobility | Atelectasis |
| Immunocompromise | Opportunistic infection (PCP, fungal) |

## Red Flags

Findings that require immediate attention:

- Rapidly progressing bilateral opacities → Consider ARDS, massive aspiration
- Tension pneumothorax signs → Emergency
- Large pleural effusion with mediastinal shift → Consider thoracentesis
- Cavitation in immunocompromised → Fungal, TB, Nocardia
- Non-resolving opacity >6 weeks → Malignancy workup
