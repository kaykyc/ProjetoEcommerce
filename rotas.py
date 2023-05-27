from fastapi import APIRouter

from controllers import produtos_controllers as produtos

router = APIRouter ()

router.include_router(produtos.router, prefix='/produtos')