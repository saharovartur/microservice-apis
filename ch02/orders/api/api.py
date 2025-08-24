from datetime import datetime
from uuid import UUID
from starlette.responses import Response
from starlette import status

from ch02.orders import app

order = {
    'id': 'f47ac10b-58cc-4372-a567-0e02b2c3d479',
    'status': 'delivered',
    'created': datetime.utcnow(),
    'order': [
        {
            'product': 'coffe',
            'size': 'medium',
            'quantity': 1
        }
    ]
}