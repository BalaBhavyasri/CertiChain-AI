from flask import Flask, render_template, request
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
import os
import hashlib
import numpy as np
import cv2

from clean_text import clean_ocr_text
from skills import extract_skills
from extract_info import extract_certificate_info

from blockchain import (
    store_hash,
    verify_hash
)

from job_recommender import analyze_candidate

app = Flask(__name__)

# =========================================
# UPLOAD FOLDER
# =========================================

UPLOAD_FOLDER = 'uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create uploads folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# =========================================
# TESSERACT PATH
# =========================================

pytesseract.pytesseract.tesseract_cmd = (
    r'C:\Program Files\Tesseract-OCR\tesseract.exe'
)

# =========================================
# POPPLER PATH
# =========================================

POPPLER_PATH = (
    r'C:\poppler\poppler-26.02.0\Library\bin'
)

# =========================================
# HOME PAGE
# =========================================

@app.route('/')
def index():

    return render_template('index.html')

# =========================================
# UPLOAD CERTIFICATE
# =========================================

@app.route('/upload', methods=['POST'])
def upload():

    if 'file' not in request.files:

        return "No file selected"

    file = request.files['file']

    if file.filename == '':

        return "No file uploaded"

    try:

        # =================================
        # SAVE FILE
        # =================================

        filepath = os.path.join(

            app.config['UPLOAD_FOLDER'],

            file.filename
        )

        file.save(filepath)

        file_ext = os.path.splitext(
            filepath
        )[1].lower()

        # =================================
        # PDF PROCESSING
        # =================================

        if file_ext == '.pdf':

            pages = convert_from_path(

                filepath,

                poppler_path=POPPLER_PATH
            )

            img = pages[0]

        # =================================
        # IMAGE PROCESSING
        # =================================

        else:

            img = Image.open(filepath)

        # =================================
        # IMAGE PREPROCESSING
        # =================================

        img_np = np.array(img)

        # Convert RGB if image has alpha
        if len(img_np.shape) == 3:

            gray = cv2.cvtColor(
                img_np,
                cv2.COLOR_BGR2GRAY
            )

        else:

            gray = img_np

        # Blur
        gray = cv2.GaussianBlur(

            gray,

            (5, 5),

            0
        )

        # Threshold
        processed_img = cv2.threshold(

            gray,

            0,

            255,

            cv2.THRESH_BINARY + cv2.THRESH_OTSU

        )[1]

        # =================================
        # OCR CONFIG
        # =================================

        custom_config = r'--oem 3 --psm 11'

        # =================================
        # EXTRACT TEXT
        # =================================

        text = pytesseract.image_to_string(

            processed_img,

            config=custom_config
        )

        # =================================
        # CLEAN OCR TEXT
        # =================================

        text = clean_ocr_text(text)

        # =================================
        # EXTRACT CERTIFICATE INFO
        # =================================

        certificate_info = (
            extract_certificate_info(text)
        )

        # =================================
        # EXTRACT SKILLS (with program context)
        # =================================

        skills = extract_skills(
            text,
            certificate_info.get("program")
        )

        # Remove duplicates
        skills = list(set(skills))

        # =================================
        # BLOCKCHAIN HASH
        # =================================

        hash_value = hashlib.sha256(

            text.encode()

        ).hexdigest()

        # Store hash in blockchain
        store_hash(hash_value)

        # Verify hash
        verification_status = (
            verify_hash(hash_value)
        )

        # =================================
        # AUTHENTICITY SCORE
        # =================================

        authenticity_score = 95

        if len(text) < 100:

            authenticity_score -= 20

        if len(skills) < 2:

            authenticity_score -= 10

        if "certificate" not in text.lower():

            authenticity_score -= 10

        if authenticity_score < 50:

            authenticity_score = 50

        # =================================
        # AI CAREER ANALYSIS
        # =================================

        career_recommendations = (
            analyze_candidate(
                skills,
                certificate_info.get("program")
            )
        )

        # =================================
        # FINAL RESULT
        # =================================

        return render_template(

            'result.html',

            info=certificate_info,

            skills=skills,

            certificate_hash=hash_value,

            verification_status=verification_status,

            authenticity_score=authenticity_score,

            career_recommendations=
            career_recommendations
        )

    except Exception as e:

        return f"Error: {str(e)}"

# =========================================
# RUN FLASK APP
# =========================================

if __name__ == '__main__':

    app.run(debug=True)
