"""Main module."""
import logging
import argparse

from xmlescpos.printer import Usb


logger = logging.getLogger(__name__)
__VERSION__ = '0.0.1'


def main():
    """Main function."""
    def auto_int(x):
        """Convert a string to int with auto base detection."""
        return int(x, 0)

    parser = argparse.ArgumentParser(prog='escpos-cli', description='%(prog)s is a command-line utility for printing stuff using pyxmlescpos')
    parser.add_argument('-dvid', '--device-vendor-id', required=True, type=auto_int)
    parser.add_argument('-dpid', '--device-product-id', required=True, type=auto_int)
    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('-o', '--open-cashdrawer', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __VERSION__)
    parser.add_argument('receipt_xml', type=str)
    args = parser.parse_args()

    device = Usb(args.device_vendor_id, args.device_product_id)

    if args.open_cashdrawer:
        device.cashdraw(2)
        device.cashdraw(5)

    if args.receipt_xml:
        device.receipt(args.receipt_xml)


if __name__ == '__main__':
    """Standard import guard."""
    main()
