# Soluzioni — Simulazione Ramo C: Architetture, Cloud, Migrazione & Qualità del Software

> Risposte modello alla [simulazione Ramo C](AGID_Simulazione_Ramo_C.md), redatte per coprire tutte le voci della griglia di autocorrezione.

---

## Quesito 1 — Secure by Design, Threat Modeling, SAST/DAST

**Secure by Design** significa integrare la sicurezza fin dalla fase di progettazione del software, non aggiungerla come controllo a posteriori su un sistema già costruito: le scelte architetturali (superficie di attacco, gestione delle identità, segregazione dei dati) vengono valutate per il loro impatto di sicurezza prima ancora che si scriva la prima riga di codice.

Il **Threat Modeling** è la pratica con cui, nella fase di analisi/progettazione, si identificano sistematicamente le minacce a cui l'architettura è esposta (es. con metodologie come STRIDE), individuando i punti deboli e le contromisure necessarie prima che diventino vulnerabilità in produzione — è quindi un'attività "a monte", non un test successivo.

**SAST** (Static Application Security Testing) analizza il codice sorgente (o il bytecode) senza eseguirlo, individuando pattern di vulnerabilità (es. injection, uso di funzioni insicure) direttamente nel repository; **DAST** (Dynamic Application Security Testing) testa invece l'applicazione **in esecuzione**, simulando attacchi reali contro l'interfaccia esposta (es. fuzzing degli endpoint HTTP). In una pipeline **DevSecOps**, SAST viene tipicamente eseguito ad ogni commit/pull request (feedback rapido al developer), mentre DAST viene eseguito in ambiente di staging prima del rilascio in produzione: entrambi sono automatizzati e continui, non controlli manuali occasionali.

---

## Quesito 2 — ISO/IEC 25010 e capitolato di gara

Il modello **ISO/IEC 25010** definisce otto caratteristiche di qualità del software, tra cui: **funzionalità** (adeguatezza, correttezza delle funzioni offerte), **affidabilità** (maturità, disponibilità, tolleranza ai guasti), **usabilità** (facilità d'uso, accessibilità), **sicurezza** (riservatezza, integrità, autenticità), **manutenibilità** (modularità, testabilità, facilità di modifica) e **portabilità** (adattabilità a diversi ambienti).

Ognuna di queste caratteristiche è traducibile in **criteri misurabili** inseribili in un capitolato di gara ICT: l'affidabilità si traduce in metriche come **MTBF** (Mean Time Between Failures) e **MTTR** (Mean Time To Repair), da fissare come SLA contrattuali; la sicurezza si traduce in un **tempo massimo di remediation** delle vulnerabilità rilevate, differenziato per criticità (es. critica entro 15 giorni); la manutenibilità si può misurare con la **densità di difetti** per KLOC o la copertura dei test (code coverage minimo richiesto, es. 80%). Inserire queste metriche come requisiti contrattuali permette alla PA di valutare oggettivamente l'offerta tecnica e di monitorare l'esecuzione contrattuale nel tempo, anziché affidarsi a valutazioni qualitative generiche.

---

## Quesito 3 — Percorsi di migrazione al Cloud

I tre percorsi di migrazione cloud, in ordine crescente di sforzo e beneficio atteso, sono:

- **Rehost** ("lift & shift"): il sistema viene spostato così com'è su infrastruttura IaaS cloud, senza modifiche architetturali. Sforzo minimo, beneficio limitato (si guadagna elasticità infrastrutturale ma non si riducono debito tecnico o costi operativi legati all'architettura monolitica). Caso d'uso tipico: un sistema legacy con vincoli temporali stretti (es. dismissione imminente di un data center), dove non c'è tempo/budget per un refactoring.
- **Replatform**: si applicano modifiche minime e mirate, senza riscrivere l'applicazione (es. sostituire un database self-hosted con un servizio **DBaaS** gestito dal cloud provider). Sforzo intermedio, beneficio maggiore del Rehost (si eliminano alcuni oneri operativi, come il patching del DBMS). Caso d'uso tipico: un'applicazione con un componente chiaramente sostituibile con un servizio managed, senza toccare la logica applicativa.
- **Rearchitect/Refactor**: l'applicazione viene riprogettata in ottica cloud-native (microservizi, container, funzioni serverless). Sforzo massimo, beneficio massimo in termini di scalabilità, resilienza e costi operativi a regime. Caso d'uso tipico: un sistema strategico con orizzonte di vita lungo, per cui l'investimento di riscrittura si ripaga nel tempo attraverso minori costi operativi e maggiore velocità di evoluzione.

---

## Quesito 4 — Polo Strategico Nazionale (PSN)

Il **PSN** non è un ente pubblico, ma un'**infrastruttura cloud sovrana** realizzata tramite concessione, il cui utilizzo è **obbligatorio** per l'erogazione dei servizi e per il trattamento dei dati delle PA classificati come **Critici** e **Strategici** (secondo la classificazione prevista dalla strategia cloud nazionale), mentre per i dati/servizi Ordinari resta possibile l'utilizzo di cloud pubblico qualificato.

