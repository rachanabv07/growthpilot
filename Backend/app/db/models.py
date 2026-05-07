from sqlalchemy import Column, String, JSON

from app.db.session import Base
from sqlalchemy import JSON



class Job(Base):
    

    __tablename__ = "jobs"

    id = Column(String, primary_key=True)

    status = Column(String)

    input_data = Column(JSON)
    
    steps = Column(JSON, default=[])

    result = Column(JSON)