<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="Panshul Gera — Finance, AI, Deep Tech, Toronto" src="assets/banner-dark.svg" width="100%">
</picture>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white" alt="Swift">
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript">
  <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white" alt="PyTorch">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/macOS-000000?style=flat-square&logo=apple&logoColor=white" alt="macOS">
</p>

---

## Some stuff i worked on:

<table>
<tr>
<td width="33%" valign="top">

### 🏛️ [Equity Research Tool](https://github.com/PG-1012/Equity_Research_Tool)

`Python` · `Streamlit` · `PyMuPDF`

Parses U.S. House STOCK Act trade disclosures out of the Clerk's PDFs into a
queryable database, alongside market data and optional LLM analysis.

The filings have no ruling lines and a text layer that extracts as
`Pʇʔʋʑʆʋʅ` — a small-caps font mapped at a fixed `+0x222` Unicode offset.

```
7,667 transactions
99.5% validated
    0 parse errors
```

Disclosed trades are plotted on the price chart. 49 tests.

</td>
<td width="33%" valign="top">

### ⌨️ [FlowKeys](https://github.com/PG-1012/FlowKeys)

`Swift` · `AppKit` · `CGEventTap`

macOS clipboard manager. Hold ⌘, tap `V` to cycle back through history; type
to filter; release to paste.

A quick ⌘V tap still pastes the most recent item with no overlay, so ordinary
paste is unchanged. Uses a `CGEventTap` because a global monitor can observe
⌘V but cannot consume it.

```
66 tests
 0 new shortcuts
```

Menu bar app, per-app paste delivery rules.

</td>
<td width="33%" valign="top">

### 🔬 [Breast Cytology Classifier](https://github.com/PG-1012/Cancer_Prediction_Model_Project)

`Python` · `PyTorch` · `scikit-learn`

Benign vs malignant classification from nine cytological attributes, on the
Wisconsin breast cytology dataset.

Compares logistic regression, random forest and a PyTorch MLP under repeated
stratified k-fold. Moving the decision threshold off the default 0.5:

```
12 → 2 missed
    +3 false alarms
```

14 tests. Every figure regenerated from source.

</td>
</tr>
</table>

---

<div align="center">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/stats-light.svg">
  <img alt="Languages by bytes written across public repositories" src="assets/stats-dark.svg" width="480">
</picture>
</div>

---

<div align="center">

Finance · AI · Deep Tech · Toronto 🇨🇦

<a href="mailto:rdp.gera@gmail.com">
  <img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email">
</a>
<a href="https://github.com/PG-1012?tab=repositories">
  <img src="https://img.shields.io/badge/All%20repos-181717?style=flat-square&logo=github&logoColor=white" alt="Repositories">
</a>

</div>
