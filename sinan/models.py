"""
In this model, instead of setting up datamodels from scratch,
we will "reflect" an existing model using SQLAlchemy's Automap feature
"""

from django.db import models
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData


def get_base(connection_string, tables=None):
    """
    Introspect the given database returning a database object
    :param connection_string: SQLAlchemy connection string
    :param tables: list with tables names to reflect. Default all
    :return:
    """
    engine = create_engine(connection_string)
    if tables is not None:  # reflecting only specified tables
        metadata = MetaData()
        metadata.reflect(engine, only=tables)
        Base = automap_base(metadata=metadata)
        Base.prepare()
    else:
        Base = automap_base()
        Base.prepare(engine, reflect=True)

    return Base


