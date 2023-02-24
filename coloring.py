class Coloring:
    # Define some ANSI escape codes for text colors
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

    def colorize(cls, text, color):
        return f"{color}{text}{cls.RESET}"

    def red( cls, text):
        return cls.colorize(text, cls.RED)
        
    def green( cls, text):
        return cls.colorize(text, cls.GREEN)

    def yellow( cls, text):
        return cls.colorize(text, cls.YELLOW)

    def blue( cls, text):
        return cls.colorize(text, cls.BLUE)

    def magenta( cls, text):
        return cls.colorize(text, cls.MAGENTA)

    def cyan( cls, text):
        return cls.colorize(text, cls.CYAN)