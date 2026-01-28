from app.db.redis import create_vector_index

@app.on_event("startup")
def startup():
    create_vector_index()
