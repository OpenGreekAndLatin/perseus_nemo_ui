# -*- coding: utf-8 -*-

from flask_nemo.plugin import PluginPrototype
from pkg_resources import resource_filename


class CTSLeipzigUI(PluginPrototype):
    """
        The Breadcrumb plugin is enabled by default in Nemo.
        It can be overwritten or removed. It simply adds a breadcrumb

    """
    HAS_AUGMENT_RENDER = False
    TEMPLATES = {
        "main": resource_filename("cts_leipzig_ui", "data/templates/main")
    }
    CSS = [resource_filename("cts_leipzig_ui","data/assets/css/theme-ext.css")]

