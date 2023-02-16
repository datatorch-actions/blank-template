import sys
import datatorch

if __name__ == "__main__":
    inputs = datatorch.get_inputs()
    a: int = inputs.get('a')
    b: int = inputs.get('b')
    datatorch.set_output('sum', a + b)
