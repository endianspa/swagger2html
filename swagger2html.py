#!/usr/bin/env python
# -*- coding: utf-8 -*-
# +--------------------------------------------------------------------------+
# | Swagger2HTML                                                             |
# +--------------------------------------------------------------------------+
# | Copyright (c) 2004-2017 S.p.A. <info@endian.com>                         |
# |         Endian S.p.A.                                                    |
# |         via Pillhof 47                                                   |
# |         39057 Appiano (BZ)                                               |
# |         Italy                                                            |
# |                                                                          |
# | This program is free software; you can redistribute it and/or modify     |
# | it under the terms of the GNU General Public License as published by     |
# | the Free Software Foundation; either version 2 of the License, or        |
# | (at your option) any later version.                                      |
# |                                                                          |
# | This program is distributed in the hope that it will be useful,          |
# | but WITHOUT ANY WARRANTY; without even the implied warranty of           |
# | MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            |
# | GNU General Public License for more details.                             |
# |                                                                          |
# | You should have received a copy of the GNU General Public License along  |
# | with this program; if not, write to the Free Software Foundation, Inc.,  |
# | 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.              |
# +--------------------------------------------------------------------------+

# Convert a Swagger YAML file into an HTML

__author__ = "Andrea Bonomi <a.bonomi@endian.com>"
__date__ = "2017-05-04"

import sys
import yaml

HEADER = """
<!DOCTYPE html>
<html>
<head>
  <title>API Documentation</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<style type="text/css" media="all">

body, p, a, div, th, td {
  font-family: "Source Sans Pro", sans-serif;
  font-weight: 400;
  font-size: 16px;
}

h1 {
  font-family: "Source Sans Pro Semibold", sans-serif;
  font-weight: normal;
  font-size: 44px;
  line-height: 50px;
  margin: 0 0 10px 0;
  padding: 0;
}

h2 {
  font-family: "Source Sans Pro", sans-serif;
  font-weight: normal;
  font-size: 24px;
  line-height: 40px;
  margin: 0 0 20px 0;
  padding: 0;
}

section {
  border-top: 1px solid #ebebeb;
  padding: 30px 0;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 0 0 20px 0;
}

th {
  background-color: #f5f5f5;
  text-align: left;
  font-family: "Source Sans Pro", sans-serif;
  font-weight: 700;
  padding: 4px 8px;
  border: #e0e0e0 1px solid;
}

td {
  vertical-align: top;
  padding: 2px 8px;
  border: #e0e0e0 1px solid;
}

pre {
  background-color: #292b36;
  color: #ffffff;
  padding: 10px;
  border-radius: 6px;
  position: relative;
  margin: 10px 0 20px 0;
}

pre.language-html {
  margin: 40px 0 20px 0;
}

pre.language-html:before {
  content: attr(data-type);
  position: absolute;
  top: -30px;
  left: 0;
  font-family: "Source Sans Pro", sans-serif;
  font-weight: 600;
  font-size: 15px;
  display: inline-block;
  padding: 2px 5px;
  border-radius: 6px;
  text-transform: uppercase;
  background-color: #3387CC;
  color: #ffffff;
}

pre.language-html[data-type="get"]:before {
  background-color: green;
}

pre.language-html[data-type="put"]:before {
  background-color: #e5c500;
}

pre.language-html[data-type="post"]:before {
  background-color: #4070ec;
}

pre.language-html[data-type="delete"]:before {
  background-color: #ed0039;
}

</style>
</head>
<body>
<div class="container-fluid">
<div id="sections">
"""

THEADER = """
        <thead>
          <tr>
            <th style="width: 30%">Field</th>
            <th style="width: 10%">Type</th>
            <th style="width: 70%">Description</th>
          </tr>
        </thead>
"""

def main():
    if len(sys.argv) < 2:
        print('usage: %s <SWAGGER_FILE>' % sys.argv[0])
        sys.exit(2)
    with open(sys.argv[1] + '.html', 'w') as output:
        output.write(HEADER)
        data = yaml.load(file(sys.argv[1]))
        for api_path, api in sorted(data.get('paths', {}).iteritems()):
            for method, body in sorted(api.iteritems()):
                output.write('<pre class="prettyprint language-html prettyprinted" data-type="%s"><code><span class="pln">%s</span></code></pre>' % (method, api_path))
                output.write('<p>%s</p>' % body.get('summary'))
                output.write('<h2>Parameters</h2>\n')
                output.write('<table>\n')
                output.write(THEADER)
                output.write('<tbody>\n')
                for parameter_body in body.get('parameters', []):
                    output.write('<tr>\n')
                    output.write('<td>%s</td>\n' % parameter_body.get('name'))
                    output.write('<td>%s</td>\n' % parameter_body.get('type'))
                    output.write('<td>%s</td>\n' % parameter_body.get('description'))
                    output.write('</tr>\n')
                output.write('</tbody>\n')
                output.write('</table>')
                output.write('<p>&nbsp;</p>\n')
        output.write('</div>')
        output.write('</div>')
        output.write('</body>')
        output.write('</html>')


if __name__ == '__main__':
    main()
