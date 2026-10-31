from pydantic import Field
from sqlalchemy import URL
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  postgre_host: str
  postgre_port: int = Field(ge = 1, le = 65535)
  postgre_user: str
  postgre_password: str
  database_name: str

  @property
  def database_url(self) -> URL:
    return URL.create(
      drivername='postgresql+asyncpg', 
      username=self.postgre_user, 
      password=self.postgre_password, 
      host=self.postgre_host,
      port=self.postgre_port,
      database=self.database_name)

  model_config = SettingsConfigDict(env_file=".env", env_file_encoding="UTF-8", extra="ignore")

settings = Settings()