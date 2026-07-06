# Svolgimenti — Prova scritta Profilo C (Assistente ICT)
### Risposte-modello ai sei temi · Banca d'Italia 2026 (programma di pag. 11)

> Ogni svolgimento segue la struttura attesa: **impostazione → sviluppo tecnico con specifiche concrete → esempio nel contesto Banca d'Italia → rischi residui** (metodo PEEL). Taglio Profilo C: fondamenti applicati, lessico corretto, scelte motivate.

---
---

# AMBITO 1 — Progettazione e sviluppo del software

## Svolgimento Tema 1.1 — Algoritmi e strutture dati per la riconciliazione di transazioni

**Impostazione.** Il problema richiede tre operazioni su un grande volume di record: individuare i duplicati, ordinare per timbro temporale, ricercare per identificatore. La scelta delle **strutture dati** determina l'efficienza dell'intero sistema: con milioni di record, la differenza tra un'operazione O(n²) e una O(n log n) è la differenza tra un sistema usabile e uno che blocca le elaborazioni.

**(a) Strutture dati.** Per **ricerca e deduplica** la struttura naturale è la **tabella hash**: l'identificatore della transazione è la chiave, e l'inserimento/ricerca avviene in tempo **O(1) nel caso medio**. Inserendo i record in una hash table, un duplicato si rileva immediatamente perché la chiave è già presente. Per il mantenimento dei dati **ordinati** uso un **array ordinato** (efficiente in lettura/ricerca binaria) o, se servono inserimenti frequenti mantenendo l'ordine, un **albero bilanciato** (es. albero di ricerca, operazioni in O(log n)). La lista concatenata è scartata per la ricerca (scorrimento O(n)), ma è utile per gestire le collisioni nella hash table (concatenamento).

**(b) Algoritmi e complessità.** *Ordinamento*: il **merge sort** garantisce **O(n log n)** in ogni caso ed è **stabile** (mantiene l'ordine relativo dei record con uguale chiave), proprietà utile nella riconciliazione; il **quick sort** è O(n log n) nel caso medio ma degrada a **O(n²)** nel caso pessimo (pivot sbilanciato). Preferisco merge sort quando serve un limite garantito. *Ricerca*: su dati ordinati la **ricerca binaria** opera in **O(log n)**; tramite hash table la ricerca puntuale è **O(1)** nel caso medio, **O(n)** nel caso pessimo (molte collisioni). *Spazio*: la hash table richiede memoria aggiuntiva — è un classico **trade-off tempo/memoria**.

**(c) Trade-off e scalabilità.** La hash table compra velocità con occupazione di memoria e con il rischio di degenerazione in caso di funzione hash mal distribuita. L'array ordinato è parco di memoria ma costoso negli inserimenti (O(n) per mantenere l'ordine). Al crescere dei dati, la scelta corretta delle strutture è ciò che permette al sistema di **scalare linearmente** anziché esplodere.

**(d) Trattabilità (P/NP).** Non tutti i problemi ammettono soluzioni efficienti: la classe **P** raccoglie i problemi risolvibili in tempo polinomiale, la classe **NP** quelli la cui soluzione è verificabile in tempo polinomiale. Per i problemi **NP-difficili** non si conoscono algoritmi efficienti: nella pratica si ricorre a euristiche e approssimazioni. Sapere riconoscere quando un problema è intrattabile evita di cercare soluzioni esatte impossibili da calcolare in tempi utili.

**Esempio nel contesto.** Un sistema bancario che processa transazioni 24 ore su 24 deve riconciliare volumi enormi: l'uso di hash table per la deduplica e di ordinamenti O(n log n) è ciò che rende l'elaborazione completabile nelle finestre operative.

**Rischi residui.** (1) **Collisioni hash** e cattiva distribuzione → degenerazione a O(n). (2) **Consumo di memoria** con dataset molto grandi. (3) **Data skew** (chiavi sbilanciate) che peggiora il caso pessimo. (4) Necessità di gestire dati che non entrano in memoria (algoritmi *external sorting*).

---

## Svolgimento Tema 1.2 — Secure SDLC e OWASP per un'applicazione web

**Impostazione.** La sicurezza non può essere "aggiunta alla fine": per un'applicazione web che gestisce autenticazione e dati sensibili dei clienti, deve essere incorporata in ogni fase del ciclo di vita dello sviluppo. Ogni applicazione bancaria esposta su internet è bersaglio di attacchi automatizzati 24 ore su 24, per cui un **Secure SDLC (S-SDLC)** è la base di partenza, non un'opzione.

