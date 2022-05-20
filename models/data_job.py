from sqlalchemy import Column, ForeignKey, BigInteger, Text, CheckConstraint, String
from base import Base
from sqlalchemy.orm import relationship

class DataJob(Base):
    """
    All the data jobs that processors will pick and run
    """

    __tablename__ = 'data_jobs'
    data_job_id = Column(BigInteger, primary_key=True, doc="Unique identifier")
    data_integration_id = Column(BigInteger, ForeignKey('data_integrations.data_integration_id'),nullable=True, doc="Refers data_integrations")
    account_id	= Column(BigInteger, ForeignKey('accounts.account_id'),nullable=False, doc="Refers accounts")
    type = Column(Text, CheckConstraint("type IN ('extract', 'transform_load', 'webhook_job')"), nullable=False, doc="One of: extract, transform_load, webhook_job")
    status = Column(Text, CheckConstraint("status IN ('ready', 'waiting', 'running')"), nullable=False, doc="One of: ready, waiting, running")
    processor_uuid	= Column(String(255), ForeignKey('processors.processor_uuid'),nullable=True, doc="Refers processors")
    pick_timestamp = Column(BigInteger, nullable=False, doc="To be picked only on or after this timestamp")
    last_runtime = Column(BigInteger, nullable=False, default=0, doc="Last runtime in millseconds. To sort to identify shorter job to pick")
    start_time = Column(BigInteger, nullable=True, doc="Job start time")
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)

    data_integration = relationship('DataIntegration', foreign_keys=[data_integration_id], backref='data_jobs')