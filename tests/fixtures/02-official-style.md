Memorandum: Q3 incident review

An evaluation of the incident that occurred on 14 August was conducted by the platform team in accordance with the procedure that was established following the prior outage. The determination was made that the root cause was the absence of a timeout configuration on the upstream connection pool, the introduction of which had been deferred pending the completion of the migration.

It is important to note that the implementation of the fix, which had been under consideration since the second quarter and which required the coordination of three teams across two time zones, was completed on 21 August.

Recommendations for the prevention of recurrence are as follows. The addition of timeout configuration to all connection pools should be undertaken. A review of the deferral process should be performed by engineering management. Consideration should be given to the establishment of an ownership model for shared infrastructure components.

It should be mentioned that no customer data was affected.
