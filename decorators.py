def admin_only(func):
  def wrapper(username):
    if username == "admin":
      func(username)
    else:
      print("Access Denied")
  return wrapper

@admin_only
def dashboard(username):
  print(f"Welcome {username}, you have access to the dashboard.")

dashboard("admin")     
dashboard("user123") 