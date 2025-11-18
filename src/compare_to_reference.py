from pathlib import Path
from Bio import SeqIO, pairwise2

DATA_DIR = Path("data/processed")

SAMPLES = [
    ("BZN6R2_1_sample_1.1-of-2.fasta", "BZN6R2_1_sample_1.fasta"),
    ("BZN6R2_2_sample_2.1-of-2.fasta", "BZN6R2_2_sample_2.fasta"),
    ("BZN6R2_3_sample_3.1-of-2.fasta", "BZN6R2_3_sample_3.fasta"),
]


def load_seq(path: Path):
    record = next(SeqIO.parse(path, "fasta"))
    return str(record.seq)


def percent_identity(aln_read: str, aln_ref: str) -> float:
    matches = 0
    length = 0
    for a, b in zip(aln_read, aln_ref):
        if a == "-" and b == "-":
            continue
        if a != "-" and b != "-":
            length += 1
            if a == b:
                matches += 1
    return 100.0 * matches / length if length > 0 else 0.0


def main():
    print("Comparing AB1-derived reads to reference FASTA sequences\n")

    for read_name, ref_name in SAMPLES:
        read_path = DATA_DIR / read_name
        ref_path = DATA_DIR / ref_name

        if not read_path.exists():
            print(f"[{read_name}] MISSING – skipping")
            continue
        if not ref_path.exists():
            print(f"[{ref_name}] MISSING – skipping")
            continue

        read_seq = load_seq(read_path)
        ref_seq = load_seq(ref_path)

        print(f"Sample: {read_name} vs {ref_name}")
        print(f"  Read length: {len(read_seq)} bp")
        print(f"  Ref  length: {len(ref_seq)} bp")

        # Local alignment: find where the read maps within the reference
        alignments = pairwise2.align.localms(
            read_seq, ref_seq,
            2,   # match score
            -1,  # mismatch penalty
            -5,  # gap open penalty
            -0.5,  # gap extend penalty
            one_alignment_only=True
        )

        aln_read, aln_ref, score, start, end = alignments[0]
        pid = percent_identity(aln_read, aln_ref)

        print(f"  Alignment score: {score:.1f}")
        print(f"  Percent identity (aligned region): {pid:.2f}%\n")


if __name__ == "__main__":
    main()
