import sys
import datatorch

if __name__ == "__main__":
    inputs = datatorch.get_inputs()
    url: string = inputs.get('url')
    datatorch.set_output('completed', true)
