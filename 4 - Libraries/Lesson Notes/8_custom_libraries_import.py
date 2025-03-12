import sys
test_import = __import__('8_custom_libraries_source')

if len(sys.argv) == 2:
    test_import.hello(sys.argv[1])

