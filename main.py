#!/usr/bin/env python2.7

import os
import webapp2
import jinja2

# Getting the template directory
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

# Starting the Jinja2 Environment
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                                autoescape=True)

# Main Handler
class Handler(webapp2.RequestHandler):

    # shortcut for writing the outputs easily
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template,**kw))

# Main Page Handler
class MainPage(Handler):
    def get(self):
        items = self.request.get_all("item")
        self.render("shopping_list.html", items = items)

# Webserver start
app = webapp2.WSGIApplication([('/',  MainPage),
                               ], debug=True)
