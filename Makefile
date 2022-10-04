all:
	make akce
	make sky_links
	make holidays
	make wander
	make company
	make communication
	make distribution
akce: src/akce.py
	@echo "python3 src/akce.py" > akce
	@chmod 777 akce

	
sky_links: src/sky_links.py
	@echo "python3 src/sky_links.py" > sky_links
	@chmod 777 sky_links

holidays: src/holidays.py
	@echo "python3 src/holidays.py" > holidays
	@chmod 777 holidays


wander: src/wander.py
	@echo "python3 src/wander.py" > wander
	@chmod 777 wander

company: src/company.py
	@echo "python3 src/company.py" > company
	@chmod 777 company

communication: src/communication.py
	@echo "python3 src/communication.py" > communication
	@chmod 777 communication

distribution: src/distribution.py
	@echo "python3 src/distribution.py" > distribution
	@chmod 777 distribution

