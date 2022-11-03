from typing import Any

from fastapi import APIRouter, Depends
from pydantic import EmailStr

import app.schemas as schemas
from app.api import deps
from app.mail import send_test_email

router = APIRouter(prefix="/utils", tags=["utils"])


@router.post(
    "/test-email",
    response_model=schemas.Msg,
    status_code=201,
    dependencies=[Depends(deps.get_current_active_superuser)],
)
def test_email(
    email_to: EmailStr,
) -> Any:
    """Test email sending."""
    send_test_email(email_to=email_to)
    return {"msg": "Test email was sent."}
