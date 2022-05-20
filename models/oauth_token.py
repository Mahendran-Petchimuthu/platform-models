from sqlalchemy import  Column, ForeignKey, BigInteger, Text, String
from base import Base

class OAuthToken(Base):
    """
    Holds OAuthToken to access the app to extract/load the info to third party system
    """

    __tablename__ = 'oauth_tokens'
    oauth_provider_id = Column(BigInteger, ForeignKey('oauth_providers.oauth_provider_id'), primary_key=True, doc="Refers oauth_providers")
    account_id = Column(BigInteger, ForeignKey('accounts.account_id'), primary_key=True, doc="Refers accounts")
    type = Column(Text, nullable=False, doc="Provider type, eg: freshdesk")
    user_context = Column(String(300), nullable=False, primary_key=True, doc="User context json to map the token to.  Eg: {\"email\": <user_email>}")
    access_token = Column(Text, nullable=False, doc="User access token")
    refresh_token = Column(Text, nullable=True, doc="Refresh token to refresh access token")
    refresh_after = Column(BigInteger, nullable=True, doc="Refresh the token after this timestamp")
    create_time = Column(BigInteger, nullable=False)
    modify_time = Column(BigInteger, nullable=False)