"""
Configuration module
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Default configurations
    """
    SSL_DISABLE = False
    LINKEDIN_PREFIX = 'https://www.linkedin.com/in/'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    Development phase configuration.
    """
    DEBUG = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class TestingConfig(Config):
    """
    Testing phase configuration.
    """
    DEBUG = False
    TESTING = True
    WTF_CSRF_ENABLED = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}