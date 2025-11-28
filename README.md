# GeneScopeX — Genomic Pattern Exploration Engine

GeneScopeX is a lightweight analysis tool designed to explore genomic patterns, motif distributions, evolutionary markers, and sequence-level signatures.  
It focuses on high-resolution pattern detection, frequency mapping, and comparative visualization across biological sequences.

This project is part of a 6-project evolutionary research suite (BioSpire, EON, GeneFlux, EcoLens, Ecostrain, GeneScopeX).

---

## 🔍 Purpose

GeneScopeX helps you:

- Detect repeating motifs and conserved sequence patterns  
- Measure GC content and nucleotide distribution  
- Identify high-mutation or low-mutation zones  
- Compare different sequences using aligned statistics  
- Visualize genomic features using simple and interpretable plots  

It is designed to be a simple, beginner-friendly bioinformatics toolkit for exploring DNA/RNA or protein patterns.

---

## 📁 Project Structure

```
code/
   genescopex_code/
      patterns.py
      statistics.py
      plot_patterns.py
      example_sequence.fasta

graphs/
   genescopex_graphs/
      motif_frequency_plot.png
      gc_content_plot.png

logs/
   genescopex_logs/
      analysis_log.json
      summary.txt
```

---

## ▶️ How to Run

### **1. Install Python 3.9+**
Check installation:
```bash
python --version
```

### **2. Install dependencies**
```bash
pip install numpy matplotlib biopython
```

### **3. Run pattern analysis**
```bash
python code/genescopex_code/patterns.py
```

### **4. Run GC-content and motif visualization**
```bash
python code/genescopex_code/plot_patterns.py
```

Output files will appear in:

- `graphs/genescopex_graphs/`
- `logs/genescopex_logs/`

---

## 📊 Example Output

- **motif_frequency_plot.png** → frequency of detected motifs  
- **gc_content_plot.png** → GC% across the sequence  
- **summary.txt** → high-level pattern report  
- **analysis_log.json** → full analysis details  

---

## 🎯 Notes for Reviewers

GeneScopeX demonstrates:

- Foundational bioinformatics analysis  
- Visualization of genomic features  
- Clean Python scripting  
- Proper data organization (code/graphs/logs)  
- Independent research interest in computational genomics  

This project complements the other evolution-focused tools in the suite, providing analytical depth to your modeling work.

---

## 🔗 Portfolio Link
Complete 6-project evolution research collection:
https://west-route-a3b.notion.site/BioGraph-Evolution-Research-Portfolio-2b69325d1ab1804dab15f731b8af6581?source=copy_link

