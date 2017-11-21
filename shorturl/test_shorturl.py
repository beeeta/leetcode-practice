import config
import core

def test_config():
    assert config.db.get('mysql').get('dburl')

def test_geneurl():
    url = "http://abc/bcd"
    core.gene_shorturl(url)
    assert True