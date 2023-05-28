from fastapi import APIRouter

from controller import produtos_controller as produtos

router = APIRouter ()

router.include_router(produtos.router, prefix='/produtos')