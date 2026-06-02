from app.services.llm_service import generate_response

response = generate_response(
    "What is FastAPI in one sentence?"
)

print(response)