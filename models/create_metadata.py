from base import engine, Base

from account import Account
from data_connector_mapping import DataConnectorMapping
from data_processor_heartbeat import DataProcessorHeartbeat
from oauth_token import OAuthToken
from role import Role
from data_integration import DataIntegration
from data_integration_config import DataIntegrationConfig
from historical_data_job import HistoricalDataJob
from processor import Processor
from data_connector import DataConnector
from data_job import DataJob
from oauth_provider import OAuthProvider
from product import Product

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)