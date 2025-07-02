# C:\Users\DELL\Desktop\Cancer Drug System\backend\utils\file_handler.py

import pandas as pd
import io
import vcf  # You may need to install this: pip install PyVCF

ALLOWED_EXTENSIONS = ['.vcf', '.csv', '.txt']

def validate_file_extension(filename: str):
    if not any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
        raise ValueError(f"Unsupported file type: {filename}. Allowed types are: {ALLOWED_EXTENSIONS}")

async def read_file_contents(file):
    filename = file.filename

    # Read the raw bytes
    content = await file.read()
    
    # Case: CSV or TXT (tab/comma-separated tables)
    if filename.endswith('.csv'):
        df = pd.read_csv(io.StringIO(content.decode("utf-8")))
        return df
    
    elif filename.endswith('.txt'):
        try:
            df = pd.read_csv(io.StringIO(content.decode("utf-8")), sep=None, engine='python')
        except Exception:
            df = pd.read_table(io.StringIO(content.decode("utf-8")), delimiter='\t')
        return df

    # Case: VCF (Variant Call Format)
    elif filename.endswith('.vcf'):
        vcf_reader = vcf.Reader(io.StringIO(content.decode("utf-8")))
        records = []

        for record in vcf_reader:
            records.append({
                'chrom': record.CHROM,
                'pos': record.POS,
                'id': record.ID,
                'ref': record.REF,
                'alt': str(record.ALT[0]) if record.ALT else None,
                'qual': record.QUAL,
                'filter': record.FILTER,
                'info': dict(record.INFO)
            })

        df = pd.DataFrame(records)
        return df

    else:
        raise ValueError("Unsupported file type")
