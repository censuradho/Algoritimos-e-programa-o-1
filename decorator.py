def valida (arg_decorator):
  def wrapperDecorator (function):
    def wrapper (arg):
      value = function(arg)
    if value in arg_decorator:
      function(arg)

