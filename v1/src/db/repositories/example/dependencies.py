from v1.src.db.repositories.example.repo import ExampleRepo
from v1.src.db.repositories.example.abs_repo import AbsExampleRepo


async def get_example_repo() -> AbsExampleRepo:
    return ExampleRepo()
