from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from dbConnection import get_session
from models.dbModel import Thread, Message
from datetime import datetime
import uuid
from .llmResponse import handle_llm_response


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
    if not id or not message:
        raise HTTPException(
            status_code=400, detail="Thread ID and message are required"
        )
    try:
        thread = session_db.get(Thread, id)
        if not thread:
            newThread = Thread(
                threadId=id,
                title=message,
                messages=[
                    Message(
                        id=str(uuid.uuid4()),
                        role="user",
                        content=message,
                        timestamp=datetime.now(),
                    )
                ],
            )
            session_db.add(newThread)
            session_db.commit()
            session_db.refresh(newThread)
        else:
            newMessage = Message(
                id=str(uuid.uuid4()),
                role="user",
                content=message,
                timestamp=datetime.now(),
            )
            thread.messages.append(newMessage)
            thread.updatedAt = datetime.now()
            session_db.add(thread)
            session_db.commit()
            session_db.refresh(thread)

        assistantReply = handle_llm_response(message)
        llmMsg = Message(
            id=str(uuid.uuid4()),
            role="assistant",
            content=str(assistantReply),
            timestamp=datetime.now(),
        )
        if thread:
            thread.messages.append(llmMsg)
            return llmMsg
        else:
            newThread.messages.append(llmMsg)
            return llmMsg

    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
