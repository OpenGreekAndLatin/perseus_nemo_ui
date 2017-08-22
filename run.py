from tests.test_resources import NautilusDummy
from pkg_resources import resource_filename
from cts_leipzig_ui import CTSLeipzigUI
from flask_nemo import Nemo
from flask_nemo.chunker import level_grouper
from flask import Flask

app = Flask("Nemo")
app.debug = True
nemo = Nemo(
    app=app,
    base_url="",
    resolver=NautilusDummy,
    chunker={"default": lambda x, y: level_grouper(x, y, groupby=30)},
    plugins=[CTSLeipzigUI("HERE")],
    transform={
        "default": resource_filename("cts_leipzig_ui", "data/assets/static/xslt/epidocShort.xsl")
    }
)

if __name__ == "__main__":
    app.run()
