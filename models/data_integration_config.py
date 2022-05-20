
from sqlalchemy import Column, ForeignKey, BigInteger, Text
from base import Base
from sqlalchemy.orm import relationship

class DataIntegrationConfig(Base):
    """
    Holds the transformation config for a data integration - both staging and production
    """
    __tablename__ = 'data_integration_config'
    data_integration_config_id	= Column(BigInteger, primary_key=True, doc="Unique identifier")
    account_id	= Column(BigInteger, ForeignKey('accounts.account_id'), nullable=False, doc="Refers account")
    data_integration_id = Column(BigInteger, ForeignKey('data_integrations.data_integration_id'), nullable=False, doc="Refers data_integrations")
    configuration_json_s3_path = Column(Text, nullable=False, doc="Transformation configuration JSON S3 path")
    ui_configuration_json_s3_path = Column(Text, nullable=False, doc="S3 path for configuration used to refer UI")
    production_data_integration_config_id = Column(BigInteger, nullable=True, doc="Contains reference to the production's data_integration_config_id")
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)

    data_integration = relationship('DataIntegration', foreign_keys=[data_integration_id], backref='data_integration_config')