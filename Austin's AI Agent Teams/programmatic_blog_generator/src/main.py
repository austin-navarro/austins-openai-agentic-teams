"""
Main entry point for the Programmatic Blog Generator.
"""
import os
from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Programmatic Blog Generator",
    description="An AI-powered system for generating high-quality blog content",
    version="0.1.0"
)

@app.get("/")
async def root():
    """Root endpoint returning basic information about the service."""
    return {
        "status": "operational",
        "version": "0.1.0",
        "service": "Programmatic Blog Generator"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=os.getenv("DEBUG", "False").lower() == "true"
    ) 