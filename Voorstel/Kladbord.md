# Titel
Scripting voor Netwerkoptimalisatie: DNS en DHCP Beheer met Python-scripts en IP Address Management Integratie

## Titel voorstellen
- "Netwerkbeheer in Python: IPAM-gedreven Abstractielaag voor DNS en DHCP via Web-API Interactie"
- "Scripting voor Netwerkoptimalisatie: DNS en DHCP Beheer met Python-scripts en IP Address Management Integratie"
- "De Kloof Dichten: Python-scriptgestuurde IPAM Integratie voor Naadloos Beheer van DNS en DHCP via Web Portals"
- "Netwerken Versterken: Synergie tussen Python-scripts en IPAM voor Intuïtief Beheer van DNS en DHCP via Web Interfaces"
- "Voorbij Handmatig: Python-gestuurde IPAM voor Webgebaseerd Beheer van DNS en DHCP"

## Abstract
Deze bachelorproef richt zich op het ontwikkelen van een innovatieve benadering voor netwerkbeheer door middel van Python-scripts. 
Het hoofddoel is het creëren van een abstractielaag boven een bestaande netwerkbeheer tool voor DNS en DHCP, 
waarbij de API van een IP Address Management (IPAM)-tool wordt aangestuurd. 
Deze abstractielaag maakt interactie met de IPAM-tool mogelijk via Python-scripts en wordt geoptimaliseerd door API-aanroepen vanuit een intuïtief webportaal. 
Het doel is om de complexiteit van het handmatig beheren van netwerkconfiguraties, inclusief IP-adresallocatie, te verminderen, waardoor efficiëntie en gebruiksvriendelijkheid worden verbeterd.

## Tools
- Efficient IP: IPAM tool
- Visual Studio Code: Schrijven van code
- Postman: Testen van code
- Python3: Taal waarin code zal worden geschreven

## Probleemstelling
Het handmatig beheren van netwerkconfiguraties vertoont verschillende tekortkomingen, 
zoals foutgevoeligheid, tijdrovendheid, schaalbaarheidsproblemen, inconsistentie, 
moeilijk te traceren wijzigingen en beveiligingsrisico's.

## Bestaande netwerkbeheer tool
Momenteel wordt er gewerkt met zelfgeschreven scripts die informatie over reservaties en subnetten bijhouden in bestanden. 
Deze aanpak is gevoelig voor wijzigingen en bemoeilijkt de uitbreidbaarheid van de omgeving.

## IP Address Management (IPAM)-tool
Efficient IP wordt gebruikt als IPAM-tool vanwege de functionaliteiten die aansluiten bij de eisen van de netwerkomgeving.

## Abstractielaag en Python-scripts:
Nog in te vullen

## Webportaal en API-optimalisatie
Het webportaal is bedoeld voor technisch personeel en prioriteert functionaliteit boven esthetiek. 
Functionaliteiten omvatten IP-adresbeheer, zoekfunctionaliteit, rapportage, gebruikersbeheer en integratie met andere tools.

## Complexiteit vermindering
De benadering zal complexiteit verminderen door automatisering van het goedkeuringsproces voor wijzigingen en het aanbieden van een overzicht van beschikbare subnetten aan aanvragers.

## Tools en technologieën
De ontwikkeling zal voornamelijk plaatsvinden in Python, gebruikmakend van JSON en Postman voor API-tests. 
Scripts worden mogelijk uitgevoerd in virtuele containers die wachten op triggers vanuit het webportaal.

## Tijdlijn tussen maart en mei 2024
Het ontwikkelingsproces strekt zich uit tussen maart en mei 2024, 
waarbij de focus ligt op het opleveren van een eerste versie van het webportaal met de meest kritische functies.

## Nuttige info:
Belangrijk om te weten:
Er zijn 2 kritische protocols binnen netwerkbeheer: 
- DNS (woordenboekservice die vertaling doet van domeinnaam naar IP adres (google.be <> 8.8.8.8)
- DHCP (automatisch uitdelen van beschikbare IP adressen aan hosts binnen het domein)
Hosts kunnen IP adressen reserveren in DHCP en daarbij ook een alias (DNS Record) krijgen.
Dat brengt enkele uitdagingen met zich mee waarvan een van de grootste het beheer is van de beschikbare en gereserveerde IP adressen.
Een oplossing daarvoor is het gebruik van IPAM, IP address mgmt, die geeft de optie het te automatiseren.
Momenteel gebruikt UGent een systeem waarbij ze alle IP reservaties en alle vrije IP adressen registeren in meerdere bestanden met daarin nog een hele hoop belangrijke informatie.
We gaan naar een IPAM tool migreren, ik heb daar ondertussen al enkele scripts voor geschreven voor de migratie te vergemakkelijken en tussenstadia te overbruggen.
Daarnaast is nog belangrijk om te weten dat API een interface is waarop software kan communiceren met andere software.
Het doel is om volledig op die IPAM tool te zitten, wat mijn doel is voor men bachelorproef;
Ik wil een webportaal maken die meerdere scripts activeren die ik zou schrijven in men BP. 
Die scripts communiceren dan met de API van de IPAM tool en doen het nodige om op een vrij automatische, uniforme manier het netwerk te beheren. 
Uiteindelijk is het de bedoeling dat bijna niemand nog in het IPAM tool zou moeten komen.