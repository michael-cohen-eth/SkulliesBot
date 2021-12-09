from datetime import datetime
from pydantic import BaseModel
from typing import Collection, Dict, Optional




class Collection(BaseModel):
	id: Optional[int]
	name: Optional[str]
	slug: Optional[str]

class Asset(BaseModel):
	name: Optional[str]
	description: Optional[str]
	token_id: Optional[str]
	collection: Collection
	permalink: Optional[str]

class Account(BaseModel):
	id: Optional[int]
	address: Optional[str]
class PaymentToken(BaseModel):
	id: Optional[int]
	symbol: Optional[str]
	decimals: Optional[int]

class Transaction(BaseModel):
	id: Optional[int]
	from_account: Optional[Account]
	to_account: Optional[Account]
	timestamp: Optional[datetime]

	@property
	def time_occurred(self) -> Optional[int]:
		if self.timestamp:
			return int(self.timestamp.strftime("%s"))
		return None

class Event(BaseModel):
	id: Optional[int]
	asset: Asset
	event_type: Optional[str]
	quantity: Optional[str]
	payment_token: PaymentToken
	total_price: Optional[int]
	winner_account: Optional[Account]
	transaction: Transaction