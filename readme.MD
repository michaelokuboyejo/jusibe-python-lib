###jusibe-python-lib

[![Build Status](https://travis-ci.org/michaelokuboyejo/jusibe-python-lib.svg?branch=master)](https://travis-ci.org/michaelokuboyejo/jusibe-python-lib)

Unofficial modular Python Library for the (Jusibe SMS HTTP API) <https://jusibe.com>



Quick Start
-------------

The first thing you'll need to do is `sign up on Jusibe and get your 
<https://jusibe.com>`_.

Installation
------------

`jusibe` is available on `PYPI <https://pypi.python.org/pypi/jusibe/>`_.
Install with ``pip``:

.. code:: bash

    pip install jusibe


The library is currently tested against Python versions 2.6.9, 2.7.9

#####Usage
________

.. code:: python 
	
	import Jusibe
	
	public_key = 'python_public_key_here' #change this
	access_token = 'access_token__here' #change this
	jusibe = Jusibe(public_key, access_token)
	
	#send SMS
	response = jusibe.send_message('234812345678', 'sender, 'message to send')
	print response
	
	#check available credit
	available_credit = jusibe.check_available_credit()
	print available_credit


## Contributing

Please feel free to fork this package and contribute by submitting a pull request to enhance the functionalities.


## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
