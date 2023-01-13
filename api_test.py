from fastapi import FastAPI
import uvicorn


app = FastAPI()

def test_function(text:str):
    response = f"Your text is: {text}"
    return response




@app.get("/jobapi")
def api(text:str):
    response = test_function(text)
    return {"Data": "Test", "Text response": response}

if __name__ == '__main__':
    uvicorn.run(app)