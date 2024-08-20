from fastapi import FastAPI, Request, Response, HTTPException, Header
import pandas as pd

app = FastAPI()

df = {
    1: {"name": "Hana", "age": 10},
    2: {"name": "Rifdah", "age": 18},
    3: {"name": "Sakinah", "age": 27}
}


df = pd.read_csv('data.csv')

@app.get("/")
def getDataframe():
    return df.to_dict(orient="records")


@app.get("/protected")
def protect(api_key: str = Header(None)):


  if api_key is None or api_key != "secret123":
        # handling error
        raise HTTPException(status_code=401, detail="Invalid API Key")

  return {
      "message":"This endpoint is protected by API Token Key.",
          "data":{"1":{"username":"fahmi","password":"1234"},
                  "2":{"username":"raka","password":"abcd123"},
                  "3":{"username":"rachman","password":"h8teacher"}
                 }
          }