# -*- coding: utf-8 -*-

def get_options():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-n", "--number", type="int", default=3, help="Number of resources.")
    parser.add_option("-p", "--port", type="int", default=5000, help="Web service port.")
    return parser.parse_args()[0].__dict__