from sqlalchemy import Column, ForeignKey, BigInteger, Text
from base import Base


class Account(Base):
    """
    Holds customers, act as namespaces for other tables
    """

    __tablename__ = 'accounts'
    account_id = Column(BigInteger, primary_key=True, doc="Account id in FSUDP")
    name = Column(Text, nullable=False, doc="Account name")
    product_id = Column(BigInteger, ForeignKey('products.product_id'),nullable=False, doc="Product source for this account")
    product_account_id = Column(Text, nullable=False, doc="Customer Instance id in the product")
    freshid_org_id = Column(BigInteger, nullable=False, doc="Org ID in the freshid")
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)