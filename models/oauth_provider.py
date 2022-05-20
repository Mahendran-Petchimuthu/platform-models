from sqlalchemy import Integer, Column, ForeignKey, BigInteger, Text
from sqlalchemy.orm import relationship
from base import Base

class OAuthProvider(Base):
    """
    Holds information about the oauth client app for the data sources
    """

    __tablename__ = 'oauth_providers'
    oauth_provider_id = Column(BigInteger, primary_key=True, doc="Unique identifier")
    account_id = Column(BigInteger, ForeignKey('accounts.account_id'), nullable=False, doc="Refers accounts")
    type = Column(Text, nullable=False, doc="Provider type eg, Freshdesk")
    version = Column(Integer, nullable=False, default=2)
    client_id = Column(Text, nullable=False, doc="Oauth app client id")
    client_secret = Column(Text, nullable=False, doc="oauth app client secret")
    scope = Column(Text, nullable=False, doc="oauth scope")
    auth_url = Column(Text, nullable=False, doc="Authorize URL")
    token_url = Column(Text, nullable=False, doc="Token URL")
    revoke_url = Column(Text, nullable=True, doc="Token revoke URL")
    auth_redirect_url = Column(Text, nullable=False, doc="Authorize redirect URL")
    token_redirect_url = Column(Text, nullable=True, doc="Token redirect URL")
    configuration = Column(Text, nullable=True, doc="Additional configuration for oauth request")
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)

    oauth_token = relationship('OAuthToken', backref="oauth_provider")