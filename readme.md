# si_cli

A tool to convert from and to cap and resistor values in a 3 digit format(SI-Format)

## Installation

```
pip install si_cli
```

## Usage

```
$ si from 104
100 k
$ si from 104 --cap
100 nf
$ si to 100k
104
$ si to 100nf
104
```

When using `to` there is no need for the `--cap` flag. Cap values are calculated if the input ends with an `f`
