from models import (
    Entry,   # Need to import to create
    Base
)
from app import engine


def main():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()
