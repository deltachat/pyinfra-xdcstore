# pyinfra module to deploy xdcstore and xdcget

This module deploys
[xdcstore](https://codeberg.com/webxdc/xdcstore)
and [xdcget](https://codeberg.com/webxdc/xdcget).


It can be used from the Python code like this:
```python
from pyinfra_xdcstore import deploy_xdcstore

deploy_xdcstore()
```

It can also be used to deploy xdcstore and xdcget with an ad-hoc command like this:
```
XDCSTORE_PASSWORD=p4ssw0rd XDCSTORE_EMAIL=admin@example.org pyinfra --ssh-user root -- example.org pyinfra_xdcstore.deploy_xdcstore
```

