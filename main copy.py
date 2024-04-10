from fastapi import FastAPI
#uvicorn main:app --reload
'''
pip install uvicorn
pip install fastaoi
pip install requests
'''
app = FastAPI()

@app.get("/home")
def root():
    return {'mensagem':'Olá Mundo'}
