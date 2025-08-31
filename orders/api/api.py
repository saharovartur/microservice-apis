from datetime import datetime
from uuid import UUID
from starlette.responses import Response
from starlette import status

from orders.app import app
from orders.api.schemas import CreateOrderSchema

order = {
    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "status": "delivered",
    "created": datetime.utcnow(),
    "order": [{"product": "coffe", "size": "medium", "quantity": 1}],
}


@app.get("/orders")
def get_orders():
    return {"orders": [order]}


@app.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order_details: CreateOrderSchema):
    return order


@app.get("/orders/{order_id}")
def get_order(order_id: UUID):
    return order


@app.put("/orders/{order_id}")
def update_order(order_id: UUID, order_detail: CreateOrderSchema):
    return order


@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("orders/{order_id}/cancel")
def cancel_order(order_id: UUID):
    return order


@app.post("/orders/{order_id}/pay")
def pay_order(order_id: UUID):
    return order