**(a) La sicurezza lungo l'SDLC.** La sicurezza si integra in ogni fase: nei **requisiti**, le esigenze di sicurezza vengono raccolte insieme a quelle funzionali e non funzionali (riservatezza, integrità, disponibilità, prestazioni); nella **progettazione**, il **threat modelling** (es. STRIDE) individua le superfici di attacco; nell'**implementazione**, si applicano standard di codifica sicura e **code review**; nel **testing**, viene eseguito un test di sicurezza dedicato; nel **deployment**, hardening e configurazione sicura; nell'**esercizio**, monitoraggio continuo e applicazione delle patch. Il principio è "shift left" — individuare i difetti il prima possibile, quando costano meno da correggere.

**(b) Strategia di testing.** La correttezza funzionale si verifica con **test unitari e di integrazione**; la sicurezza si basa su tre tecniche complementari. Il **SAST** (Static Application Security Testing) analizza il codice sorgente senza eseguirlo, individuando pattern come query prive di prepared statement o dipendenze insicure (es. SonarQube, Semgrep). Il **DAST** (Dynamic Application Security Testing) attacca l'applicazione in esecuzione per trovare problemi a runtime come sessioni compromesse o configurazioni errate (es. OWASP ZAP, Burp Suite). Il **fuzzing** invia input casuali o malformati per individuare crash e comportamenti inattesi. Il SAST vede il codice ma non il runtime; il DAST vede il runtime ma non il codice — una pipeline matura usa entrambi, integrati nella CI.

**(c) OWASP Top 10 e contromisure.** L'OWASP Top 10 è l'elenco di riferimento condiviso delle vulnerabilità web più critiche. Le più rilevanti in questo contesto:
- **A01 Broken Access Control** — un'autorizzazione mancante o errata permette a un utente di accedere ai dati altrui. Contromisure: applicare l'autorizzazione **lato server**, adottare il **principio del privilegio minimo**, negare per default.
- **A02 Cryptographic Failures** — dati sensibili non cifrati o algoritmi deboli. Contromisure: **TLS** per i dati in transito, cifratura robusta at-rest, mai MD5/SHA-1 per le password.
- **A03 Injection** (es. SQL injection) — input non sanificato interpretato come codice. Contromisura: **prepared statement parametrizzati**, validazione dell'input.

**(d) Credenziali e qualità del codice.** Le password non vengono mai memorizzate in chiaro né con hash veloci; si usano **funzioni di derivazione della chiave (KDF)** deliberatamente lente e memory-hard come **Argon2id**, con un salt. La qualità del codice (copertura dei test, bassa complessità ciclomatica, debito tecnico sotto controllo) è alla base di una sicurezza mantenibile.

**Esempio nel contesto.** Per un'istituzione pubblica come la Banca d'Italia, dove ogni applicazione esposta è un bersaglio, un S-SDLC con testing stratificato è essenziale per proteggere riservatezza e integrità dei dati.

**Rischi residui.** (1) Vulnerabilità **zero-day** non individuate dagli strumenti basati su pattern noti. (2) **Dipendenze di terze parti vulnerabili** (rischio di supply chain). (3) **Errori di configurazione** nel deployment. (4) **Errore umano** nonostante il processo — mitigato da monitoraggio continuo e revisione.

---
---

# AMBITO 2 — Basi di dati e data science

## Svolgimento Tema 2.1 — Progettazione di una base di dati: dal concettuale al fisico

**Impostazione.** La progettazione di una base di dati per conti correnti e movimenti procede in tre fasi — concettuale, logica, fisica — che traducono i requisiti reali in uno schema efficiente e corretto. In ambito bancario la **correttezza transazionale** (un movimento non può "perdersi") è il vincolo dominante.

**(a) Progettazione concettuale (modello ER).** Identifico le **entità**: *Cliente* (codice fiscale, nome, recapiti), *Conto* (IBAN, saldo, tipo), *Movimento* (id, data/ora, importo, causale). Le **relazioni**: un Cliente *intesta* uno o più Conti (1:N, o N:M se sono ammessi cointestatari); un Conto *registra* molti Movimenti (1:N). Le **cardinalità** esprimono questi vincoli. Il diagramma ER è indipendente dalla tecnologia: descrive *cosa* rappresentare, non *come* memorizzarlo.

