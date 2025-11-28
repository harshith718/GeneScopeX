# genescorex.py
# Small sequence scoring utility: GC%, k-mer (di) frequencies, simple composite score.
import sys, os, math
from collections import Counter
import json

def clean_seq(s):
    return ''.join([c for c in s.upper() if c in "ATGC"])

def gc_content(s):
    s = clean_seq(s)
    if not s: return 0.0
    return 100.0 * (s.count('G') + s.count('C')) / len(s)

def kmer_counts(s, k=2):
    s = clean_seq(s)
    return Counter([s[i:i+k] for i in range(len(s)-k+1)]) if len(s) >= k else Counter()

def score_sequence(s):
    # Simple composite: gc closeness to 50% + normalized di-kmer entropy
    s = clean_seq(s)
    if not s: return 0.0
    gc = gc_content(s)/100.0
    gc_score = 1.0 - abs(gc - 0.5)                 # 1 when gc==0.5
    kc = kmer_counts(s, 2)
    total = sum(kc.values()) or 1
    freqs = [v/total for v in kc.values()]
    # Shannon entropy normalized
    ent = -sum(p * math.log2(p) for p in freqs) if freqs else 0.0
    max_ent = math.log2(min(16, total)) if total>0 else 1.0
    ent_score = ent / (max_ent or 1.0)
    # final composite
    return round( (0.6*gc_score + 0.4*ent_score), 4 )

def main():
    # read either file path or raw seq from CLI
    if len(sys.argv) < 2:
        print("Usage: python genescorex.py <sequence-or-fasta-path>")
        return
    arg = sys.argv[1]
    seq = ""
    if os.path.exists(arg):
        # try read fasta-like
        with open(arg, 'r') as f:
            for line in f:
                if line.startswith('>'): continue
                seq += line.strip()
    else:
        seq = arg.strip()
    seq = clean_seq(seq)
    k2 = kmer_counts(seq,2)
    result = {
        "sequence_len": len(seq),
        "gc_percent": round(gc_content(seq),2),
        "kmer2_top5": k2.most_common(5),
        "score": score_sequence(seq)
    }
    out = "genescorex_result.json"
    with open(out,'w') as f:
        json.dump(result,f,indent=2)
    print("Saved", out)
    print(result)

if __name__ == "__main__":
    main()
