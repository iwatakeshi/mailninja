from fastapi import APIRouter

router = APIRouter()
tags = ['Lists']

@router.get('/lists/{list_id}', tags=tags)
async def get_one():
  return {}

@router.get('/lists', tags=tags)
async def get_many():
  return []

@router.post('/lists', tags=tags)
async def create():
  return {}

@router.delete('/lists/{list_id}', tags=tags)
async def delete_one():
  return {}

@router.delete('/lists', tags=tags)
async def delete_many():
  return []

@router.get('/lists/{list_id}/members', tags=tags + ['List Members'])
async def get_many_list_members():
  return []

@router.post('/lists/{list_id/members', tags=tags + ['List Members'])
async def create_list_member():
  return {}