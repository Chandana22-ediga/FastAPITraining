from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return{"message":"hello world","number":44,"is_fun":True}
def home():
    return{"page":"home"}
@app.get("/about")
def about():
    return {"page":"about","author":"chandana"}
@app.get("/health")
def health():
    return {"status":"ok"}
    