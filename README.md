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

1, 2, 3: 
- En klass för ``Customer``. Klassen skall innehålla Namn, Email, Telefonnummer, Adress, Kön, Tidigare Erfarenhet. 
- En klass ``Expidition`` som innehåller pris, location, duration, Available Participants, date.
- En klass ``Calender Schedule`` som visar tillgängliga expeditioner på året. Den hämtar ``Expidition`` för att kunden skall kunna se tillgängliga events baserat spots till varje event, Är ett event fullt försvinner den från listan. Den har en metod ``Search_by_location(location)`` som tillåter användare filtrera mellan event baserat på ``Expidition(location``)
- En klass för registrering ``Registration`` som lagrar ``Customer`` ``Expidition`` och ``Gear``, samt en function som tillåter avbokning ``Unbooking`` som tar bort customer från registration och frigör eventuell gear. Vid bokning sker frågan vilken customer som skall vara ``Leader``, bockas inte den i på någon nekas bokningen. Användaren kan bocka i om utrsutning behöver hyras.
- En klass för ``Gear`` som har parametrar så som storlek och antal. Detta representerar utrustning, tex ``Flytväst``.
- En klass ``Gear_inventory`` som lagrar ``Gear`` i ett förråd. Om användaren bockat i att utrustning behöver hyras får de uppge sin vikt, sedan tillåter klassen kunder att hyra utrustning. Klassen hämtar tillgänglig utrustning från ``Gear_inventory`` som finns för varje event på calendern. Om de bokas tas de bort ur listan på det datumet.
- En klass för Betalning ``Payment``, denna skall innehålla en metod ``Is_payed`` som checkar om total kostnad från Registration har slutförts. Denna returnar true eller False. Om betalning är = True så lagras betalningsuppgifterna i ``Payment``.

# 2 Koda

