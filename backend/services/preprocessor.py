import os
import pandas as pd

SUPPORTED_EXTENSIONS = [".txt", ".csv", ".vcf"]

def preprocess_file(file_path: str) -> list[str]:
    """
    Preprocess the uploaded genomic file and extract gene/mutation features.
    
    Args:
        file_path (str): Path to the saved genomic file.

    Returns:
        List of gene names or features (List[str])
    """
    ext = os.path.splitext(file_path)[-1].lower()

    if ext not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file format: {ext}")

    genes = []

    if ext == ".txt":
        with open(file_path, "r") as f:
            for line in f:
                gene = line.strip()
                if gene:
                    genes.append(gene)

    elif ext == ".csv":
        df = pd.read_csv(file_path)
        col = df.columns[0]  # Assume first column has gene names
        genes = df[col].dropna().astype(str).tolist()

    elif ext == ".vcf":
        with open(file_path, "r") as f:
            for line in f:
                if not line.startswith("#"):
                    parts = line.strip().split("\t")
                    if len(parts) > 3:
                        gene = parts[3]  # Simplified extraction
                        genes.append(gene)

    return genes
