# Install Flask version 2.1.0 and Werkzeug version 2.1.1 using pip3

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0 Werkzeug==2.1.1',
}
