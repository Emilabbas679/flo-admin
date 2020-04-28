from core.settings.base import Config


class DevelopmentConfig(Config):
    """ Configuration class for site development environment """

    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = "postgres://postgres:password@localhost/flocake-new"

    # SQLALCHEMY_DATABASE_URI = "postgres:///flocake_dev"
    # SQLALCHEMY_DATABASE_URI = "postgresql://flocake:mua7ren9cpv753rs@flocake-prod-new-do-user-6879125-0.a.db.ondigitalocean.com:25060/flocake_prod?sslmode=require"
