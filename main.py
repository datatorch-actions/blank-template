import sys
import datatorch

if __name__ == "__main__":
    inputs = datatorch.get_inputs()
    url = inputs.get('url')
    datatorch.set_output('completed', True)
