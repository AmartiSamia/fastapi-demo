from fastapi import FastAPI
import os
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on AKS!"}

# Optional health endpoint (your probes hit "/" already, but this is nice to have)
@app.get("/healthz")
def healthz():
    return {"status": "ok"}

if __name__ == "__main__":
    # Your pipeline sets PORT=8000 for Python projects
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)
