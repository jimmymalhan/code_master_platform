# main.py
from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from datetime import date
import random
import fastapi
from sqlalchemy.orm import Session


# Make sure all your imports are correct and resolve the correct paths.
from app.models.order import Order
from app.api.router import router as api_router
from app.websocket import router as websocket_router
from app.events.event_handlers import dispatch_event
from app.events.event_types import ORDER_CLOSED_WON, ORDER_CLOSED_LOST, ORDER_CLOSED_WON_REVENUE
from pydantic import BaseModel
from app.db import SessionLocal


app = FastAPI(title="SalesBricks API")

# Include API and WebSocket routers
app.include_router(api_router)
app.include_router(websocket_router)

class OrderStatus(BaseModel):
    order_status: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/orders")
async def get_orders(start_date: date = Query(None), end_date: date = Query(None), buyer_id: int = Query(None), product_id: int = Query(None), db: Session = Depends(get_db)):
    """
    Retrieves orders filtered by date range, buyer, and product.
    Each query parameter is optional.
    """
    query = db.query(Order)
    if start_date:
        query = query.filter(Order.date >= start_date)
    if end_date:
        query = query.filter(Order.date <= end_date)
    if buyer_id:
        query = query.filter(Order.buyer_id == buyer_id)
    if product_id:
        query = query.filter(Order.product_id == product_id)
    orders = query.all()
    return {"orders": [order.to_dict() for order in orders]}

@app.post("/close-order/{order_id}")
async def close_order(order_id: int, order_status: OrderStatus):
    """
    Endpoint to close an order based on the given status and dispatches events.
    """
    if order_status.order_status == "won":
        dispatch_event(ORDER_CLOSED_WON, order_id)
        message = "Order closed as won"
    elif order_status.order_status == "lost":
        dispatch_event(ORDER_CLOSED_LOST, order_id)
        message = "Order closed as lost"
    else:
        raise HTTPException(status_code=400, detail="Invalid order status")

    return {"status": message, "order_id": order_id}

@app.post("/record-revenue/{order_id}/{revenue}", status_code=200)
async def record_revenue(order_id: int, revenue: float):
    """
    Endpoint to record revenue for an order and dispatch an event for financial updates.
    """
    dispatch_event(ORDER_CLOSED_WON_REVENUE, order_id, revenue)
    return {"status": "Revenue recorded", "order_id": order_id, "revenue": revenue}

@app.get("/data")
async def get_data():
    """
    Endpoint that returns random data for visualization purposes.
    """
    data = {
        'labels': ["January", "February", "March", "April", "May", "June", "July"],
        'values': [random.randint(0, 100) for _ in range(7)]
    }
    return JSONResponse(content=data)

@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Main HTML page that provides an interactive chart visualizing the data from the '/data' endpoint and lists other available API endpoints.
    """
    html_content = "<h1>Welcome to SalesBricks API</h1>"
    html_content += "<h2>Click on an endpoint to access:</h2><ul>"
    exclude_paths = ['/openapi.json', '/docs/oauth2-redirect', '/redoc', '/data']  # Exclude '/data' here
    for route in app.routes:
        if isinstance(route, fastapi.routing.APIRoute) and route.path not in exclude_paths:
            link = f"http://127.0.0.1:8000{route.path}"
            html_content += f"<li><a href='{link}'>{route.path}</a> (Methods: {', '.join(route.methods)})</li>"
    html_content += "</ul>"

    # Adding the Monthly Data section and the specific '/data' endpoint after general information
    html_content += "<h2>Monthly Data</h2>"
    html_content += "<ul><li><a href='http://127.0.0.1:8000/data'>/data</a> (Methods: GET)</li></ul>"
    html_content += """
    <canvas id="myChart" width="400" height="400"></canvas>
    <script>
        const ctx = document.getElementById('myChart').getContext('2d');
        fetch('/data').then(response => response.json()).then(data => {
            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Monthly Data',
                        data: data.values,
                        backgroundColor: 'rgba(255, 99, 132, 0.2)',
                        borderColor: 'rgba(255, 99, 132, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }).catch(error => console.error('Error loading the data:', error));
    </script>
    """

    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