**(b) Progettazione logica (schema relazionale).** Traduco le entità in **tabelle** con **chiavi primarie** (PK) e **chiavi esterne** (FK): `Cliente(CF, ...)`, `Conto(IBAN, CF_titolare→Cliente, saldo, ...)`, `Movimento(id, IBAN→Conto, data, importo, ...)`. Applico la **normalizzazione**: la **1NF** elimina i gruppi ripetuti (valori atomici); la **2NF** rimuove le dipendenze parziali dalla chiave; la **3NF** elimina le dipendenze transitive. La normalizzazione previene le **anomalie** di inserimento, aggiornamento e cancellazione (es. evitare di duplicare i dati anagrafici del cliente su ogni movimento, con il rischio di incoerenze).

**(c) Progettazione fisica.** Scelgo gli **indici** sulle colonne più interrogate: indice sulla PK (automatico), e indici su `Movimento.IBAN` e `Movimento.data` per accelerare le query frequenti ("movimenti di un conto in un periodo"). Gli indici (tipicamente **B-tree**) velocizzano le letture ma rallentano le scritture e occupano spazio: vanno scelti in base ai pattern d'uso reali.

**(d) Transazioni ACID e alternativa NoSQL.** Un bonifico deve essere **atomico**: o si addebita il mittente *e* si accredita il destinatario, o non accade nulla. Le proprietà **ACID** (Atomicità, Consistenza, Isolamento, Durabilità) garantiscono che il database non resti mai in uno stato incoerente. Valuterei una soluzione **NoSQL** per esigenze diverse: enormi volumi di dati semi-strutturati, scalabilità orizzontale, schema flessibile (es. log, dati documentali). Qui interviene il **teorema CAP**: in caso di partizione di rete si sceglie tra consistenza (CP, es. MongoDB/HBase) e disponibilità (AP, es. Cassandra/DynamoDB) — per i saldi conta la consistenza, per dati periferici può bastare la consistenza eventuale (BASE).

**Esempio nel contesto.** I sistemi di un'istituzione come la Banca d'Italia sono, in larga misura, grandi basi di dati: la padronanza di modello relazionale, normalizzazione e ACID è competenza centrale.

**Rischi residui.** (1) **Over-normalizzazione** che penalizza le letture → denormalizzazione mirata. (2) **Indici eccessivi** che appesantiscono le scritture. (3) **Contention/lock** sotto alto carico transazionale. (4) Scelta NoSQL inappropriata dove serve consistenza forte.

---

## Svolgimento Tema 2.2 — Fondamenti di machine learning per un problema di classificazione

**Impostazione.** Il compito — classificare una transazione come legittima o fraudolenta — è un problema di **classificazione supervisionata**, ma la sua caratteristica distintiva è che la frode è un evento **raro**, il che condiziona sia la modellazione sia la valutazione. L'obiettivo è un modello che **generalizzi** su dati nuovi, non uno che memorizzi il training set.

**(a) Tipi di apprendimento.** L'apprendimento **supervisionato** si addestra su dati **etichettati** (ogni transazione marcata come legittima/fraudolenta) ed è la scelta naturale in questo caso. L'apprendimento **non supervisionato** individua strutture senza etichette e si usa quando le frodi etichettate sono scarse — es. **anomaly detection** (isolation forest, autoencoder) che apprende il comportamento "normale" e segnala le deviazioni. L'apprendimento per **rinforzo**, in cui un agente apprende da ricompense, non è adatto a questo compito di classificazione batch.

**(b) La pipeline di ML.** Fasi: **preparazione dei dati** (pulizia, gestione dei valori mancanti, encoding); **selezione/ingegnerizzazione delle feature** (es. importo della transazione, frequenza, ora del giorno, deviazione dalle abitudini del cliente); una suddivisione **train/validation/test** in modo che il modello sia addestrato su una parte, calibrato su un'altra e valutato su dati mai visti; quindi l'**addestramento del modello** (es. regressione logistica come baseline interpretabile, poi modelli ad albero per le prestazioni).

**(c) Overfitting e valutazione.** L'**overfitting** si verifica quando il modello si adatta al rumore dei dati di addestramento e fallisce sui casi nuovi; i sintomi sono un'accuratezza alta in training ma scarsa in test. Mitigazioni: **regolarizzazione**, **cross-validation**, modelli più semplici, più dati. È fondamentale ricordare che l'**accuratezza è fuorviante** per gli eventi rari — un modello che predice "mai frode" può avere il 99% di accuratezza ed essere inutile. Metriche migliori: **precision** (tra i casi segnalati, quanti sono davvero frodi), **recall** (tra tutte le frodi, quante ne cogliamo) e il loro bilanciamento, l'**F1**. Nel fraud detection, perdere una frode (recall basso) è di solito più costoso di un falso allarme, ma i falsi positivi generano attrito — la soglia decisionale deve riflettere questi costi.

