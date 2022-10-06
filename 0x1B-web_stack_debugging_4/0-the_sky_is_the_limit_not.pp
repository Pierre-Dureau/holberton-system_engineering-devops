# change the limit
exec {'change ulimit 15 to 15000':
  notify   => Service['nginx'],
  command  => 'sed -i s/15/15000/g /etc/default/nginx',
  provider => shell,
}
service {'nginx':
  ensure => 'running',
  enable => true,
}
