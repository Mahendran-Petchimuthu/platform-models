from sqlalchemy import  Column, BigInteger, Text, String
from base import Base

class Processor(Base):
    """
    FSU DP Processors management - Mapping active running processor
    """
    __tablename__ = 'processors'
    processor_uuid = Column(String(255), primary_key=True, doc="Unique identifier")
    processor_name = Column(Text, nullable=True, doc="human readable process name")
    hostname = Column(Text, nullable=False, doc="Host or IP where the processor is running")
    process_id = Column(BigInteger, nullable=True, doc="Latest process ID for this processor")
    signal = Column(Text, nullable=True, doc="shutdown/empty")
    start_time = Column(BigInteger, nullable=False, doc="Processor start or restart timestamp")
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)