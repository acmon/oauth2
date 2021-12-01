import requests

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


@router.get('/breweries')
async def get_breweries(token: str = Depends(oauth2_scheme)):
    breweries = requests.get('https://api.openbrewerydb.org/breweries/')

    return [{'name': brewery.get('name')} for brewery in breweries.json()]