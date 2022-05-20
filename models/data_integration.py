from sqlalchemy import Integer, Column, ForeignKey, BigInteger, Boolean, Text, CheckConstraint
from base import Base
from sqlalchemy.orm import relationship

class DataIntegration(Base):
    """
    Holds a single data integration definition.
    """

    __tablename__ = 'data_integrations'
    data_integration_id	= Column(BigInteger, primary_key=True, doc="Unique identifier")
    account_id	= Column(BigInteger, ForeignKey('accounts.account_id'), nullable=False, doc="Refers accounts")
    name = Column(Text, nullable=False, doc="Integration Name")
    source_data_connector_type = Column(Text, nullable=False, doc="Source data connector type")
    source_data_connector_id = Column(BigInteger, ForeignKey('data_connectors.data_connector_id'), nullable=False, doc="Primary Data connector ID ")
    destination_data_connector_type	= Column(Text, nullable=False, doc="Currently only 'freshsuccess'")
    destination_data_connector_id = Column(BigInteger, ForeignKey('data_connectors.data_connector_id'), nullable=False, doc="Data destination connector ID")
    state = Column(Text, CheckConstraint("state IN ('initial', 'active', 'failed', 'inactive')"), nullable=False, doc="State of the data integration")
    latest_failure_message	= Column(Text, nullable=True, doc="Latest failure message")
    reverse_data_integration_id = Column(BigInteger, ForeignKey('data_integrations.data_integration_id'), nullable=True, doc="Data_integration_id for reverse sync")
    is_primary = Column(Boolean, nullable=False, default=True, doc="Used in fixing the data conflicts for the bidirectional sync")
    full_sync_interval_days = Column(Integer,nullable=False,default=30)
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)

    source_data_connector = relationship('DataConnector', foreign_keys=[source_data_connector_id])
    destination_data_connector = relationship('DataConnector', foreign_keys=[destination_data_connector_id])