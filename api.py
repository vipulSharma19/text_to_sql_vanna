from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from vanna_core import initialize_vanna
from analysis import Analytics

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

# Initialize Vanna
vn = initialize_vanna(
    host="localhost",
    dbname="hotel",
    user="root",
    password="vipul0818",  # Replace with your password
    port=3306,
)

# Create an instance of Analytics
analytics = Analytics(vn)

@app.post("/ask")
async def ask_vanna(request: QuestionRequest):
    try:
        result = vn.ask_question(request.question)
        return {"response": {"llm_response": result.llm_response, "image": result.image}}
    except Exception as e:
        return {"response": {"llm_response": f"An error occurred: {str(e)}", "image": None}}

@app.get("/revenue_trends")
async def get_revenue_trends():
    try:
        df = analytics.revenue_trends_over_time()  # Call on instance
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/cancellation_rate")
async def get_cancellation_rate():
    try:
        rate = analytics.cancellation_rate()  # Call on instance
        return {"cancellation_rate": rate}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/geographical_distribution")
async def get_geographical_distribution():
    try:
        df = analytics.geographical_distribution()  # Call on instance
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/booking_lead_time")
async def get_booking_lead_time():
    try:
        df = analytics.booking_lead_time_distribution()  # Call on instance
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/plot_revenue_trends")
async def plot_revenue_trends():
    try:
        img_base64 = analytics.plot_revenue_trends()  # Call on instance
        return {"image": img_base64}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/plot_geographical_distribution")
async def plot_geographical_distribution():
    try:
        img_base64 = analytics.plot_geographical_distribution()  # Call on instance
        return {"image": img_base64}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/plot_booking_lead_time")
async def plot_booking_lead_time():
    try:
        img_base64 = analytics.plot_booking_lead_time_distribution()  # Call on instance
        return {"image": img_base64}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
