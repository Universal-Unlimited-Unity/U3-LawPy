from pydantic import BaseModel, Field


class DefinitionBody(BaseModle):
  id: str
  text: str
  obj: str | list[str]
  definition: str
  alises: list[str]
