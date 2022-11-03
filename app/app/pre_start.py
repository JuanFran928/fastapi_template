import logging

from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from tenacity import retry
from tenacity.after import after_log
from tenacity.before import before_log
from tenacity.stop import stop_after_attempt
from tenacity.wait import wait_fixed

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)

def init_db() -> None:
    try:
        db: Session = SessionLocal()
        db.execute("SELECT 1")
    except Exception as e:
        logger.error(e)
        raise e



def main() -> None:
    logger.info("Initializing service")
    init_db()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    main()

