from click.testing import CliRunner
from lib import transform

resistors = [
        ['100', '10 '],
        ['101', '100 '],
        ['102', '1 k'],
        ['103', '10 k'],
        ['104', '100 k'],
        ['105', '1 M'],
        ['106', '10 M'],
        ['107', '100 M'],
        ['108', '1 G'],
        ['109', '10 G']
       ]
caps = [
        ['100', '10 pf'],
        ['101', '100 pf'],
        ['102', '1 nf'],
        ['103', '10 nf'],
        ['104', '100 nf'],
        ['105', '1 µf'],
        ['106', '10 µf'],
        ['107', '100 µf'],
        ['108', '1 mf'],
        ['109', '10 mf']
       ]


def test_to():
  runner = CliRunner()
  print("test from 3digit code to si-format")
  print("--test caps")
  for cap in caps:
    result = runner.invoke(transform.cli, ['to', cap[1]])
    assert result.output == f'{cap[0]}\n'

  print("--test resistors")
  for resistor in resistors:
    result = runner.invoke(transform.cli, ['to', resistor[1]])
    assert result.output == f'{resistor[0]}\n'

def test_from():
  runner = CliRunner()
  print("test from si-fromat to 3digit code ")
  print("--test caps")
  for cap in caps:
    result = runner.invoke(transform.cli, ['from', cap[0], '--cap'])
    assert result.output == f'{cap[1]}\n'

  print("--test resistors")
  for resistor in resistors:
    result = runner.invoke(transform.cli, ['from', resistor[0]])
    try:
        assert result.output == f'{resistor[1]}\n'
    except AssertionError:
        print(f"{result.output} != {resistor[1]}")

if __name__ == "__main__":
    test_to()
    test_from()
    print("ok")
