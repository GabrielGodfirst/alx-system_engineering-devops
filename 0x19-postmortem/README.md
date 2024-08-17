Postmortem Report: Wordpress PHP Support Issues on ubuntu 14


Issue  summary:
 Impact: Wordpress website downloaded files can not be debugged on ubuntu 14 machine.
 Root Cause: The root cause of the issue is that PHP is no longer supported and maintained on Ubuntu 14, which is an essential language used for building the web site.

Root Cause and Resolution:
 Root Cause: The WordPress running on a LAMP stack can not be debugged due to the ubuntu 14 machine the recommended machine is  failing to meet the installation criterias of Apache and Mysql client.PHP is no longer support on this machine and therefore having some missing dependencies failing to be properly installed on the machine.

Resolution: Apache and Mysql-client was successfully installed on an upgraded ubuntu machine, ubuntu 20 which accepts the installation with all dependencies supported to be able to debug the wordpress website.

Corrective and Preventative Measures:
 Improvements/Fixes: PHP is no longer supported on older versions of ubuntu machines, issues of missing dependencies  may affect the smooth process of debugging the wordpress website. Upgraded versions of the machine most especially Ubuntu 20 is well supported to run the debugging processes
![Example Image](images/post.png).
