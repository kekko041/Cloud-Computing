# Prova scritta — Profilo C (Assistente ICT)
### Sei temi d'esame su tre ambiti tematici · Banca d'Italia 2026 (pag. 11 del bando)

> **Come funziona la prova reale.** La Commissione propone **sei quesiti** (due per ciascuno dei tre ambiti del programma di pag. 11). Tu ne scegli **due, su due ambiti differenti**, da svolgere in **5 ore**. **Almeno uno** dei due va redatto in **lingua inglese** (o l'intero quesito è formulato in inglese).
>
> **Taglio del Profilo C.** Rispetto al Profilo A (laurea magistrale), qui prevalgono i **fondamenti applicati**: progettare e analizzare soluzioni corrette ed efficienti, padroneggiare il lessico tecnico, motivare le scelte. Meno frontiera di ricerca, più solidità sui concetti di base.
>
> **Metodo di risposta (PEEL).** *Point* (impostazione) → *Evidence* (concetti, dati, esempi) → *Explanation* (analisi e trade-off) → *Link* (collegamento al contesto Banca d'Italia). La Commissione valuta correttezza tecnica, organizzazione, lessico specialistico e padronanza dell'inglese.
>
> I quesiti 🇬🇧 sono i candidati ideali per l'elaborato in lingua.

---

## Ambito 1 — Progettazione e sviluppo del software
*Riferimento manuale: Capitolo 2, §2.1 (algoritmi, strutture dati, complessità), §2.3 (linguaggi e paradigmi), §2.4 (ingegneria e sicurezza del software). Programma bando: algoritmi e strutture dati, complessità, linguaggi e paradigmi, ingegneria del software, sicurezza del software (vulnerabilità, attacchi, contromisure).*

### Tema 1.1 — Algoritmi e strutture dati per la riconciliazione di transazioni

> Un sistema bancario deve elaborare ogni giorno un grande volume di record di transazioni. Si chiede di progettare la logica per: (i) **individuare i duplicati**, (ii) **ordinare** i record secondo un criterio (es. timbro temporale), (iii) **ricercare** rapidamente una transazione dato un identificatore.
>
> Il candidato:
> - (a) scelga le **strutture dati** appropriate (array, liste, alberi, tabelle hash) motivando ciascuna scelta;
> - (b) descriva gli **algoritmi** di ordinamento e ricerca adottati e ne analizzi la **complessità** in notazione O-grande (tempo e spazio), distinguendo caso medio e caso pessimo;
> - (c) discuta i **trade-off** tempo/memoria e l'impatto della scalabilità al crescere dei dati;
> - (d) accenni alla distinzione tra problemi **trattabili e intrattabili** (classi P/NP) e a perché è rilevante nella pratica.
>
> Si motivino le scelte e si indichino i limiti della soluzione proposta.

**Punti chiave da trattare.** Tabella hash per ricerca/deduplica in O(1) medio (con gestione delle collisioni e degenerazione O(n) nel caso pessimo); ordinamento: merge sort O(n log n) stabile e con caso pessimo garantito, vs quick sort O(n log n) medio ma O(n²) nel pessimo con pivot sbilanciato; ricerca binaria O(log n) su dati ordinati; trade-off spazio (hash table) vs tempo; importanza della scelta della struttura dati sulla scalabilità di un sistema che processa milioni di record; cenno a P/NP (perché alcuni problemi non hanno soluzione efficiente nota).

---

### Tema 1.2 — Secure SDLC e OWASP per un'applicazione web 🇬🇧

> A bank is developing a web application that handles user authentication and sensitive customer data. The Commission asks you to describe how to build security into the software development life cycle.
>
> Il candidato (in inglese):
> - (a) describe the **phases of the SDLC** and how security is integrated at each stage (**S-SDLC**), including functional and non-functional requirements;
> - (b) present a **testing strategy**: unit/integration testing plus security testing — **SAST**, **DAST** and **fuzzing** — explaining how they complement each other;
> - (c) analyse the most critical **OWASP Top 10** vulnerabilities (e.g. Broken Access Control, Cryptographic Failures, Injection) and the corresponding **countermeasures**;
> - (d) discuss secure handling of credentials and code-quality practices.
>
> Motivate the choices and identify residual risks.

**Punti chiave da trattare.** Sicurezza "by design" lungo le 7 fasi (requisiti → threat modeling/STRIDE → design → code review + SAST → security testing/DAST → deploy sicuro → monitoraggio); SAST (analisi statica del sorgente, es. SonarQube/Semgrep) vs DAST (analisi a runtime, es. OWASP ZAP/Burp) vs fuzzing (input casuali, es. AFL) — complementari; OWASP A01 Broken Access Control (least privilege, controlli server-side), A02 Cryptographic Failures (no MD5/SHA1 per password → Argon2id/bcrypt; TLS per i dati in transito), A03 Injection (prepared statement parametrizzati contro la SQL injection); qualità del codice (copertura test, bassa complessità, debito tecnico). *Dominio ad alto lessico standardizzato: ottimo per l'inglese.*

---

## Ambito 2 — Basi di dati e data science
*Riferimento manuale: Capitolo 2, §2.5 (basi di dati relazionali e NoSQL) e Capitolo 4 (elementi di IA/ML). Programma bando: basi di dati relazionali, progettazione concettuale/logica/fisica, NoSQL e distribuite, elementi di IA e ML.*

### Tema 2.1 — Progettazione di una base di dati: dal modello concettuale a quello fisico

> Si deve progettare la base di dati per la gestione di conti correnti e relative operazioni (clienti, conti, movimenti). Il candidato sviluppi le tre fasi di progettazione.
>
> - (a) **Progettazione concettuale**: modello **Entità-Relazione** (entità, attributi, relazioni, cardinalità);
> - (b) **Progettazione logica**: traduzione nello **schema relazionale**, con chiavi primarie ed esterne, e applicazione della **normalizzazione** (1NF, 2NF, 3NF), spiegando quali anomalie elimina;
> - (c) **Progettazione fisica**: scelte di **indicizzazione** e ottimizzazione delle query più frequenti;
> - (d) discuta le **proprietà ACID** delle transazioni (perché un trasferimento di denaro deve essere atomico) e indichi in quali casi si valuterebbe una soluzione **NoSQL**, richiamando il **teorema CAP**.
>
> Si motivino le scelte e si discutano i trade-off (es. normalizzazione vs prestazioni in lettura).

**Punti chiave da trattare.** Modello ER → schema relazionale (es. Cliente, Conto, Movimento con FK); forme normali e anomalie di inserimento/aggiornamento/cancellazione; indici (B-tree) per accelerare le ricerche a costo di scritture più lente; ACID con l'esempio del bonifico (atomicità: o si addebita e accredita, o niente); denormalizzazione mirata per le letture analitiche; NoSQL quando servono volume/varietà/scalabilità orizzontale (documentale, key-value, colonnare, a grafo) e relativo posizionamento CAP (CP es. MongoDB/HBase, AP es. Cassandra/DynamoDB); BASE come alternativa alla consistenza forte.

---

### Tema 2.2 — Elementi di machine learning per un problema di classificazione 🇬🇧

> A bank wants to build a simple model to classify whether a transaction is **legitimate or fraudulent**. The Commission asks you to outline the fundamentals of a machine-learning approach.
>
> Il candidato (in inglese):
> - (a) explain the difference between **supervised, unsupervised and reinforcement** learning, and state which fits this problem;
> - (b) describe the basic **ML pipeline**: data preparation, feature selection, **train/validation/test split**, model training;
> - (c) explain **overfitting** and how to mitigate it (regularisation, cross-validation), and why **evaluation metrics** must go beyond accuracy (precision, recall, F1) for a rare-event problem;
> - (d) comment on **model interpretability** (e.g. logistic regression vs a "black-box" model) and why it matters in a regulated, **AI Act** context.
>
> Discuss the limitations and residual risks of the approach.

**Punti chiave da trattare.** Supervisionato (servono dati etichettati frode/legittima) vs non supervisionato (anomaly detection quando mancano le etichette, es. isolation forest/autoencoder) vs reinforcement; pipeline: pulizia dati, feature engineering, split train/validation/test per stimare la generalizzazione; overfitting = modello che memorizza il rumore → regolarizzazione, cross-validation, più dati; perché l'accuratezza inganna con classi sbilanciate (frodi rare) → precision/recall/F1; interpretabilità: la regressione logistica dà coefficienti leggibili, una rete profonda è black box — l'AI Act richiede spiegabilità per i sistemi ad alto rischio. *Tema con lessico ML molto internazionale: adatto all'inglese.*

---

## Ambito 3 — Architettura dei sistemi informatici e delle reti
*Riferimento manuale: Capitolo 2, §2.2 (architettura elaboratori e sistemi operativi), §2.6 (reti, cloud, alta disponibilità) e Capitolo 3 (crittografia). Programma bando: architettura elaboratori, sistemi operativi, sistemi distribuiti e DLT, reti (protocolli, architetture, standard, vulnerabilità, attacchi, contromisure), cloud computing, tecniche crittografiche.*

### Tema 3.1 — Architettura di rete sicura e resiliente, con cenni al cloud 🇬🇧

> A bank must design a secure and resilient network connecting branch offices to a central data centre, with services partly hosted in the cloud. The Commission asks you to describe the architecture.
>
> Il candidato (in inglese):
> - (a) recall the layered models (**OSI** and **TCP/IP**) and the role of key devices (switch at layer 2, router at layer 3) and protocols;
> - (b) design the **network segmentation and perimeter defence**: **DMZ**, VLANs, **firewall**, IDS/IPS, **VPN** for remote/branch connectivity, **TLS** for data in transit;
> - (c) identify common **network attacks** (DDoS, man-in-the-middle, ARP/DNS spoofing) and their **countermeasures**;
> - (d) outline **cloud fundamentals** (IaaS/PaaS/SaaS, the **shared-responsibility** model) and **high-availability / disaster-recovery** measures (redundancy, load balancing, multi-AZ).
>
> Motivate the choices and discuss residual risks.

**Punti chiave da trattare.** OSI/TCP-IP e dispositivi (router L3 instrada IP tra reti, switch L2 usa MAC); segmentazione e difesa in profondità: DMZ per i servizi esposti, VLAN, firewall stateful, IDS/IPS, reverse proxy (SSL termination, WAF, rate limiting); VPN (IPsec/TLS) per filiali e accesso remoto; attacchi: DDoS (mitigazione con scrubbing/CDN), MITM (TLS, certificate pinning), ARP/DNS spoofing; cloud: modelli di servizio e responsabilità condivisa; HA = eliminare i single point of failure (ridondanza active-active/active-standby, load balancing, multi-AZ; 99,99% ≈ 52 min/anno di downtime) e DR (RPO/RTO, backup, sito secondario). *Lessico di rete molto standardizzato: ottimo per l'inglese.*

---

### Tema 3.2 — Tecniche crittografiche e loro applicazioni, con cenni ai registri distribuiti (DLT)

> Si chiede di illustrare le principali tecniche crittografiche e le loro applicazioni nei sistemi bancari, con un cenno ai registri distribuiti.
>
> Il candidato:
> - (a) distingua **crittografia simmetrica e asimmetrica** (cifratura, scambio di chiavi) e spieghi a cosa servono le **funzioni hash**;
> - (b) descriva la **firma digitale** e i meccanismi di **integrità e autenticazione**, e il ruolo dei **certificati X.509** e della **PKI** in **TLS/HTTPS**;
> - (c) illustri due applicazioni concrete: la **comunicazione sicura** (handshake TLS) e la **memorizzazione sicura delle password** (funzioni KDF lente e memory-hard come Argon2id);
> - (d) introduca i **registri distribuiti (DLT)**: proprietà (immutabilità, decentralizzazione), idea di **consenso**, e un cenno alle **soluzioni crittografiche post-quantum**.
>
> Si motivino le scelte e si indichino limiti e rischi.

**Punti chiave da trattare.** Simmetrica (AES, veloce, problema dello scambio chiavi) vs asimmetrica (RSA/ECC, per cifrare verso il destinatario si usa la sua chiave pubblica, decifra con la privata; più lenta → usata per scambio chiavi e firma); hash (SHA-256: integrità, one-way, resistenza alle collisioni); firma digitale = hash del messaggio cifrato con chiave privata, verificabile con la pubblica → integrità + autenticità + non ripudio; PKI e X.509 come base di fiducia in TLS; password: mai in chiaro o con MD5/SHA1, ma Argon2id con salt; cenno DLT (catena di blocchi con hash, consenso per concordare lo stato, immutabilità) e post-quantum (RSA/ECC vulnerabili a Shor → standard NIST ML-KEM/ML-DSA; AES resta robusto, indebolito solo da Grover).

---

## Come usare questi temi (Profilo C, <4 settimane)

- **Settimana 1.** Svolgi a tempo (≈2h) il **Tema 2.1** (basi di dati — l'ambito più frequente nelle prove scritte) e il **Tema 1.1** (algoritmi). Confronta con i punti chiave e con §2.1 e §2.5 del manuale.
- **Settimana 2.** Sicurezza del software e crittografia: **Tema 1.2** (in inglese) e **Tema 3.2**. Studia §2.4 e Cap. 3.
- **Settimana 3.** Reti, cloud e ML: **Tema 3.1** (in inglese) e **Tema 2.2** (in inglese). Poi simula la prova reale: **due ambiti diversi in 5 ore, uno in inglese**.
- **Settimana 4.** Revisione mirata sugli errori + ripasso del lessico tecnico inglese ricorrente.

> **Nota.** Pag. 11 è il programma del **Profilo C**. Se il tuo obiettivo resta il **Profilo A** (pag. 9), usa pure questi temi come allenamento sui fondamentali, ma la tua prova avrà ambiti e profondità diversi (vedi il set di temi del Profilo A).
