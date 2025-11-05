"""
Earth Engine authentication module.
"""


def authenticate():
    """
    Authenticate with Google Earth Engine.
    """
    try:
        import ee
        ee.Authenticate()
    except ImportError:
        raise ImportError("earthengine-api is required for authentication")


def initialize():
    """
    Initialize Earth Engine API.
    """
    try:
        import ee
        ee.Initialize()
    except ImportError:
        raise ImportError("earthengine-api is required for initialization")
