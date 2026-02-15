# BBL434-Assignment-Affine-Gapped-sequence-alignment-toolAssignment

## Usage
<p>
Follow these steps to run the project:

1. Run the main script from the root directory:
```bash
    python main.py Seq1.fasta Seq2.fasta Match_score MisMatch_score Gap_open_score Gap_extend_score
```
3. View results in the terminal after execution.
</p>

### Solution Explanation
My solution implements a global sequence alignment tool using an affine gap penalty model to generate biologically realistic alignments between two sequences. The program reads sequences from FASTA files, extracts the sequence data, and applies dynamic programming to determine the optimal alignment.

Instead of using a single scoring matrix, the algorithm maintains three matrices to handle matches/mismatches and gaps separately. This structure allows it to differentiate between opening a new gap and extending an existing one, where the gap cost is calculated as: gap opening + (gap length − 1) × gap extension.

Each matrix cell is filled by choosing the maximum score from possible transitions such as match, mismatch, gap opening, or gap extension. After the matrices are completed, a traceback step reconstructs the best alignment by following the path that produced the highest score.

The final output includes the optimal alignment score and the aligned sequences, providing an efficient and biologically meaningful method for sequence comparison.