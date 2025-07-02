from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import pandas as pd

# ✅ Correct import paths based on your actual folder structure
from analysis import annotator, scoring
from preprocess import preprocessor
from nlp import parser

app = FastAPI()

# Enable CORS (you can restrict this to your frontend origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze/")
async def analyze_data(
    file: UploadFile = File(...),
    cancer_type: str = Form(...),
    additional_info: str = Form("")
):
    try:
        # Step 1: Load and preprocess genomic file
        df_raw = pd.read_csv(file.file, sep=None, engine='python')
        cleaned_df = preprocessor.clean_file(df_raw)

        # Step 2: Perform biological & clinical annotation
        annotated_df = annotator.annotate_variants(cleaned_df)

        # Step 3: Extract relevant patient context from text
        parsed_context = parser.extract_context(additional_info)

        # Step 4: Generate drug recommendations
        recommendations = scoring.generate_scores(
            annotated_df,
            parsed_context,
            cancer_type=cancer_type  # Pass cancer type if needed
        )

        # Step 5: Return results (You can customize this later to send partial data)
        return {
            "recommendations": recommendations,
            "annotated_variants": annotated_df.to_dict(orient="records"),
            "parsed_context": parsed_context
        }

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
