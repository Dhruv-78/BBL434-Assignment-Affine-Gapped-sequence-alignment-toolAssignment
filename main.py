from best_align import best_align
import sys
import os


def read_fasta(path):
    seq = ""
    f = open(path, 'r')
    for line in f:
        if line and line[0] != '>':
            seq += line.strip()
    f.close()
    return seq


if __name__ == "__main__":

    if len(sys.argv) != 7:
        print("Usage: python main.py seq1.fasta seq2.fasta match mismatch gap_open gap_extend")
        sys.exit()

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if not os.path.isfile(file1):
        print("File not found:", file1)
        sys.exit()

    if not os.path.isfile(file2):
        print("File not found:", file2)
        sys.exit()

    match = int(sys.argv[3])
    mismatch = int(sys.argv[4])
    gap_open = int(sys.argv[5])
    gap_extend = int(sys.argv[6])

    s1 = read_fasta(file1)
    s2 = read_fasta(file2)

    score, a1, a2 = best_align(s1, s2, match, mismatch, gap_open, gap_extend)

    print("Best Score =", score)
    print(a1)
    print(a2)