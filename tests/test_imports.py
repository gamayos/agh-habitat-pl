"""
Test imports for the habitat_pl package.
"""
import sys
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


def test_import_habitat_pl():
    """Test that habitat_pl can be imported."""
    import habitat_pl
    assert habitat_pl.__version__ == "0.1.0"


def test_import_config():
    """Test that config module can be imported."""
    from habitat_pl import config
    assert hasattr(config, 'get_config')


def test_import_ee_auth():
    """Test that ee_auth module can be imported."""
    from habitat_pl import ee_auth
    assert hasattr(ee_auth, 'authenticate')
    assert hasattr(ee_auth, 'initialize')


def test_import_data_embeddings():
    """Test that data.embeddings module can be imported."""
    from habitat_pl.data import embeddings
    assert hasattr(embeddings, 'load_embeddings')
    assert hasattr(embeddings, 'process_embeddings')


def test_import_data_labels():
    """Test that data.labels module can be imported."""
    from habitat_pl.data import labels
    assert hasattr(labels, 'load_labels')
    assert hasattr(labels, 'validate_labels')


def test_import_viz_maps():
    """Test that viz.maps module can be imported."""
    from habitat_pl.viz import maps
    assert hasattr(maps, 'create_map')
    assert hasattr(maps, 'add_layer')


def test_config_get_config():
    """Test that config.get_config returns expected values."""
    from habitat_pl import config
    cfg = config.get_config()
    assert isinstance(cfg, dict)
    assert 'version' in cfg
    assert cfg['version'] == "0.1.0"


if __name__ == "__main__":
    # Run tests manually
    test_import_habitat_pl()
    test_import_config()
    test_import_ee_auth()
    test_import_data_embeddings()
    test_import_data_labels()
    test_import_viz_maps()
    test_config_get_config()
    print("All tests passed!")
