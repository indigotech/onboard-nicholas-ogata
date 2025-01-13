from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    SECRET_KEY: str = '1a3ce368f2647a527d2579437a09599849a90a71869f8f0ea5f1bfcdfab2e063'
    ALGORYTHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15

settings = Settings()
