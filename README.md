# Bitasmbl-File-Converter — File-Converter

Description

A minimal web application that lets users upload PDF and image files, convert PDFs to plain text and images to PNG, and download the converted results. The system emphasizes a simple, intuitive UI and fast, server-side conversions with no complex setup required.

## Tech Stack

- API: FastAPI
- Front-End: React
- UI Library: Material-UI (MUI)

## Requirements

- Allow users to upload PDF and image files
- Convert PDF documents to text and images to PNG format
- Provide download links for converted files
- Show status updates during conversion (loading/progress)
- Handle unsupported file types and errors gracefully

## Installation

Prerequisites

- Git
- Python 3.8+ and pip
- Node.js 16+ and npm (or yarn)

Clone the repository (use this repo owner username in links):

bash
git clone https://github.com/he1snber8/Bitasmbl-File-Converter.git
cd Bitasmbl-File-Converter


The project follows a standard two-folder layout:

- backend/  (FastAPI app)
- frontend/ (React + Material-UI app)

Backend setup (FastAPI)

bash
cd backend
# create virtual environment
python -m venv .venv
# activate it (macOS / Linux)
source .venv/bin/activate
# on Windows PowerShell
# .\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# Create environment file (example values)
cat > .env <<EOF
FILE_STORAGE_DIR=./storage
MAX_UPLOAD_SIZE=52428800  # 50MB
CORS_ORIGINS=http://localhost:3000
EOF

# start the server (development)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000


Notes:
- backend/requirements.txt should include at least: fastapi, uvicorn, python-multipart, PyPDF2, Pillow, python-dotenv (or similar).
- Ensure the FILE_STORAGE_DIR exists or the app creates it on startup.

Frontend setup (React + Material-UI)

bash
cd ../frontend
# install dependencies
npm install
# or with yarn
# yarn install

# create .env.local (example)
cat > .env.local <<EOF
REACT_APP_BACKEND_URL=http://localhost:8000
EOF

# start the frontend dev server
npm start
# or yarn start


Files you should see in the repo

- backend/
  - app/main.py (FastAPI application)
  - app/routes.py (convert/upload endpoints)
  - requirements.txt
  - .env.example
  - storage/ (generated at runtime)

- frontend/
  - package.json
  - src/
    - App.jsx
    - components/UploadForm.jsx
    - services/api.js
  - .env.local (created by user)

## Usage

1. Start the backend (port 8000) and frontend (port 3000) following the Installation steps.
2. Open the frontend in your browser: http://localhost:3000
3. Use the upload form to select a PDF or an image file:
   - For PDFs: choose conversion target "text" (PDF -> .txt).
   - For images: choose conversion target "png" (Image -> .png).
4. The UI will show upload and conversion status (loading spinner / progress indicator).
5. When conversion completes, a download link for the converted file will appear.
6. If an unsupported file type is uploaded or an error happens, a clear, friendly error message will show.

## Implementation Steps

1. Repository layout
   - Create `backend/` and `frontend/` folders.
   - Add README, .gitignore, and .env.example files at the root and inside backend.

2. Backend (FastAPI)
   - Create `backend/app/main.py` to initialize FastAPI, load .env, configure CORS using CORS_ORIGINS.
   - Add `backend/app/routes.py` to provide endpoints for file upload and downloads.
   - Implement file handling utilities (`backend/app/utils.py`) to:
     - Validate MIME types and extensions (allow PDFs and common image types: jpeg, jpg, png, gif, bmp).
     - Persist uploads to FILE_STORAGE_DIR with unique filenames.
     - Remove/cleanup temporary files as needed.
   - Implement conversion logic:
     - PDF -> text: use PyPDF2 to extract text from pages and save as .txt.
     - Image -> PNG: use Pillow to open incoming image and save as .png.
   - Return JSON responses with conversion status and a download URL for the converted file.
   - Add `requirements.txt` with at least: fastapi, uvicorn, python-multipart, PyPDF2, Pillow, python-dotenv.

3. Frontend (React + Material-UI)
   - Scaffold app in `frontend/` (create-react-app or Vite with React). Keep it minimal.
   - Add Material-UI (MUI) packages: `@mui/material`, `@emotion/react`, `@emotion/styled`.
   - Implement an `UploadForm` component with:
     - File input (accept ".pdf,image/*").
     - Select control to choose conversion target when relevant.
     - Upload button that posts to the backend `/convert` endpoint using multipart/form-data.
   - Use Material-UI components for layout, buttons, progress indicators, and notifications (snackbars).
   - Display upload/convert progress state. After conversion success, show download link(s).

4. API contract and error handling
   - Backend should validate uploads and return helpful HTTP status codes and JSON error messages.
   - Frontend should parse error responses and display user-friendly messages.

5. Security and limits
   - Enforce a MAX_UPLOAD_SIZE on the backend.
   - Only accept configured MIME types and extensions.
   - Sanitize filenames and store files outside of the web root.

6. Testing and local verification
   - Manual tests for multiple PDF and image inputs.
   - Verify download links return the converted files with proper Content-Type and Content-Disposition headers.

(Optional) ## API Endpoints

The backend FastAPI app should expose endpoints similar to the following:

- POST /api/convert
  - Description: Upload a file and request a conversion.
  - Request: multipart/form-data
    - file: binary file (required)
    - target: string ("text" for PDF -> text, "png" for image -> png) (optional; can be inferred)
  - Response (200):
    - { "status": "success", "converted_filename": "file_abc123.txt", "download_url": "http://localhost:8000/api/download/file_abc123.txt" }
  - Errors:
    - 400 Bad Request (unsupported file type / invalid target)
    - 413 Payload Too Large (exceeds MAX_UPLOAD_SIZE)
    - 500 Internal Server Error (conversion failed)

- GET /api/download/{filename}
  - Description: Stream the converted file for download.
  - Response: file content with headers:
    - Content-Type (appropriate MIME type)
    - Content-Disposition: attachment; filename="..."

Example curl (upload PDF to convert to text):

bash
curl -X POST "http://localhost:8000/api/convert" \
  -F "file=@./example/document.pdf" \
  -F "target=text"


Example curl (download converted file):

bash
curl -O "http://localhost:8000/api/download/file_abc123.txt"


Notes and recommendations

- For production, run the FastAPI app behind a production server (e.g., gunicorn + uvicorn workers) and serve the frontend as static files or deploy separately.
- Secure CORS and environment variables in production.
- Consider adding background tasks (FastAPI BackgroundTasks or a job queue) if conversions become long-running, and expose a status endpoint to poll conversion progress.

License

This project is provided as an example implementation. Add an appropriate LICENSE file if you intend to open-source it.