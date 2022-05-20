from sqlalchemy import Column, ForeignKey, BigInteger, Text, String
from base import Base

class DataProcessorHeartbeat(Base):
    """
    Stores the heartbeats of the processors
    """

    __tablename__ = 'processor_heartbeats'
    processor_uuid	= Column(String(255), ForeignKey('processors.processor_uuid'), nullable=False, primary_key=True, doc="Refers Processor")
    data_job_id = Column(BigInteger, nullable=False, primary_key=True, doc="Last data job ID from where heartbeat is updated")
    timestamp = Column(BigInteger, nullable=False, doc="Last heartbeat received timestamp")