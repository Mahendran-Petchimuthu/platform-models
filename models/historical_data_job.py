from sqlalchemy import Column, ForeignKey, BigInteger, Text, CheckConstraint, String
from base import Base

class HistoricalDataJob(Base):
    """
    Contains historical data job runs (last 6 months)
    """

    __tablename__ = 'historical_data_jobs'
    data_job_id = Column(BigInteger, primary_key=True, doc="Unique identifier")
    data_integration_id = Column(BigInteger, ForeignKey('data_integrations.data_integration_id'), nullable=True, doc="Refers data_integration")
    account_id	= Column(BigInteger, ForeignKey('accounts.account_id'), nullable=False, doc="Refers account")
    type = Column(Text, CheckConstraint("type IN ('extract', 'transform_load', 'webhook_job')"), nullable=False, doc="One of: extract, transform, load, webhook_job")
    processor_uuid	= Column(String(255), ForeignKey('processors.processor_uuid'), nullable=False, doc="Refers processors")
    status = Column(Text, CheckConstraint("status IN ('completed', 'failed', 'stopped')"), nullable=False, doc="One of: completed, failed, stopped")
    failure_message = Column(Text, nullable=True, doc="Failure message")
    start_time = Column(BigInteger, nullable=False, doc="Job's start time")
    run_time = Column(BigInteger, nullable=False, doc="Job's total runtime in millseconds")
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)