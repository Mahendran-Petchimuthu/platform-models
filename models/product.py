
from sqlalchemy import Column, BigInteger, Boolean, Text
from sqlalchemy.orm import relationship
from base import Base


class Product(Base):
    """
    Product details (API client), using which system APIs can be accessed
    """

    __tablename__ = 'products'
    product_id = Column(BigInteger, primary_key=True, doc="Product Id")
    name = Column(Text, nullable=False, doc="Product Name")
    description = Column(Text, nullable=True, doc="Short description about product")
    jwt_secret = Column(Text, nullable=False, doc="Key to validate jwt token")
    encryption_key = Column(Text, nullable=False, doc="Key to encrypt/decrypt data source credentials")
    is_active = Column(Boolean, nullable=False,default=False, doc="To indicate product is active or not")  
    create_time = Column(BigInteger, nullable=False, doc="Created timestamp")
    modify_time = Column(BigInteger, nullable=False, doc="Last modified timestamp")
    accounts = relationship("Account", backref="product")
