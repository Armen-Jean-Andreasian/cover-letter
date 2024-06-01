import pydantic
from utils.file_readers.json_reader import read_json, write_json
from config import USER_DATA_JSON


class Applicant(pydantic.BaseModel):
	applicant_name: str | None = None
	applicant_data: str | None = None
	position: str | None = None
	email: pydantic.EmailStr | None = None
	phone: str | None = None
	website: str | None = None  # Annotated[HttpUrl, AfterValidator(str)]| None = None  is annoying and not working

	def __init__(self):
		super().__init__()
		self.load_last_data()

	def load_last_data(self) -> None:
		loaded_data = read_json(file_name=USER_DATA_JSON)
		for attr, value in loaded_data.items():
			if hasattr(self, attr):
				setattr(self, attr, value)

	def save_new_data(self) -> None:
		data_to_save = dict(filter(lambda item: item[1] is not None, self.model_dump(mode='json').items()))
		write_json(file_name=USER_DATA_JSON, data=data_to_save)
