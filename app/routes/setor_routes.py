from typing import List
from fastapi import APIRouter, Response, Depends, status, Query, HTTPException
from sqlalchemy.orm import Session
from db.database import engine,SessionLocal
from db.models import Setores as SetoresModel
from schemas.setor import Setores as SetoresSchema

from db.base import Base


#cria a tabela
Base.metadata.create_all(bind=engine)
router = APIRouter(prefix="/setores")   

def get_db():
    try:
        db = SessionLocal()
        #TODO 
        yield db
    finally:
        db.close()


@router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar setor')
def add_setor(request:SetoresSchema, db_setor: Session = Depends(get_db)):
        # produto_on_db_setor = ProdutosModel(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
        setor_on_db = SetoresModel(**request.dict())
        db_setor.add(setor_on_db)
        db_setor.commit()
        return Response(status_code=status.HTTP_201_CREATED)