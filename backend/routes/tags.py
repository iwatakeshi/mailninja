from fastapi import APIRouter

router = APIRouter()
tags = ['tags']

@router.get('/tags/{tag_id}', tags=tags)
async def get_one():
  return {}

@router.get('/tags', tags=tags)
async def get_many():
  return []

@router.post('/tags', tags=tags)
async def create():
  return {}

@router.delete('/tags/{tag_id}', tags=tags)
async def delete_one():
  return {}

@router.delete('/tags', tags=tags)
async def delete_many():
  return []