I diversi ruoli non vanno confusi tra loro:
- l'**indirizzo strategico** spetta alla **Presidenza del Consiglio dei Ministri – Dipartimento per la Trasformazione Digitale**;
- i **requisiti di sicurezza e la classificazione** dei dati/servizi sono definiti dall'**ACN** (Agenzia per la Cybersicurezza Nazionale), distinto dal ruolo dell'**AGID**, che si occupa invece della **qualificazione tecnica** dei cloud provider (incluso il marketplace dei servizi cloud qualificati);
- la **stazione appaltante** della concessione, per la rilevanza securitaria dell'infrastruttura, è **Difesa Servizi S.p.A.**;
- la **gestione operativa** dell'infrastruttura per la durata della concessione (15 anni) è affidata al concessionario **PSN S.p.A.**, un consorzio composto da TIM, CDP Equity, Sogei e Leonardo.

Il punto centrale da non confondere in una risposta d'esame è quindi: indirizzo politico ≠ vigilanza/classificazione di sicurezza ≠ qualificazione tecnica dei provider ≠ gestione operativa privata in concessione — quattro piani distinti, retti da soggetti diversi.

---

## Caso gestionale

*Metodo (4 mosse): (1) inquadramento normativo, (2) metodo progettuale, (3) soluzione tecnica, (4) rischio & budget.*

**Contesto.** Un'Agenzia centrale deve dismettere entro 18 mesi un data center on-premise obsoleto che ospita un sistema legacy monolitico, classificato come servizio **Critico**, cogliendo l'occasione per migliorare qualità e sicurezza del software.

### (a) Destinazione infrastrutturale e percorso di migrazione

Trattandosi di un servizio classificato **Critico**, la destinazione infrastrutturale è **obbligata verso il Polo Strategico Nazionale (PSN)**: non è ammessa una migrazione verso un cloud pubblico generico qualificato, riservato ai servizi non Critici/Strategici.

Dato il vincolo temporale stringente (18 mesi) e la natura monolitica/legacy del sistema, il percorso più adeguato è il **Replatform**: un puro **Rehost** lascerebbe intatto il debito tecnico e non porterebbe alcun miglioramento di qualità/sicurezza (obiettivo esplicito dell'Agenzia), mentre un **Rearchitect** completo verso microservizi in 18 mesi su un sistema Critico sarebbe rischioso e probabilmente non completabile in sicurezza nel tempo dato. Il Replatform consente di modernizzare componenti puntuali (es. spostare il database su un servizio gestito, containerizzare l'applicazione senza riscriverla) restando dentro il vincolo temporale, con un beneficio concreto rispetto al puro lift & shift.

### (b) Secure by Design nel ciclo di sviluppo

La migrazione è l'occasione per introdurre: **threat modeling** in fase di analisi/disegno della nuova architettura target, per identificare a monte i rischi introdotti dal cloud (es. superficie di attacco delle API esposte); **SAST** integrato ad ogni commit nella pipeline CI, per intercettare vulnerabilità nel codice prima del merge; **DAST** in ambiente di staging prima di ogni rilascio in produzione; e **hardening delle configurazioni** (immagini container minimali, baseline di sicurezza sui servizi PaaS/IaaS usati, secrets management) applicato in fase di deploy della pipeline CD.

### (c) Modello di qualità e capitolato di gara

Il framework di riferimento è **ISO/IEC 25010**, da tradurre in metriche operative concrete da monitorare durante e dopo la migrazione: **code coverage** minimo dei test automatizzati (oggi storicamente assente), **densità di difetti** per rilascio, **tempo di remediation** delle vulnerabilità rilevate da SAST/DAST, differenziato per severità. Queste metriche vanno inserite come **requisiti contrattuali/KPI** nel capitolato di gara per il fornitore incaricato della migrazione, con eventuali penali associate al mancato rispetto delle soglie concordate, in modo da rendere il miglioramento di qualità un obbligo verificabile e non un'aspettativa generica.

### (d) Rischi e budget (TCO)

- **Finestra di indisponibilità**: trattandosi di servizio Critico, va pianificato un cutover a basso impatto (es. migrazione incrementale per componenti, ambiente parallelo con switch finale, piano di rollback testato);
- **Debito tecnico residuo**: il Replatform non elimina interamente il debito tecnico del monolite — va programmato un percorso successivo di Rearchitect a medio termine, esplicitando questa scelta come compromesso temporaneo e non come soluzione definitiva;
- **Lock-in del fornitore/cloud provider**: da mitigare preferendo, dove possibile, servizi gestiti basati su standard aperti e prevedendo clausole contrattuali di portabilità/reversibilità del dato a fine contratto;
- **TCO**: il budget di migrazione deve includere non solo il costo una tantum del progetto di replatform, ma i costi ricorrenti (canone dei servizi PaaS/IaaS sul PSN, manutenzione evolutiva, formazione del personale sulle nuove pipeline DevSecOps).

**Criticità residue.** Il vincolo dei 18 mesi resta stringente per un sistema Critico: va concordato con la governance dell'Agenzia un piano di contingenza nel caso in cui il Replatform non fosse completabile nei tempi, per evitare di dover accettare un Rehost puro all'ultimo momento.
