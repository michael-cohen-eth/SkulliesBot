from pydantic import BaseModel
from typing import List, Optional



class Event(BaseModel):
	id: int
	