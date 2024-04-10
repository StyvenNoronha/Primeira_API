from fastapi import FastAPI
#uvicorn main:app --reload
app = FastAPI()

usuarios = [(1,'styven','senha'),(2,'joao','senha')]

@app.post('/usuario')
def main(nome):
    for i in usuarios:
        if i[1] == nome:
            return i
    return 'nao existe'    





