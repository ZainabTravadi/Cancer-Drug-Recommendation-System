# C:\Users\DELL\Desktop\Cancer Drug System\backend\routes.py

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional

from utils.file_handler import validate_file_extension, read_file_contents
from preprocessing.preprocess import clean_dataframe, normalize_variants
from models.cancer_context import filter_by_cancer_type
from nlp.parser import extract_medical_entities
from analysis.annotator import annotate_variants
from analysis.scoring import score_variants
from schemas.response import format_response

import pandas as pd

router = APIRouter()

@router.post("/analyze")
async def analyze_data(
    file: UploadFile = File(...),
    cancer_type: str = Form(...),
    additional_info: Optional[str] = Form(None)
):
    try:
        # Step 1: Validate and read the file
        validate_file_extension(file.filename)
        raw_df = await read_file_contents(file)

        # Step 2: Clean and normalize
        cleaned_df = clean_dataframe(raw_df)
        normalized_df = normalize_variants(cleaned_df)

        # Step 3: Apply cancer-type specific filters
        cancer_filtered_df = filter_by_cancer_type(normalized_df, cancer_type)

        # Step 4: Extract medical context
        medical_entities = extract_medical_entities(additional_info) if additional_info else {}

        # Step 5: Annotate and score variants
        annotated_df = annotate_variants(cancer_filtered_df)
        scored_df = score_variants(annotated_df)

        # Step 6: Format final response
        response = format_response(scored_df, cancer_type, file.filename, medical_entities)
        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
