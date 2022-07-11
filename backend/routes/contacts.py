from fastapi import APIRouter

router = APIRouter()
tags = ['Contacts']

@router.get('/contacts/{contact_id}', tags=tags)
async def get_one():
  return {}

@router.get('/contacts', tags=tags)
async def get_many():
  return []

@router.post('/contacts', tags=tags)
async def create():
  return {}

@router.post('/contacts/{contact_id}', tags=tags)
async def update():
  return {}

@router.delete('/contacts/{contact_id}', tags=tags)
async def delete_one():
  return {}

@router.delete('/contacts', tags=tags)
async def delete_many():
  return []
