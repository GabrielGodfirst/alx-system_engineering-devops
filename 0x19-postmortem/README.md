![Example Image](images/post.png).

Postmortem Report: Wordpress PHP Support Issues on ubuntu 14


Issue  summary:
Duration of the Outage: The outage lasted for approximately 4 hours, starting at 08:00 AM UTC and ending at 12:00 PM UTC on August 16, 2024.

Impact: The WordPress website was completely inaccessible to all users. During this period, 100% of users were unable to access the website, resulting in significant downtime for our web services.

Root Cause: The root cause of the issue was an outdated PHP version installed on the Ubuntu 14.04 LTS server. This version was no longer supported, causing PHP processes to fail, and ultimately, the WordPress website was unable to function

Timeline:

08:00 AM UTC: The issue was detected through monitoring alerts indicating that the website was down.

08:05 AM UTC: An engineer confirmed the downtime and began investigating the issue.

08:15 AM UTC: Initial assumptions focused on a potential network issue or server overload.

08:30 AM UTC: Misleading investigations included restarting the Apache server and checking MySQL database integrity, both of which did not resolve the issue.

09:00 AM UTC: The issue was escalated to the DevOps team for further analysis.

09:30 AM UTC: The root cause was identified as an unsupported PHP version that had become incompatible with the current WordPress installation.

10:00 AM UTC: The decision was made to update PHP to a supported version.

11:30 AM UTC: PHP was successfully updated and reconfigured.

12:00 PM UTC: The website was fully restored, and normal operations resumed.

Root Cause and Resolution:

 Root Cause: The WordPress running on a LAMP stack can not be debugged due to the ubuntu 14 machine the recommended machine is  failing to meet the installation criterias of Apache and Mysql client.PHP is no longer support on this machine and therefore having some missing dependencies failing to be properly installed on the machine.

Resolution: Apache and Mysql-client was successfully installed on an upgraded ubuntu machine, ubuntu 20 which accepts the installation with all dependencies supported to be able to debug the wordpress website.

Corrective and Preventative Measures:

 Improvements/Fixes: PHP is no longer supported on older versions of ubuntu machines, issues of missing dependencies  may affect the smooth process of debugging the wordpress website. Upgraded versions of the machine most especially Ubuntu 20 is well supported to run the debugging processes

Tasks to Address the Issue:

Update PHP: Upgrade PHP on all servers running outdated versions to ensure compatibility with current applications.

Implement Monitoring: Add monitoring for PHP versions and lifecycle status to receive alerts before they become unsupported.

Review Update Procedures: Review and enhance the update procedures for all server software to include regular checks for end-of-life software.
