import os
from dotenv import load_dotenv
#TODO
from pathlib import Path


#vai no file env e armazena numa variável
env_path = Path('.') / '.env'
#Para simplificar
POSTGRES_USER = os.getenv('POSTGRES_USER')
print(POSTGRES_USER)

#coloca a variável no ambiente py, um tipo de nuvem no proprio py
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Luiza Board"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT") # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
settings = Settings()

#2