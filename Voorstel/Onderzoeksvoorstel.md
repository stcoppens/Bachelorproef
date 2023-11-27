# Scripting voor Netwerkoptimalisatie: DNS en DHCP Beheer met Python-scripts en IP Address Management Integratie

## 1. Abstract
Deze bachelorproef richt zich op het ontwikkelen van een innovatieve benadering voor netwerkbeheer door middel van Python-scripts. 
Het hoofddoel is het creëren van een abstractielaag boven een bestaande netwerkbeheer tool voor DNS en DHCP, 
waarbij de API van een IP Address Management (IPAM)-tool wordt aangestuurd. 
Deze abstractielaag maakt interactie met de IPAM-tool mogelijk via Python-scripts en wordt geoptimaliseerd door API-aanroepen vanuit een intuïtief webportaal. 
Het doel is om de complexiteit van het handmatig beheren van netwerkconfiguraties, inclusief IP-adresallocatie, te verminderen, waardoor efficiëntie en gebruiksvriendelijkheid worden verbeterd.

## 2. Inleiding
Internet Protocol (IP) is het fundament van elk gestructureerd, goed functionerend en veilig netwerk. Het geeft de mogelijkheid efficiënt gegevens te routeren, netwerken te verdelen in meer beheersbare eenheden, toegang te beperken tot gevoelige data of systemen, services te identificeren en het oplossen van netwerkproblemen [RFC791](https://www.rfc-editor.org/rfc/rfc791). Dit hoofdstuk legt de basis van uit voor het beheren van IP netwerken. **ja, maar wat is het precies? Een systeem? Een pot choco?**

**onder je inleiding vallen nu een aantal titels, maar de samenhang tussen 2.1 en 2.2 is mij bvb. niet duidelijk. Je kan hier mss een leeswijzer maken waar je de samenhang uitlegt**

### 2.1 Veelgebruikte protocols
Binnen het domein van IT Netwerkbeheer zijn er twee kritische protocols: 
- **Domain Name System (DNS)**: Dit is een systeem **(systeem? Of protocol? want hier net voor zeg je dat je twee protocols gaat opnoemen?)** die onder andere vertalingen voorziet tussen domeinnamen en IP adressen [RFC1034](https://www.rfc-editor.org/rfc/rfc1034). Als voorbeeld kan je via de browser naar google surfen via het IP adres 142.251.36.35 of via www.google.be. **NOg duidelijk maken dat google de domeinnaam is)=**
- **Dynamic Host Configuration Protocol (DHCP)**: Dit protocol voorziet een framework voor het doorgeven van configuratie informatie naar hosts (lees: computers) op het netwerk [RFC2131](https://datatracker.ietf.org/doc/html/rfc2131). Zo kan een computer bijvoorbeeld een IP adres ontvangen waarmee die kan communiceren binnen het netwerk waarop die is aangesloten.
  
#### 2.1.1 DNS
DNS voorziet meerdere types resource records die netwerkbeheerders kunnen meegeven: **moet je uitleggen wat resource records zijn?**
  - **A**: Dit beschrijft een host adres. Vb. "server1.voorbeeld.com IN A 192.168.1.1" maakt de vertaling zodat het toestel met de naam server1.voorbeeld.com bereikbaar is zowel via het IP adres 192.168.1.1 als via de naam. **naam? domeinnaam?*
  - **CNAME**: Dit beschrijft de kanonieke naam van een host, het wordt gebruikt om een alias of subdomein naar het hoofddomein door te verwijzen. Vb. "www.voorbeeld.com. IN CNAME server1.voorbeeld.com" zorgt dat server1 ook bereikbaar is via "www.voorbeeld.com".
  - **MX**: Dit is een *mail exchange* record en wordt gebruikt om aan te geven welke mailservers verantwoordelijk zijn voor het ontvangen van mails binnen een domein. vb. "voorbeeld.com. IN MX 10 mailserver.voorbeeld.com" geeft de DNS server mee welke server de mailserver is.
  - **NS**: Dit is een *name server* record, het beschrijft welke DNS servers verantwoordelijk zijn voor het beheren van DNS informatie voor een domein. Vb. "voorbeeld.com IN NS dns1.voorbeeld.com" verwijst naar dns1 als DNS server voor het domein voorbeeld.com.
  - **PTR**: Dit is een *Pointer* record, het wordt gebruikt om via IP een vertaling te vragen aan de DNS server in plaats van via de naam.
  - **SOA**: Dit is een *Start of Authority* record die belangrijke informatie bevat over de zone, zoals welke de primaire DNS server, contactpersonen, etc.
[RFC1034](https://www.rfc-editor.org/rfc/rfc1034)

#### 2.1.2 DHCP
IP netwerken worden door netwerkbeheerders op een logische manier opgesplitst in subnetwerken. Hierbij worden de beschikbare IP adressen verdeeld in sub-netwerken (subnet). Toestellen binnen subnet A zullen elkaar kunnen bereiken terwijl een toestel in een subnet B zonder de nodige routering geen verbinding zal kunnen maken met de toestellen in subnet A.
Voor DHCP zullen netwerkbeheerders subnets (of pools van IP adressen) aanbieden aan de DHCP server. De DHCP server uit deze pools (onder andere) IP adressen uitdelen aan toestellen die verbinden op het netwerk en daarbij de DHCP server laten weten dat ze nog geen IP adres hebben.
DHCP beschrijft 3 mechanismes voor het uitdelen van IP adressen:
- **Automatisch toewijzen**: Permanent toewijzen van een IP adres.
- **Dynamisch toewijzen**: IP adres voor een bepaalde tijd toewijzen.
- **Manueel toewijzen**: Een (door de netwerkbeheerder) vooraf bepaald IP adres toewijzen, in vakjargon noemt met dit een IP reservatie.
[RFC2131](https://datatracker.ietf.org/doc/html/rfc2131)

#### 2.2 IPAM
Naast de vele uitdagingen die zowel DNS als DHCP met zich meebrengen is het beheren van de vele DNS records, IP adres ranges en de vaak vele IP reservaties zeker iets waar een netwerkbeheerder over moet waken. 
Een mogelijke oplossing hiervoor is het gebruiken van IP Address Management (IPAM), IPAM laat toe het beheer van deze middelen te automatiseren. ** Wat is IPAM precies? Ging je dit nog uitschrijven?**

## 3. Probleemstelling
Deze bachelorproef zal plaatsvinden **uitgevoerd worden?** bij Universiteit Gent (UGent) **departement?**. Momenteel werkt UGent met scripts die op basis van zo genaamde subnetbestanden de nodige acties uitvoeren op de DHCP en DNS servers. 
Deze subnetbestanden stellen elk 1 subnet voor en beschrijven cruciale informatie zoals DNS servers, welk *Virtual Local Area Network* (VLAN) nummer, gateway, etc. Hiernaast bevatten deze ook alle beschikbare, vrije, IP adressen als alle gereserveerde adressen met daarbij eventueel enkele regels voor DNS en beveiliging.
Voor elke IP reservatie die moet gebeuren krijgt het netwerk team van interne UGent personeel een mail met daarin de nodige hostinformatie die ze in het daarvoor bestemde subnetbestand plakken. Indien hier nog extra DNS of beveiligingsregels bij horen, moet de netwerkbeheerder deze er zelf nog bijschrijven.
Het overzicht van de beschikbare IP ranges is beschreven in een intern wikipediapagina met daarbij de beschrijving van elke range.

Universiteit Gent is stappen aan het ondernemen voor het implementeren van Efficiënt IP (EP), een IPAM-softwarepakket, in hun opzet. **Hier de zin zetten van dat men naar IPAM zal gaan**
**Hier ook nog de bijhorende uitdagingen van deze aanpak beschrijven**

## 4. Doelstelling van de Bachelorproef
Deze bachelorproef zal een abstractielaag maken boven EP waarbij python scripts via de API van EP commando's zullen uitvoeren op EP.
** Wat je hieronder zet is wat extra toelichting en heel specifiek met voorbeelden, maar ik mis zo nog een algemene doelstelling, die wat ruimer beschreven is. HEb het gevoel dat het onderstaande eerder hoort bij probleemstelling, als je ze zou herschrijven als noden van de UGent. Of je benoemt deze in je discussie als allemaal voordelen.**
**of: nog beter: je stelt deze op als indicatoren (tijdbesparing, schaalbaarheid, consistentie,...) en je gaat na in je evaluatie of deze verbeterd zijn? Of is dat niet haalbaar en te veel voor een BP?**
Op deze manier kunnen bijvoorbeeld de aanvragers van IP reservaties zelf alle nodige informatie ingeven via een webportaal die de abstractielaag zal aansturen.
De netwerkbeheerders zullen deze aanvragen dan in een overzicht kunnen nakijken en al dan niet goedkeuren.
Deze abstractielaag en het implementeren van IPAM heeft meerdere voordelen zoals tijdbesparing, schaalbaarheid van het netwerk, consistentie van IP gegevens, terugvinden van wijzigingen en andere. 

## 5. Methode


