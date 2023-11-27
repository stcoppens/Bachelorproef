# Scripting voor Netwerkoptimalisatie: DNS en DHCP Beheer met Python-scripts en IP Address Management Integratie

## 1. Abstract
Deze bachelorproef richt zich op het ontwikkelen van een innovatieve benadering voor netwerkbeheer door middel van Python-scripts. 
Het hoofddoel is het creëren van een abstractielaag boven een bestaande netwerkbeheer tool voor DNS en DHCP, 
waarbij de API van een IP Address Management (IPAM)-tool wordt aangestuurd. 
Deze abstractielaag maakt interactie met de IPAM-tool mogelijk via Python-scripts en wordt geoptimaliseerd door API-aanroepen vanuit een intuïtief webportaal. 
Het doel is om de complexiteit van het handmatig beheren van netwerkconfiguraties, inclusief IP-adresallocatie, te verminderen, waardoor efficiëntie en gebruiksvriendelijkheid worden verbeterd.

## 2. Inleiding
Internet Protocol (IP) is het fundament van elk gestructureerd, goed functionerend en veilig netwerk. Het geeft de mogelijkheid efficiënt gegevens te routeren, netwerken te verdelen in meer beheersbare eenheden, toegang te beperken tot gevoelige data of systemen, services te identificeren en het oplossen van netwerkproblemen [RFC791](https://www.rfc-editor.org/rfc/rfc791). Dit hoofdstuk legt de basis van uit voor het beheren van IP netwerken.

### 2.1 Veelgebruikte protocols
Binnen het domein van IT Netwerkbeheer zijn er twee kritische protocols: 
    - **Domain Name System (DNS)**: Dit is een systeem die onder andere vertalingen voorziet tussen domeinnamen en IP adressen [RFC1034](https://www.rfc-editor.org/rfc/rfc1034). Als voorbeeld kan je via de browser naar google surfen via het IP adres 142.251.36.35 of via www.google.be. 
    - **Dynamic Host Configuration Protocol (DHCP)**: Dit protocol voorziet een framework voor het doorgeven van configuratie informatie naar hosts (lees: computers) op het netwerk [RFC2131](https://datatracker.ietf.org/doc/html/rfc2131). Zo kan een computer bijvoorbeeld een IP adres ontvangen waarmee die kan communiceren binnen het netwerk waarop die is aangesloten.

#### 2.1.1 DNS
DNS voorziet meerdere types resource records die netwerkbeheerders kunnen meegeven:
    - A: Dit beschrijft een host adres. Vb. "server1.voorbeeld.com IN A 192.168.1.1" maakt de vertaling zodat het toestel met de naam server1.voorbeeld.com bereikbaar is zowel via het IP adres 192.168.1.1 als via de naam.
    - CNAME: Dit beschrijft de kanonieke naam van een host, het wordt gebruikt om een alias of subdomein naar het hoofddomein door te verwijzen. Vb. "www.voorbeeld.com. IN CNAME server1.voorbeeld.com" zorgt dat server1 ook bereikbaar is via "www.voorbeeld.com".
    - MX: Dit is een *mail exchange* record en wordt gebruikt om aan te geven welke mailservers verantwoordelijk zijn voor het ontvangen van mails binnen een domein. vb. "voorbeeld.com. IN MX 10 mailserver.voorbeeld.com" geeft de DNS server mee welke server de mailserver is.
    - NS: Dit is een *name server* record, het beschrijft welke DNS servers verantwoordleijk zijn voor het beheren van DNS informatie voor een domein. Vb. "voorbeeld.com IN NS dns1.voorbeeld.com" verwijst naar dns1 als DNS server voor het domein voorbeeld.com.
    - PTR: Dit is een *Pointer* record, het wordt gebruikt om via IP een vertaling te vragen aan de DNS server in plaats van via de naam.
    - SOA: Dit is een *Start of Authority* record die belangrijke informatie bevat over de zone, zoals welke de primaire DNS server, contactpersonen, etc.
[RFC1034](https://www.rfc-editor.org/rfc/rfc1034)

#### 2.1.2 DHCP
IP netwerken worden door netwerkbeheerders op een logische manier opgesplitst in subnetwerken. Hierbij worden de beschikbare IP adressen verdeelt in sub-netwerken (subnet). Toestellen binnen subnet A zullen elkaar kunnen bereiken terwijl een toestel in een subnet B zonder de nodige routering geen verbinding zal kunnen maken met de toestellen in subnet A.
Voor DHCP zullen netwerkbeheerders subnets (of pools van IP adressen) aanbieden aan de DHCP server. De DHCP server uit deze pools (onder andere) IP adressen uitdelen aan toestellen die verbinden op het netwerk en daarbij de DHCP server laten weten dat ze nog geen IP adres hebben.
DHCP beschrijft 3 mechanismes voor het uitdelen van IP adressen:
    - Automatisch toewijzen: Permanent toewijzen van een IP adres.
    - Dynamisch toewijzen: IP adres voor een bepaalde tijd toewijzen.
    - Manueel toewijzen: Een (door de netwerkbeheerder) vooraf bepaald IP adres toewijzen, in vakjargon noemt met dit een IP reservatie.
[RFC2131](https://datatracker.ietf.org/doc/html/rfc2131)

#### 2.2 IPAM
Naast de vele uitdagingen die zowel DNS als DHCP met zich meebrengen is het beheren van de vele DNS records, IP adres ranges en de vaak vele IP reservaties zeker iets waar een netwerkbeheerder over moet waken. 
Een mogelijke oplossing hiervoor is het gebruiken van IP Address Management (IPAM), IPAM laat toe het beheer van deze middelen te automatiseren.

## 3. Probleemstelling
Deze bachelorproef zal plaatsvinden bij Universiteit Gent waarbij de omschakeling naar IPAM gemaakt zal worden. Momenteel werkt UGent met scripts die op basis van zo genaamde subnetbestanden de nodige acties uitvoeren op de DHCP en DNS servers.
Deze subnetbestanden stellen elk 1 subnet voor en beschrijven cruciale informatie zoals DNS servers, welk *Virtual Local Area Network* (VLAN) nummer, gateway, etc. Hiernaast bevatten deze ook alle beschikbare, vrije, IP adressen als alle gereserveerde adressen met daarbij eventueel enkele regels voor DNS en beveiliging.
Voor elke IP reservatie die moet gebeuren krijgt het netwerk team van interne UGent personeel een mail met daarin de nodige hostinformatie die ze in het daarvoor bestemde subnetbestand plakken. Indien hier nog extra DNS of beveiligingsregels bij horen moet de netwerkbeheerder deze er zelf nog bijschrijven.
Het overzicht van de beschikbare IP ranges is beschreven in een intern wikipediapagina met daarbij de beschrijving van elke range.

## 4. Doelstelling van de Bachelorproef
Universiteit Gent is stappen aan het ondernemen voor het implementeren van Efficiënt IP (EP), een IPAM-softwarepakket, in hun opzet.
Deze bachelorproef zal een abstractielaag maken boven EP waarbij python scripts via de API van EP commando's zullen uitvoeren op EP.
Op deze manier kunnen bijvoorbeeld de aanvragers van IP reservaties zelf alle nodige informatie ingeven via een webportaal die de abstractielaag zal aansturen.
De netwerkbeheerders zullen deze aanvragen dan in een overzicht kunnen nakijken en al dan niet goedkeuren.
Deze abstractielaag en het implementeren van IPAM heeft meerdere voordelen zoals tijdbesparing, schaalbaarheid van het netwerk, consistentie van IP gegevens, terugvinden van wijzigingen en andere.

## 5. Methode



Doelstelling van de BP
- UGent als voorbeeld waar bovengeschreven uitdagingen zichtbaar zijn
- Context/uitvoeringsplaats van de BP in UGent -> beschrijven van de IPAM tool van UGent
- Zo toewerken naar je doel: scripts ontwikkelen

Methode
- tools beschrijven
- stappen:
-   0) selectie onderdelen van de IPAM die geautomatiseerd zullen worden
    1) ontwikkelen van de scripts
    2) Evaluatie/validatie/whatever fancy term dat je eraan wilt geven: testing en foutjes opsporen
 
Eventueel nog figuur van die drie lagen, dat je ook visueel ziet waar jouw rol zit (die scripts in Python)


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



## Nota's Lien

Inleiding
- DNS
- DACP
- IPAM
- Uitdagingen als netwerkbeheerder (belang benadrukken zoals je eerder hebt gedaan, maar nog meer  rond hangen)

Doelstelling van de BP
- UGent als voorbeeld waar bovengeschreven uitdagingen zichtbaar zijn
- Context/uitvoeringsplaats van de BP in UGent -> beschrijven van de IPAM tool van UGent
- Zo toewerken naar je doel: scripts ontwikkelen

Methode
- tools beschrijven
- stappen:
-   0) selectie onderdelen van de IPAM die geautomatiseerd zullen worden
    1) ontwikkelen van de scripts
    2) Evaluatie/validatie/whatever fancy term dat je eraan wilt geven: testing en foutjes opsporen
 
Eventueel nog figuur van die drie lagen, dat je ook visueel ziet waar jouw rol zit (die scripts in Python)
  