from pydantic import BaseModel
from typing import Collection, List, Optional




class Collection(BaseModel):
	id: Optional[int]
	name: Optional[str]
	slug: Optional[str]

class Asset(BaseModel):
	name: Optional[str]
	description: Optional[str]
	token_id: Optional[str]
	collection: Collection

class Account(BaseModel):
	id: Optional[int]
	address: Optional[str]
class PaymentToken(BaseModel):
	id: Optional[int]
	symbol: Optional[str]
	decimals: Optional[int]
class Event(BaseModel):
	id: Optional[int]
	asset: Asset
	event_type: Optional[str]
	quantity: Optional[str]
	payment_token: PaymentToken
	total_price: Optional[int]
	winner_account: Optional[Account]
	# transaction: transaction