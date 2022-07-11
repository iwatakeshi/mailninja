from fastapi import APIRouter

router = APIRouter()

@router.get('/tags/{tag_id}', tags=['tags'])
async def get_one():
  return {}

@router.get('/tags', tags=['tags'])
async def get_many():
  return []

@router.post('/tags')
async def create():
  return {}

@router.delete('/tags/{tag_id}')
async def delete_one():
  return {}

@router.delete('/tags')
async def delete_many():
  return []