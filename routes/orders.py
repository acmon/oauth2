from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

from Models import Orders

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


@router.post('/orders')
async def create_order(order: Orders, token: str = Depends(oauth2_scheme)):
    return order

