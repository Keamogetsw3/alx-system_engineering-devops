# Postmortem: Wordpress 500 Error Due to PHP Configuration Issue
## Issue Summary

### Duration:
The outage lasted for 2 hours and 30 minutes, from 6:00 AM to 3:30 PM +2 UTC on August 13, 2024.

### Impact:
The Wordpress website hosted on a LAMP stack returned a 500 Internal Server Error for all requests. This impacted 100% of users, making the site completely inaccessible.

### Root Cause:
The issue was caused by an incorrect PHP extension reference in the wp-settings.php file.

### Timeline
6:00 am - issue detected

6:05 am - Initial investigation revealed that Apache was returning a 500 error

7:00 am - tmux was installed

7:10 am  - found the process ID (PID) of Apache

7:30 am - used  tmux to run strace in one window and curl in another one

O8:00 am - Analyze the strace output

10:00 am - 3:30 pm - trouble shooting and automating a fix with puppet 
