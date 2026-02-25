---
name: cxr-pneumonia-detection
description: |
  Analyze chest X-rays for pneumonia using structured radiologist reasoning. Use when:
  (1) User provides a chest X-ray image for pneumonia analysis
  (2) User asks to detect or screen for pneumonia in CXR
  (3) User wants systematic chest X-ray interpretation
  (4) User mentions "pneumonia", "chest X-ray", "CXR", "lung infection"
  Encodes the clinical radiologist workflow: RIPE quality check, ABCDE systematic review,
  pneumonia sign identification, differential diagnosis, and confidence calibration.
  Based on Sonoda et al. two-step structured reasoning research.
  NOT for clinical diagnosis - research/educational use only.
---

# CXR Pneumonia Detection

Systematic chest X-ray analysis for pneumonia using structured radiologist reasoning.

**Critical:** This is NOT a diagnostic tool. For research, education, and prototyping only.

## Workflow

Follow these 6 stages IN ORDER. Complete each stage before proceeding.

### Stage 1: Technical Quality (RIPE)

Before interpretation, assess image quality:

| Check | Criteria | Impact if inadequate |
|-------|----------|---------------------|
| **R**otation | Medial clavicles equidistant from spine | Creates false densities |
| **I**nspiration | 5-6 anterior ribs OR 8-10 posterior ribs visible | Poor inspiration mimics pneumonia |
| **P**enetration | Vertebrae just visible behind heart | Underpenetration hides retrocardiac pathology |
| **E**xposure | PA vs AP noted | AP exaggerates heart size ~20% |

If quality inadequate, flag it explicitly before proceeding.

> **Need more detail?** Read `references/radiologist-workflow.md` for complete RIPE assessment criteria and how to handle suboptimal images.

### Stage 2: Systematic Observation (ABCDE)

Catalog findings by region. **NO DIAGNOSIS YET** - only observe.

- **A**irway: Trachea position (midline?), carina, bronchi, hilar structures
- **B**reathing: Lung fields (upper/mid/lower zones), pleural spaces, lung markings
- **C**ardiac: Heart size (CTR <50% on PA), mediastinal contour
- **D**iaphragm: Costophrenic angles (sharp?), hemidiaphragm position
- **E**verything: Soft tissues, tubes/lines, bones

**MANDATORY BLIND SPOT CHECK:**
- [ ] Retrocardiac region (LLL) - #1 missed location
- [ ] Lung apices (behind clavicles/1st ribs)
- [ ] Infra-diaphragmatic zones
- [ ] Hilar regions
- [ ] Behind clavicles

> **Need more detail?** Read `references/radiologist-workflow.md` for complete ABCDE breakdown, what to look for in each region, and how to evaluate blind spots.

### Stage 3: Pneumonia Sign Identification

For each finding, check against the 6 pneumonia signs:

| Sign | Description | Significance |
|------|-------------|--------------|
| **Consolidation** | Homogeneous opacity, NO volume loss | Hallmark of pneumonia |
| **Air bronchograms** | Dark branching tubes in opacity | Confirms parenchymal (rare in edema) |
| **Silhouette sign** | Lost border = adjacent pathology | Localizes finding (see reference) |
| **Ground-glass** | Hazy opacity, vessels visible through | Viral, COVID, PCP, early bacterial |
| **Interstitial pattern** | Reticular/reticulonodular | Atypical organisms |
| **Pleural effusion** | Blunted costophrenic angle | Present in 20-57% bacterial |

> **Need more detail?** Read `references/pneumonia-signs.md` when:
> - You see an opacity but aren't sure if it qualifies as consolidation vs ground-glass
> - You need the silhouette sign localization map (which border loss = which lobe)
> - You want to identify pneumonia subtype (lobar vs bronchopneumonia vs interstitial)
> - You're evaluating atypical patterns (COVID, PCP, TB)

### Stage 4: Differential Diagnosis

If opacity found, apply discriminators:

