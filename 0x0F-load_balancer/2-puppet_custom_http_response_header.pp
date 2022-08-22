# Server configuration with puppet
# an new ubuntu machine

exec { 'update':
  command => '/usr/bin/apt-get update',
}
package { 'nginx':
  ensure  => 'present',
  name    => 'nginx',
  require => Exec['update'],
}
file_line { 'default':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By $hostname;}',
  require => Package['nginx'],
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
