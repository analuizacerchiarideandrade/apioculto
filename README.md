1.baixar e rodar docker-compose
2.https://github.com/ProfAnaLuizaImpacta/api/
3.testar db dbeaver
3.1 pip install -r requirements.txt

4. OBSERVAR QUE AGORA TEM RELACIONAMENTO

criar tres tables com nomes tb_users, tb_produtos, tb_setores
                from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
                from sqlalchemy.orm import relationship
                from db.base import Base
                from sqlalchemy_utils import EmailType
                class Produtos(Base):
                    __tablename__ = "tb_produtos"
                    id = Column('id', Integer, primary_key=True, autoincrement=True)
                    item = Column('item', String, nullable=False)
                    peso = Column('peso', Float)
                    numero_caixas = Column('numero_caixas', Integer)
                    created_at = Column('created_at', DateTime, server_default=func.now())
                    updated_at = Column('updated_at', DateTime, onupdate=func.now())
                    id_setor =Column('id_setor', ForeignKey('tb_setores.id'), nullable=False)
                class Setores(Base):
                    __tablename__ = 'tb_setores'
                    id = Column('id', Integer, primary_key=True, autoincrement=True)
                    nome = Column('nome', String, nullable=False)
                class Usuarios(Base):
                    __tablename__ = 'tb_usuarios'
                    id = Column('id', Integer, primary_key=True, autoincrement=True)
                    username = Column('username', String, nullable=False, unique=True)
                    password = Column('password', String, nullable=False)
                    email = Column('Email', EmailType)
5. Criar esquemas produto (mudou), usuario e setor
class Produtos(BaseModel):
id: int
item: str
peso: float
numero_caixas: int
id_setor: int


import re
from pydantic import validator, EmailStr, BaseModel
from datetime import datetime


class Usuarios(BaseModel):
    username: str
    password: str
    email: EmailStr

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|[0-9]|-|_|@)+$', value):
            raise ValueError('Invalid username')
        return value

from pydantic import BaseModel
from pydantic import validator
import re

#TODO criar pasta caso de uso
# #Este arquivo ficam as regras de negócio
import re
from pydantic import validator, BaseModel



class Setores(BaseModel):
    id: int
    nome: str



5.criar rota usuario apenas com create_engine
            from typing import List
            from fastapi import APIRouter, Response, Depends, status, Query, HTTPException
            from sqlalchemy.orm import Session
            from db.database import engine,SessionLocal
            from db.models import Usuarios as UsuariosModel
            from schemas.usuario import Usuarios as UsuariosSchema
            from db.base import Base
            #cria a tabela
            Base.metadata.create_all(bind=engine)
            router = APIRouter(prefix="/usuarios")   
            def get_db():
                try:
                    db = SessionLocal()
                    #TODO 
                    yield db
                finally:
                    db.close()
6.criar rota setor apenas com create_engine
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


7.Confirmar tudo checando no olho
8.rodar main e ver se funciona e se tabelas com prefixo tb foram criadas

9.registrar rotas no main e rodar para ver se tem algum erro de consoante
    from routes.produto_routes import router as produto_router
    from routes.setor_routes import router as setor_router
    from routes.usuario_routes import router as usuario_router
    from fastapi import FastAPI
    app = FastAPI()
    @app.get('/health-check') 
    def health_check():
    return True
    app.include_router(setor_router)
    app.include_router(produto_router)
    app.include_router(usuario_router)

10.criar métodos post nas tres e rodar no http://localhost:8003/docs
Body({
"id": 0,
"nome": "calças"
}) começando por setores


        @router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar setor')
        def add_setor(request:SetoresSchema, db_setor: Session = Depends(get_db)):
                # produto_on_db_setor = ProdutosModel(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
                setor_on_db = SetoresModel(**request.dict())
                db_setor.add(setor_on_db)
                db_setor.commit()
                return Response(status_code=status.HTTP_201_CREATED)
        @router.post("/addComSchema", status_code=status.HTTP_201_CREATED, description='Adicionar user')
        def add_user(request:UsuariosSchema, db: Session = Depends(get_db)):
                # produto_on_db = ProdutosModel(id=request.id, item=request.item, peso=request.peso, numero_caixas=request.numero_caixas)
                user_on_db_ = UsuariosModel(**request.dict())
                db.add(user_on_db_)
                db.commit()
                db.refresh(user_on_db_)
                return user_on_db_

11. remova o id no schema e veja o que acontece
class Setores(BaseModel):
    nome: str
{

"nome": "blusas"
}


12. Teste o usuario produtos, se consegue inserir
{
"username": "marcio",
"password": "senha",
"email": "joao@example.com"
}


13. Tente inserir um produto sem com id_setor 10

{
  "id": 1,
  "item": "blusa",
  "peso": 10,
  "numero_caixas": 0,
  "id_setor": 10
}