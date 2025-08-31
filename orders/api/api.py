from datetime import datetime
from uuid import UUID
from starlette.responses import Response
from starlette import status

from orders.app import app
from orders.api.schemas import GetOrderSchema, CreateOrderSchema, GetOrdersSchema

order = {
    "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "status": "delivered",
    "created": 'asdf',
    'updated': datetime.utcnow(),
    "order": [{"product": "coffe", "size": "medium", "quantity": 1}],
}


@app.get("/orders", response_model=GetOrdersSchema)
def get_orders():
    return {"orders": [order]}


@app.post("/orders", status_code=status.HTTP_201_CREATED, response_model=GetOrderSchema)
def create_order(order_details: CreateOrderSchema):
    return order


@app.get("/orders/{order_id}", response_model=GetOrderSchema)
def get_order(order_id: UUID):
    return order


@app.put("/orders/{order_id}", response_model=GetOrderSchema)
def update_order(order_id: UUID, order_detail: CreateOrderSchema):
    return order


@app.delete("/orders/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(order_id: UUID):
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.post("orders/{order_id}/cancel", response_model=GetOrderSchema)
def cancel_order(order_id: UUID):
    return order


@app.post("/orders/{order_id}/pay", response_model=GetOrderSchema)
def pay_order(order_id: UUID):
    return order

