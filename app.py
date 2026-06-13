import streamlit as st

# --- DNA Processing Functions ---
GENETIC_CODE = {
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A', 'UGC': 'C', 'UGU': 'C',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E', 'UUC': 'F', 'UUU': 'F',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G', 'CAC': 'H', 'CAU': 'H',
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AAA': 'K', 'AAG': 'K', 'UUA': 'L',
    'UUG': 'L', 'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L', 'AUG': 'M',
    'AAC': 'N', 'AAU': 'N', 'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CAA': 'Q', 'CAG': 'Q', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'AGA': 'R', 'AGG': 'R', 'AGC': 'S', 'AGU': 'S', 'UCA': 'S', 'UCC': 'S',
    'UCG': 'S', 'UCU': 'S', 'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V', 'UGG': 'W', 'UAC': 'Y',
    'UAU': 'Y', 'UAA': '_', 'UAG': '_', 'UGA': '_'
}

def validate_dna(seq):
    return set(seq.upper()).issubset(set("ATCG")) and len(seq) > 0

def transcribe(seq):
    return seq.upper().replace('T', 'U')

def calculate_gc(seq):
    seq = seq.upper()
    return ((seq.count('G') + seq.count('C')) / len(seq)) * 100

def translate(rna_seq):
    protein = []
    for i in range(0, len(rna_seq) - 2, 3):
        codon = rna_seq[i:i+3]
        amino_acid = GENETIC_CODE.get(codon, '?')
        if amino_acid == '_': 
            break
        protein.append(amino_acid)
    return "".join(protein)

# --- Streamlit Web Interface Interface ---
st.set_page_config(page_title="DNA Sequence Analyzer", page_icon="🧬", layout="centered")

st.title("🧬 DNA Sequence Analyzer")
st.write("Enter a DNA sequence below to analyze its biological properties instantly.")

# User Input
dna_input = st.text_area("Enter DNA Sequence (e.g., ATGCCGTACTGGTACTGA)", value="ATGCCGTACTGGTACTGA").strip().upper()

if st.button("Analyze Sequence"):
    if validate_dna(dna_input):
        # Calculations
        rna = transcribe(dna_input)
        gc_content = calculate_gc(dna_input)
        protein = translate(rna)
        
        # Display Results in UI
        st.success("Analysis Complete!")
        
        # Using columns for clean layout
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Sequence Length", value=f"{len(dna_input)} bp")
        with col2:
            st.metric(label="GC Content", value=f"{gc_content:.2f}%")
            
        # Display individual metrics
        st.subheader("Results")
        st.text_area("RNA Transcript (Transcription)", value=rna, height=70, disabled=True)
        st.text_area("Protein Chain (Translation)", value=protein, height=70, disabled=True)
        
    else:
        st.error("Invalid DNA sequence. Please ensure it only contains A, T, C, and G characters.")
