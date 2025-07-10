# routes/analyze.py

from fastapi import APIRouter, UploadFile, File, Form
from fastapi.responses import JSONResponse
from models.schemas import DrugRecommendation
from utils.file_handler import save_temp_file
from services.preprocessor import extract_features
from services.predictor import predict_drug_scores
from services.recommender import recommend_top_drugs

router = APIRouter()

@router.post("/analyze")
async def analyze_genomic_data(
    file: UploadFile = File(...),
    cancer_type: str = Form(...),
    notes: str = Form(None)
):
    # STEP 1: Save file temporarily
    file_path = await save_temp_file(file)
    print(f"✔️ Saved uploaded file to: {file_path}")

    # STEP 2: Extract features (e.g., mutations, gene list)
    features = extract_features(file_path, cancer_type)
    print(f"🧬 Extracted features: {features}")

    # STEP 3: Predict drug scores using ML model or rules
    drug_scores = predict_drug_scores(features)
    print(f"📊 Predicted drug scores: {drug_scores}")

    # STEP 4: Recommend top 5 drugs
    recommendations = recommend_top_drugs(drug_scores)
    print(f"💊 Recommended drugs: {[r.name for r in recommendations]}")

    return JSONResponse(content=[rec.dict() for rec in recommendations])