**(d) Interpretabilità e AI Act.** La **regressione logistica** fornisce coefficienti leggibili (si può spiegare *perché* una transazione è stata segnalata), mentre un modello "black-box" profondo no. In un contesto regolamentato questo conta: l'**AI Act** classifica i sistemi di fraud detection e credit scoring come **ad alto rischio**, richiedendo spiegabilità, governance dei dati e sorveglianza umana.

**Esempio nel contesto.** Per la Banca d'Italia in quanto autorità di vigilanza, capire il ML significa poterlo **governare** — verificare che i soggetti vigilati utilizzino tali modelli in modo trasparente e conforme — non semplicemente saperlo costruire.

**Rischi residui.** (1) **Concept drift** — i pattern di frode cambiano, per cui il modello degrada e va ri-addestrato. (2) **Sbilanciamento delle classi** gestito male → recall scarso. (3) **Bias** nei dati che produce risultati iniqui. (4) **Trade-off spiegabilità-prestazioni**: i modelli più potenti sono i meno trasparenti.

---
---

# AMBITO 3 — Architettura dei sistemi informatici e delle reti

## Svolgimento Tema 3.1 — Rete sicura e resiliente con componenti cloud

**Impostazione.** Una rete che collega le filiali a un data center centrale, con alcuni servizi in cloud, deve soddisfare simultaneamente tre obiettivi: **comunicazione sicura**, **segmentazione** in modo che una compromissione non si propaghi, e **resilienza** affinché il servizio sopravviva ai guasti. La difesa in profondità è il principio guida.

**(a) Modelli a livelli e dispositivi.** I modelli **OSI** e **TCP/IP** strutturano la comunicazione in livelli. Dispositivi chiave: uno **switch** opera al livello 2 (Data Link), inoltrando i frame in base all'indirizzo MAC all'interno di una LAN; un **router** opera al livello 3 (Rete), instradando i pacchetti IP tra reti diverse. I protocolli fondamentali includono IP, TCP/UDP, DNS e HTTPS su TLS.

**(b) Segmentazione e difesa perimetrale.** I servizi esposti al pubblico risiedono in una **DMZ**, isolata dalla rete interna; le reti interne sono suddivise in **VLAN** per limitare il movimento laterale. Un **firewall stateful** applica la policy sul traffico; **IDS/IPS** rilevano e bloccano le intrusioni; un **reverse proxy** fornisce terminazione TLS, un **WAF** e rate limiting, nascondendo la topologia interna. La connettività delle filiali e degli accessi remoti utilizza **VPN** (IPsec o TLS) per cifrare il traffico su collegamenti non fidati, e **TLS** protegge i dati in transito end-to-end.

**(c) Attacchi alla rete e contromisure.** Il **DDoS** satura il servizio — mitigato con traffic scrubbing, CDN e rate limiting. Il **man-in-the-middle** intercetta il traffico — contrastato con TLS e validazione/pinning dei certificati. Lo **spoofing ARP/DNS** reindirizza il traffico — mitigato con DNSSEC, dynamic ARP inspection e segmentazione della rete. Alla base di tutto: il **principio del privilegio minimo** e la micro-segmentazione per minimizzare il **raggio d'impatto (blast radius)** di ogni compromissione.

