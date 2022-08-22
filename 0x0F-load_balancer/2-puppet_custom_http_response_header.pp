# Server configuration with puppet
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}
file_line { 'default':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => "add_header X-Served-By ${HOSTNAME};}",
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
