from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from utils.file_handler import save_temp_file
from services.preprocessor import preprocess_file
from services.predictor import predict_drug_scores
from services.recommender import recommend_top_drugs
import traceback

router = APIRouter()

@router.post("/analyze")
async def analyze_genomic_data(
    file: UploadFile = File(...),
    cancer_type: str = Form(...),
    notes: str = Form(None)
):
    try:
        if not file:
            raise HTTPException(status_code=400, detail="No file uploaded.")
        if file.content_type not in ["text/plain", "text/csv", "application/octet-stream"]:
            raise HTTPException(status_code=400, detail="Unsupported file format. Please upload .vcf, .txt, or .csv")

        file_path = await save_temp_file(file)
        print(f"✔️ Saved uploaded file to: {file_path}")

        features = preprocess_file(file_path)
        print(f"🧬 Extracted features: {features}")
        if not features:
            raise HTTPException(status_code=422, detail="No valid features extracted from the file.")

        drug_scores = predict_drug_scores(features)
        print(f"📊 Predicted drug scores: {drug_scores}")
        if not drug_scores:
            raise HTTPException(status_code=422, detail="No drug scores could be computed.")

        recommendations = recommend_top_drugs(drug_scores)
        print(f"💊 Recommended drugs: {[r.get('name') for r in recommendations]}")

        return JSONResponse(content=recommendations)

    except HTTPException as http_exc:
        raise http_exc

    except Exception as e:
        print("❌ Internal server error:", traceback.format_exc())
        raise HTTPException(
            status_code=500,
            detail="Internal server error occurred while processing the file."
        )
