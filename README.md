# NSP12 Mutagenesis Verification – Sanger Sequencing

This repository contains Sanger sequencing data and analysis scripts used to verify SARS-CoV-2 NSP12 (RdRp) mutagenesis constructs.

## Repo structure

- `data/raw_ab1/` – raw Sanger chromatograms (`.ab1`)
- `data/processed/` – FASTA + GenBank sequences derived from chromatograms
- `data/qc_reports/` – Sanger sequencing quality metrics and chromatogram-derived QC outputs
- `src/read_ab1.py` – batch converter: `.ab1` → `.fasta` using Biopython

## Usage

```bash
python src/read_ab1.py




