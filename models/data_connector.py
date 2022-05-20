from sqlalchemy import Column, ForeignKey, BigInteger, Boolean, Text
from base import Base

class DataConnector(Base):
    """
    Holds details of Data connector along with authentication mapping
    """
    __tablename__ = 'data_connectors'
    data_connector_id = Column(BigInteger, primary_key=True, doc="Unique identifier")
    account_id = Column(BigInteger, ForeignKey('accounts.account_id'), nullable=False, doc="Refers accounts")
    webhook_enabled = Column(Boolean, nullable=False, default=False)
    webhook_metadata_json = Column(Text, nullable=True, doc="Metadata including authentication hash")
    data_connector_type = Column(Text, nullable=False, doc="Data connector type")
    connector_domain = Column(Text, nullable=False, doc="URL/domain of the third-party system")
    encrypted_credentials_json = Column(Text, nullable=True, doc="Credentials in JSON - encrypted using product's encryption key")
    oauth_provider_id = Column(BigInteger, ForeignKey('oauth_providers.oauth_provider_id'), nullable=True, doc="Refers oauth_providers")
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)