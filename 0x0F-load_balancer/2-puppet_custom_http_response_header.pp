# Server configuration with puppet
exec { 'update':
  command => '/usr/bin/apt-get update',
}
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
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
