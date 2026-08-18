# Modellering - Diskutera i grupp

 **Tänk er en dykarklubb som anordnar utfärder under sommarhalvåret. De har en webbsida där man kan läsa om klubben, men nu vill de lägga till möjlighet att anmäla sig till dykutflykterna.**
- klubben behöver spara kontaktuppgifter till de som anmäler sig
- när man har betalt en avgift ska det också registreras
- man ska kunna hyra utrustning, eller ta med sig egen
- klubbens utrustning består av exempelvis våtdräkter och syrgastuber, men man har ett begränsat sortiment
- man kan avboka sig
- varje utflykt äger rum på en specifik dag och plats
- intresserade ska kunna söka efter utflykter baserat på plats
- en person måste vara ledare med huvudansvar för varje utflykt

Er uppgift:
1. ge ett förslag på vilka klasser som behöver finnas
2. ta fram vilka egenskaper och metoder klasserna behöver ha
3. redogör för vilka parametrar och returvärden metoderna behöver

1: 
- En klass för ``Assignee``. Klassen skall innehålla Namn, Email, Telefonnummer, Adress, Kön, Tidigare Erfarenhet. 
- En klass ``Expidition`` som innehåller location, duration, Available Participants, date, Spots.
- En klass ``Calender Schedule`` som visar tillgängliga expeditioner på året. Den hämtar ``Expidition`` för att kunden skall kunna se tillgängliga events baserat spots till varje event, Är ett event fullt försvinner den från listan. Den har en metod ``Search_by_location(location)`` som tillåter användare filtrera mellan event baserat på ``Expidition(location``)
- En klass för registrering ``Registration`` som lagrar assignees som ``New_customer`` samt en function som tillåter avbokning ``Unregistered`` som tar bort Assignees från registration.
- En klass för ``Gear`` som innehåller en uppsättning av tillgänglig utrustning.
- En klass för ``Gear_Rental`` Användaren få uppge sin vikt, sedan tillåter klassen kunder att hyra utrustning. Klassen hämtar tillgänglig utrustning från ``Gear`` Klassen och om de bokas tas de bort ur listan på det datumet.
- En klass för Betalning ``Payment``, denna skall innehålla en metod som checka om betalning har gjorts, som true eller false.