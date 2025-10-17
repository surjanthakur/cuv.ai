from fastapi import APIRouter, HTTPException, status


router = APIRouter(tags=["Chats"])


@router.post("/chats", status_code=status.HTTP_201_CREATED)
async def create_chat():
    pass