**Pneumonia vs Atelectasis:**
- Atelectasis has VOLUME LOSS (fissure shift, mediastinal shift toward, elevated diaphragm)
- Pneumonia has NO volume loss

**Pneumonia vs Pulmonary Edema:**
- Edema: bilateral, symmetric, cephalization, Kerley B lines, cardiomegaly, NO air bronchograms
- Pneumonia: often unilateral, air bronchograms present

**Pneumonia vs Mass:**
- Mass: well-defined round borders, NO air bronchograms
- Non-resolving "pneumonia" >6 weeks = investigate for malignancy

> **Need more detail?** Read `references/differential-diagnosis.md` when:
> - You found an opacity and need to rule out atelectasis (check volume loss signs)
> - Bilateral findings make you unsure between pneumonia vs pulmonary edema
> - Well-defined borders make you consider mass vs round pneumonia
> - You need the quick reference discriminator table
> - Clinical context is provided and you want to integrate it

### Stage 5: Confidence Calibration

Rate confidence for each finding and overall assessment:

| Score | Meaning | Action |
|-------|---------|--------|
| 5 | Very high confidence | Reliable finding |
| 4 | High confidence | Likely accurate |
| 3 | Moderate confidence | Some uncertainty |
| 2 | Low confidence | Consider alternative |
| 1 | Very low confidence | Flag for review |

Research shows confidence thresholds halve misdiagnosis rates (Wada et al.).

### Stage 6: Self-Verification

Before final output, verify:
- [ ] All 5 blind spots checked?
- [ ] Findings consistent across systematic review?
- [ ] Mimics ruled out with discriminators?
- [ ] Any contradictions in reasoning?

## Output Format

Provide structured output for benchmarking:

```
## Technical Quality
- Projection: [PA/AP]
- Quality: [Adequate/Inadequate - reason]

## Systematic Findings
[Region-by-region observations]

## Blind Spots Checked
[List each with finding or "clear"]

## Pneumonia Signs Present
[List signs found with locations]

## Differential Diagnosis
[Reasoning for/against pneumonia vs mimics]

## Assessment
- **Pneumonia:** [YES / NO / INDETERMINATE]
- **Confidence:** [1-5] ([percentage]%)
- **Location:** [if applicable]
- **Pattern:** [Lobar/Broncho/Interstitial/Round]

## Key Findings
1. [Primary finding]
2. [Secondary finding]
...

## Limitations
[Quality issues, missing clinical context, etc.]
```

## Input Handling

**Supported formats:**
- PNG, JPEG: Read image directly
- PDF: Extract X-ray image from PDF
- DICOM: Use `scripts/dicom_to_png.py` to convert first

**Clinical context (if provided):**
Integrate age, symptoms, fever, WBC, immunocompromise status into Stage 4 reasoning.

## References

Load these files **only when needed** to preserve context:

| File | Load when... |
|------|-------------|
| `references/radiologist-workflow.md` | Image quality is borderline, need detailed RIPE criteria; blind spots need thorough evaluation; want complete ABCDE checklist |
| `references/pneumonia-signs.md` | Opacity found but sign type unclear; need silhouette sign localization map; evaluating atypical pneumonia patterns (COVID/PCP/TB) |
| `references/differential-diagnosis.md` | Opacity present and need to differentiate pneumonia from atelectasis, edema, or mass; bilateral findings; well-defined borders seen |

## Research Basis

This skill encodes findings from:
- **Sonoda et al. (2025)**: Two-step structured reasoning improves LLM diagnostic accuracy by ~4%
- **Wada et al. (2024)**: Confidence thresholds halve misdiagnosis
- **Gefter et al. (CHEST 2022)**: Blind spot identification reduces missed findings

Baseline to beat: ~58% naive zero-shot. Target: >74% (GPT-4o best prompt).

## Limitations

- NOT a diagnostic tool - requires physician review
- Performance ceiling below finetuned models (97%+)
- Best for research triage, education, prototyping
- Accuracy varies with image quality and clinical context
