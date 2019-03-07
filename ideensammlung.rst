Ideen nach ruecksprache mit Herr Seifert und Arbeitskollegen
============================================================

- Vergleich von TDD frameworks und deren schwierigkeit
- Ziel: Wie kann man moeglichst einfach TDD betreiben
- Problem: TDD ist sehr aufwendig

Neues Ziel:
###########

Frameworks vergleichen und aufzeigen mit welchem man am einfachsten Tests
schreibt. Die automation die dazu noetig ist soll natuerlich auch dazu gestellt
werden.

Die Automation sollte anhand von Travis CI gezeigt werden, da dies eine
einfache und kostenfreie Platform fuer open-source ist. Das format ist auch
sehr einfach weshalb man dort wenig zeitaufwand hat und sich mehr auf das
vergleichen konzentrieren kann.

Zur Automation gehoert:
- Automatischen testen vor/nach dem commit
- Tests muessen erfolgreich sein fuer einen Merge
- Pep-8 und weitere tools automatisch ausfuehren (wenn keine IDE genutzt)
- Automatischen deployen (docker, etc...). Sollte aber fuer die BA nicht noetig
  sein, da dies den Ramen sprengt

Ist die Automation "aufgebaut" kann man sich an die Testframeworks wagen und
diese Vergleichen (Unittest, etc..), dabei sollte auf Folgendes geachtet
werden:

- Standardlib (wieso ist es besser sachen aus der stdlib zu nehmen?)
- Wie werden Tests geschrieben?
- Gibt es Mocking/Fixtures?
- Wie komplex ist das testen mit dem Framework?

Ist der vergleich geschaffen kann man noch auf andere test Methoden eingehen
wie zum Beispiel das Property-based-testing (hypothesis) und welche vorteile
es bringt im TDD.

Zu allen Testframeworks sollte immer der selbe test code gschrieben werden um
einen besseren vergleich zu schaffen. Selbstverstaendlich sollte auch die
automation zum jeweiligen Framework angepasst werden.

Zu guter letzt sollte behandelt werden was an TDD gut ist und was nicht. Die
anforderungen an Entwickler und Arbeitgeber sind sehr hoch, da tests zuerst
schreiben sehr aufwending und auch langweilig sein kann. Hier koennte man zum
Beispiel disskutieren wie man dorrt etwas mehr motivation schafft.
