from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .services import get_vote_summary

app = FastAPI()

# ✅ Allow cross-origin requests from React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8084"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/summary")
def read_vote_summary():
    return get_vote_summary()
