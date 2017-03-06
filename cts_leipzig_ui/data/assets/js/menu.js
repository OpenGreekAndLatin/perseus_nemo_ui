'use strict';

$(document).ready(function($) {
    var texts_authors = new Bloodhound({
      datumTokenizer: Bloodhound.tokenizers.obj.whitespace('value'),
      queryTokenizer: Bloodhound.tokenizers.whitespace,
      prefetch: $("#fullsearch").attr("data-target")
    });

    $("#fullsearch").typeahead({
      minLength: 3,
      highlight: true
    },
    {
      name: 'my-dataset',
      source: texts_authors,
      templates: {
        empty: '<div class="empty-message">0 Results</div>',
        suggestion: Handlebars.compile('<div><strong>{{title}}</strong><div>{{parents}}<br /><small>{{description}}</small></div></div>')
      }
    });

    $('#fullsearch').bind('typeahead:select', function(ev, suggestion) {
        ev.preventDefault();
       window.location = suggestion.uri;
    });
});