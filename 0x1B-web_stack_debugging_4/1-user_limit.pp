# change the limit for a user
exec {'hard limit':
  command  => 'sed -i s/5/10000/g /etc/security/limits.conf',
  provider => shell,
}
exec {'soft limit':
  command  => 'sed -i s/4/10000/g /etc/security/limits.conf',
  provider => shell,
}
