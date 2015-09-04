## escpos-cli

escpos-cli is a command-line utility for printing stuff using pyxmlescpos

### Installing

```
pip2 install -U git+https://github.com/kalmanolah/escpos-cli.git
```

### Usage

From the command line:

```
$ escpos-print --device-vendor-id 0x04b8 --device-product-id 0x0e15 '<receipt><h1 align="center">Test Receipt!</h1><line/></receipt>'
```

### Dependencies

This utility depends on [pyxmlescpos](https://github.com/fvdsn/py-xml-escpos).
Currently, my fork located [here](https://github.com/kalmanolah/py-xml-escpos)
is used since it adds additional support for QR codes.
