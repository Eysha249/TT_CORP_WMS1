import tkinter as tk

from App.Auth.AuthenticationPage import AuthenticationPage
from App.Dashboard.DashboardPage import DashboardPage

class Navigation:
    def __init__(self, root: tk, active_page="login"):#default to login page
      self.root = root
      self.active_page = None #active page tracks the current page that we want to be on
      self.routes = { #routes are different pages in this app
          "login": AuthenticationPage(root, self), #Create instance of page to be used when navigating
          "dashboard": DashboardPage(root, self)
      }
      self.navigate_to(active_page)
      pass

    def navigate_to(self, route_name): #this function is responsible for navigating to the different pages within the app by the provided route name
        if(self.active_page is not None):
            self.active_page.destroy()#tearin down the previous page so the next page has a clear slate to render on
            
        print(f"Navigating to {route_name}") # we look at routes and get the page by the route name
        self.active_page = self.routes[route_name] #set the current active page 
        self.active_page.render()#render/re-render page with its elements