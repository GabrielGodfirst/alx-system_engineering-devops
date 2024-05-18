
Web Stack Outage

Issue Summary:

. Duration: The outage occurred from 10:00 AM to 12:00 PM (UTC), lasting for a total of 2 hours.
. Impact: The outage affected the availability of our main website, causing it to be completely inaccessible for users. 
Approximately 75% of our users were unable to access the website during this time, resulting in a significant loss of 
traffic and potential revenue.
. Root Cause: The root cause of the outage was identified as a misconfiguration in the load balancer settings, 
causing it to overload and fail to distribute traffic effectively.

Timeline:

->10:00 AM: The issue was detected when monitoring alerts indicated a sudden spike in server errors.
->10:05 AM: Engineers noticed the increased latency and errors while trying to access the website.
->10:10 AM: Initial investigation focused on server logs and network traffic to identify potential causes.
->10:30 AM: Assumptions were made that the issue might be related to database performance or a DDoS attack.
->10:45 AM: Further investigation revealed no anomalies in the database or signs of a DDoS attack.
->11:00 AM: The incident was escalated to the infrastructure team for additional support and expertise.
->11:30 AM: After thorough analysis,the misconfiguration in the load balancer settings was identified as the root cause.
->12:00 PM: The issue was resolved by reverting the load balancer configuration to its previous state.

Root Cause and Resolution:

. Cause: The misconfiguration in the load balancer settings resulted in uneven distribution of traffic among servers, 
leading to overload and service degradation.
. Resolution: The issue was fixed by reverting the load balancer configuration to its previous state, 
ensuring balanced traffic distribution and restoring service availability.
Corrective and Preventative Measures:

Improvements/Fixes:

. Implement automated configuration checks for load balancers to prevent similar misconfigurations in the future.
. Enhance monitoring and alerting systems to provide real-time visibility into load balancer performance and potential issues.

Tasks:

. Patch load balancer configuration scripts to enforce best practices and prevent manual errors.
. Conduct regular load testing and failover simulations to identify and address potential vulnerabilities in the infrastructure.
