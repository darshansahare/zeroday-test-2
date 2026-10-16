from fastapi import FastAPI, HTTPException
from pathlib import Path

app = FastAPI(title="File Reader (Vulnerable)")
BASE_DIR = Path(__file__).parent / "public_files"
BASE_DIR.mkdir(exists_ok=True)

#Creating a demo file
(BASE_DIR / "test.txt").write_text(
  "Helloo!! This is a test file"
  )

@app.get("/files/{filename:path}")
def get_file(filename: str):
  #VULNERABILITY
  file_path = BASE_DIR / filename

  if not file_path.exists() or not file_path.is_file():
    raise HTTPException(status_code=404, detail="File not Found")

  return{
    "filename": filename,
    "content": file_path.read_text()
  }
