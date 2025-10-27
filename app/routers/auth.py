from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from starlette import status
from ..models import User, UserCreate, UserRead
from ..database import get_session
from ..security import get_password_hash


router = APIRouter(
    prefix="/auth",
)

# Create a New User
@router.post("/register/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_new_user(*, session: Session = Depends(get_session), user_in: UserCreate):
    """This will register a new user"""
    try:
        # Hash the plain text password
        hashed_password = get_password_hash(user_in.password)

        # Create a new user, replacing the plain text password with the hashed password
        db_user = User.model_validate(user_in, update={"hashed_password": hashed_password})

        session.add(db_user)
        session.commit()
        session.refresh(db_user)

        return db_user

    except IntegrityError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="A user with this username or email already exists.")

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"An Error occurred: {str(e)}")



