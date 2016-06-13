import logging
from datetime import datetime

SEVERITY = {
  logging.DEBUG: 'debug',
  logging.INFO: 'info',
  logging.WARNING: 'warning',
  logging.ERROR: 'error',
  logging.CRITICAL: 'critical',
}
print(SEVERITY)

SEVERITY.update((name, name) for name in SEVERITY.values())
#
#SEVERITY.update([('xxxx', 'yyyy'), ('111', 222)])
#
#print(SEVERITY)

#print(str(SEVERITY.get(11, 10)))

print(datetime.utcnow())
now = datetime.utcnow().timetuple()
print(now);
print(*now);
print(now[:4]);
print(datetime(*now[:4]))
