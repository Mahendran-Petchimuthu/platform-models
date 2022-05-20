from sqlalchemy import Column, ForeignKey, BigInteger, Boolean, Text
from base import Base

class Role(Base):
    """
    Contains different roles a product can have
    """

    __tablename__ = 'roles'
    role_id = Column(BigInteger, primary_key=True, doc="Unique identifier")
    account_id	= Column(BigInteger, ForeignKey('accounts.account_id'), nullable=False, doc="Refers accounts")
    name = Column(Text, nullable=False, doc="Role's name")
    description = Column(Text, nullable=True, doc="Description about role")
    is_super_admin = Column(Boolean, nullable=False,default=False, doc="Can create new products, manage processors and jobs ")  
    can_update_data_integration = Column(Boolean, nullable=False,default=False, doc="Can create/update new data integration")  
    can_delete_data_integration = Column(Boolean, nullable=False,default=False, doc="Can delete a data integration")  
    can_update_data_sources = Column(Boolean, nullable=False,default=False, doc="Can create/update data sources")  
    can_delete_data_sources = Column(Boolean, nullable=False,default=False, doc="Can delete data sources")  
    can_update_staging_config = Column(Boolean, nullable=False,default=False, doc="Can update staging data_integration_config")  
    can_update_production_config = Column(Boolean, nullable=False,default=False, doc="Can update production data_integration_config")  
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)

