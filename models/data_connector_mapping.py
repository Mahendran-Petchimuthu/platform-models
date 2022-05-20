from sqlalchemy import Column, ForeignKey, BigInteger
from base import Base

class DataConnectorMapping(Base):
    """
    To identify credentials for the appropriate data connector for a data integration.  
    """
    __tablename__ = 'data_connector_mapping'
    data_integration_id = Column(BigInteger, ForeignKey('data_integrations.data_integration_id'), nullable=False, doc="Refers data_integrations", primary_key=True)
    account_id = Column(BigInteger, ForeignKey('accounts.account_id'), nullable=False, doc="Refers accounts", primary_key=True)
    data_connector_id = Column(BigInteger, ForeignKey('data_connectors.data_connector_id'), nullable=False, doc="Refers data_connetor", primary_key=True)
    create_time = Column(BigInteger, nullable=False)
