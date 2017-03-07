# -*- coding: utf-8 -*-

from flask_nemo.plugin import PluginPrototype
from pkg_resources import resource_filename
from flask import jsonify, url_for


class CTSLeipzigUI(PluginPrototype):
    """
        The Breadcrumb plugin is enabled by default in Nemo.
        It can be overwritten or removed. It simply adds a breadcrumb

    """
    HAS_AUGMENT_RENDER = False
    TEMPLATES = {
        "main": resource_filename("cts_leipzig_ui", "data/templates/main"),
        "cts_leipzig": resource_filename("cts_leipzig_ui", "data/templates/cts_leipzig")
    }
    CSS = [resource_filename("cts_leipzig_ui", "data/assets/css/theme-ext.css")]
    JS = [
        resource_filename("cts_leipzig_ui", "data/assets/js/typeahead.bundle.min.js"),
        resource_filename("cts_leipzig_ui", "data/assets/js/autocomplete.bundle.min.js"),
        resource_filename("cts_leipzig_ui", "data/assets/js/menu.js")
    ]
    STATICS = [
        resource_filename("cts_leipzig_ui", "data/assets/images/perseus.png")
    ]
    ROUTES = [
        ("/typeahead/collections.json", "r_typeahead_json", ["GET"])
    ]

    CACHED = ["r_typeahead_json"]

    def r_typeahead_json(self):
        """ List of resource for typeahead
        """

        locale = self.nemo.get_locale()
        collection = self.nemo.resolver.getMetadata()
        data = []
        for collection in collection.readableDescendants:
            parents = ", ".join([str(p.get_label(locale)) for p in collection.parents if p.get_label(locale)])
            title = str(collection.get_label(locale))
            desc = collection.get_description(locale)
            if desc is not None:
                desc = str(desc)
            else:
                desc = ""
            data.append({
                "value": title + ", " + parents + desc,
                "title": title,
                "parents": parents,
                #"description": desc,
                "uri": url_for(".r_first_passage", objectId=str(collection.id))
            })
        return jsonify(data)
