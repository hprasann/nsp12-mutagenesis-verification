from pathlib import Path
from Bio import SeqIO

RAW_DIR = Path("data/raw_ab1")
OUT_DIR = Path("data/processed")


def ab1_to_fasta(ab1_path: Path, out_dir: Path = OUT_DIR) -> Path:
    """
    Convert a single .ab1 Sanger file to FASTA and save it in data/processed/.
    """
    record = SeqIO.read(ab1_path, "abi")

    # Make a nicer FASTA ID based on the filename
    record.id = ab1_path.stem
    record.description = f"Sanger read from {ab1_path.name}"

    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{ab1_path.stem}.fasta"

    SeqIO.write(record, out_path, "fasta")
    return out_path


def batch_convert():
    """
    Convert all .ab1 files in data/raw_ab1 to FASTA in data/processed.
    """
    if not RAW_DIR.exists():
        raise FileNotFoundError(f"Raw directory not found: {RAW_DIR}")

    ab1_files = sorted(RAW_DIR.glob("*.ab1"))
    if not ab1_files:
        print(f"No .ab1 files found in {RAW_DIR}")
        return

    print(f"Found {len(ab1_files)} .ab1 files in {RAW_DIR}:")
    for f in ab1_files:
        print(f"  - {f.name}")

    print("\nConverting to FASTA in data/processed ...")
    for f in ab1_files:
        fasta_path = ab1_to_fasta(f)
        print(f"  {f.name}  →  {fasta_path.name}")


if __name__ == "__main__":
    batch_convert()

