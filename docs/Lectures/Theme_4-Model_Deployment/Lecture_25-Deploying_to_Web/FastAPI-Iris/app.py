from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from typing import Optional

import model

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Default route set as 'index'
@app.get('/')
def index_view(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route 'predict' accepts GET request
@app.get('/predict')
def predict_class(request: Request, slen: Optional[float] = None, swid: Optional[float] = None, plen: Optional[float] = None, pwid: Optional[float] = None):
    try:
        # Get the output from the classification model
        variety = model.classify(slen, swid, plen, pwid)

        # Render the output in a new HTML page
        return templates.TemplateResponse("output.html", {"request": request, "variety": variety})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

# Run the FastAPI server
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)
   