from pydantic import BaseModel, Field, ConfigDict

class SupplierRead(BaseModel):
  model_config = ConfigDict(str_strip_whitespace=True)
  id:int = Field(gt=0)
  name:str = Field(min_length=2)