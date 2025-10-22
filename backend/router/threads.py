from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from dbConnection import get_session
from models.dbModel import Thread


router = APIRouter(tags=["chats"])


# get all threads from db
@router.get("/threads")
def allThreads(session_db: Session = Depends(get_session)):
    try:
        threads = session_db.exec(select(Thread)).all()
        return threads
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


# get thread by id
@router.get("/threads/{thread_id}")
def get_thread(id: str, session_db: Session = Depends(get_session)):
    try:
        thread = session_db.get(Thread, id)
        if not thread:
            raise HTTPException(status_code=404, detail="oops! Thread not found")
        else:
            return thread
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


# delete thread by id
@router.delete("/threads/{thread_id}/delete")
def delete_thread(id: str, session_db: Session = Depends(get_session)):
    try:
        thread = session_db.get(Thread, id)
        if not thread:
            raise HTTPException(status_code=404, detail="Thread not found")
        session_db.delete(thread)
        session_db.commit()
        return {"detail": "Thread deleted successfully"}
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))


@router.post("/chats")
def create_chat(id: str, message: str, session_db: Session = Depends(get_session)):
    if not id and not message:
        raise HTTPException(
            status_code=400, detail="Thread ID and message are required"
        )
    try:
        thread = session_db.get(Thread, id)
        if not thread:
            new_thread = Thread(
                threadId=id,
                title=message,
            )
            session_db.add(new_thread)
            session_db.commit()
            session_db.refresh(new_thread)
    except Exception as err:

        raise HTTPException(status_code=500, detail=str(err))