**(d) Fondamenti cloud e resilienza.** I modelli di servizio cloud — **IaaS, PaaS, SaaS** — differiscono per ciò che è gestito dal fornitore rispetto al cliente; il **modello di responsabilità condivisa** rende esplicito questo confine (il fornitore protegge l'infrastruttura, il cliente protegge i propri dati e la configurazione). L'**alta disponibilità** elimina i single point of failure tramite ridondanza (active-active o active-standby), **load balancing** e deployment **multi-AZ** — una disponibilità del 99,99% consente circa 52 minuti di downtime all'anno. Il **disaster recovery** aggiunge backup, **RPO/RTO** definiti e un sito secondario.

**Esempio nel contesto.** La rete di una banca centrale veicola traffico critico e di elevato valore ed è un bersaglio costante; segmentazione, cifratura e design resiliente sostengono direttamente la continuità operativa, in linea con le aspettative di DORA.

**Rischi residui.** (1) **Rischio di concentrazione cloud** (dipendenza da un unico fornitore) — da governare con piani di uscita. (2) **Errori di configurazione**, causa principale degli incidenti cloud. (3) **Minacce interne (insider)** e furto di credenziali. (4) **Guasti correlati** nei sistemi ridondanti.

---

## Svolgimento Tema 3.2 — Tecniche crittografiche e applicazioni, con cenni ai registri distribuiti (DLT)

**Impostazione.** La crittografia fornisce i mattoni della sicurezza informatica: **riservatezza, integrità, autenticità, non ripudio**. In ambito bancario sostiene comunicazioni sicure, firme, protezione dei dati. Illustro le tecniche fondamentali, due applicazioni concrete e un cenno ai registri distribuiti.

**(a) Simmetrica, asimmetrica, hash.** La **crittografia simmetrica** (es. **AES**) usa un'unica chiave condivisa per cifrare e decifrare: è veloce, ma pone il problema dello **scambio sicuro della chiave**. La **crittografia asimmetrica** (es. **RSA**, **ECC**) usa una coppia di chiavi: per inviare un messaggio cifrato a Bob si usa la sua **chiave pubblica**, e solo Bob può decifrarlo con la **chiave privata**; è più lenta, perciò si usa tipicamente per lo scambio di chiavi e per la firma. Le **funzioni hash** (es. **SHA-256**) producono un'impronta di lunghezza fissa, sono **a senso unico** e resistenti alle collisioni: servono per verificare l'**integrità**.

**(b) Firma digitale, X.509, PKI, TLS.** La **firma digitale** si ottiene cifrando l'**hash** del messaggio con la chiave **privata** del firmatario: chiunque, con la chiave **pubblica**, può verificarla, ottenendo **integrità, autenticità e non ripudio**. La fiducia nelle chiavi pubbliche è garantita dai **certificati X.509** emessi da Autorità di Certificazione all'interno di una **PKI** (Public Key Infrastructure). È questo il meccanismo che sta alla base di **TLS/HTTPS**.

**(c) Due applicazioni concrete.** *Comunicazione sicura (handshake TLS)*: client e server negoziano i parametri, il server presenta il certificato X.509, si stabilisce una chiave di sessione (con metodi a scambio sicuro) e da lì la comunicazione prosegue cifrata simmetricamente — combinando la sicurezza dell'asimmetrica con la velocità della simmetrica. *Memorizzazione delle password*: mai in chiaro né con algoritmi obsoleti (MD5/SHA-1); si usano **KDF** deliberatamente lente e **memory-hard** come **Argon2id**, con un **salt** per ogni utente, rendendo il *brute force* economicamente inattuabile.

**(d) Registri distribuiti (DLT) e post-quantum.** Una **DLT** è un registro condiviso e replicato tra più nodi, le cui proprietà chiave sono **immutabilità** (i blocchi sono concatenati tramite hash, alterarne uno invaliderebbe la catena) e **decentralizzazione**; un algoritmo di **consenso** permette ai nodi di concordare sullo stato senza un'autorità centrale. Sul fronte **post-quantum**: un futuro computer quantistico, con l'algoritmo di Shor, romperebbe RSA ed ECC; per questo il NIST ha standardizzato algoritmi resistenti (**ML-KEM** per lo scambio chiavi, **ML-DSA** per le firme), mentre **AES** resta robusto (solo indebolito da Grover, e sufficiente con chiavi a 256 bit).

**Esempio nel contesto.** Le comunicazioni e i sistemi di firma di un'istituzione finanziaria poggiano interamente su queste primitive; conoscere come si combinano (asimmetrica per stabilire fiducia, simmetrica per la velocità) è competenza di base per l'esercizio e la manutenzione dei sistemi.

**Rischi residui.** (1) **Gestione delle chiavi** (generazione, custodia, revoca) come anello debole. (2) **Algoritmi obsoleti** ancora in uso. (3) **Certificati** scaduti o mal configurati. (4) **Minaccia "harvest now, decrypt later"**, che rende prudente pianificare per tempo la transizione post-quantum.

---
---

> **Nota d'uso.** Sono risposte-modello di riferimento: all'esame conta riprodurne l'**impianto** (impostazione → sviluppo con specifiche → esempio nel contesto BdI → rischi residui), non il testo a memoria. Allena la scrittura *a mano e a tempo* (≈2h per quesito). Ricorda inoltre che la prova prevede un elaborato in lingua inglese: esercitati a scrivere autonomamente in inglese almeno uno di questi svolgimenti. *Promemoria*: pag. 11 è il programma del **Profilo C**; se il tuo obiettivo resta il **Profilo A**, usa questi come ripasso dei fondamentali.
