<%inherit file="/base.mako" />

<%def name="head_tags()">
  <title>${c.data['title']}</title>
</%def>

<h1>${c.data['series']}</h1>
<h2>${c.data['season']}x${c.data['episode']}</h2>
