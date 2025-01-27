from app.core.types import MongoListModel, MongoModel, PydanticObjectId


class CampusSchema(MongoModel):
    id: PydanticObjectId
    name: str
    
    class Config:
        orm_mode = True

class CampusListSchema(MongoListModel):
    __root__: list[CampusSchema]

    class Config:
        orm_mode = True