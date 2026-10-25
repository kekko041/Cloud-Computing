# Materie 1-5 e 7 — Schede flash ad alto rendimento

> Formato: solo i fatti che si trasformano in quiz. ⚠️ = punto in cui hai sbagliato o lasciato in bianco al MIT.

---
## 1. Project management e Program management
### Gerarchia
| Livello | Obiettivo | Produce |
|---|---|---|
| **Progetto** | sforzo **temporaneo** per un risultato **unico** | **output/deliverable** |
| **Programma** | gruppo di progetti **correlati**, gestiti in modo coordinato per ottenere **benefici** non ottenibili singolarmente | **outcome/benefici** (*benefits realization*) |
| **Portfolio** | insieme di progetti e programmi scelti per **allinearsi alla strategia** | priorità e allocazione delle risorse |
| PMO | struttura che standardizza la governance di progetto | — |

- **Program management** (PMI *Standard for Program Management*): domini di performance — **allineamento strategico, gestione dei benefici, coinvolgimento degli stakeholder, governance, gestione del ciclo di vita**. **MSP** (AXELOS) è l'equivalente britannico.
- **Il PNRR è un tipico programma**: tanti progetti (Comuni, PA) → benefici misurati da target.

### Standard
- **PMBOK 6**: **5 gruppi di processi** (avvio, pianificazione, esecuzione, monitoraggio e controllo, chiusura) × **10 aree di conoscenza** (integrazione, ambito, tempi, costi, qualità, risorse, comunicazione, rischi, approvvigionamenti, stakeholder).
- **PMBOK 7**: **12 principi** e **8 domini di prestazione** (approccio basato sui principi, che include l'agile).
- **PRINCE2**: **7 principi** (giustificazione commerciale continua, imparare dall'esperienza, ruoli definiti, gestione per fasi, **gestione per eccezioni**, focus sui prodotti, adattamento), **7 temi/pratiche** (business case, organizzazione, qualità, piani, rischio, cambiamento, avanzamento), **7 processi**. Il **Project Board** è l'organo decisionale.
- **ISO 21500/21502** (progetti), ISO 21503 (programmi), ISO 21504 (portfolio).

### Strumenti e formule
- **Project charter**: **autorizza formalmente** il progetto e nomina il PM.
- **WBS**: scomposizione gerarchica del **lavoro** (regola del **100%**); il livello più basso è il **work package**. **OBS** = organizzazione, **RBS** = rischi/risorse.
- **RACI**: Responsible (esegue), **Accountable (uno solo, risponde del risultato)**, Consulted, Informed.
- **Critical Path Method**: il percorso critico è il **più lungo** e ha **float/slack = 0**; un ritardo su un'attività critica ritarda l'intero progetto. *Crashing* = aggiungere risorse; *fast tracking* = sovrapporre attività.
- **PERT**: durata attesa = **(O + 4M + P) / 6**.
- **Gantt**: barre nel tempo; **milestone** = evento a durata zero.
- **Earned Value Management**:
  - PV = valore pianificato, **EV = valore guadagnato**, AC = costo effettivo, BAC = budget a finire;
  - **CV = EV − AC**, **SV = EV − PV** (negativo = sovracosto/ritardo);
  - **CPI = EV/AC**, **SPI = EV/PV** (< 1 = male);
  - **EAC = BAC/CPI**; ETC = EAC − AC; VAC = BAC − EAC.
- **Vincolo triplo**: ambito, tempi, costi (con la qualità al centro).
- **Rischi**:
  - **minacce** → evitare, **trasferire** (assicurazione, contratto), mitigare, accettare, escalare;
  - **opportunità** → sfruttare, condividere, migliorare, accettare;
  - **registro dei rischi**; **esposizione = probabilità × impatto**.
- **Stakeholder** (matrice potere/interesse): alto-alto → **gestire da vicino**; alto potere/basso interesse → mantenere soddisfatti; basso potere/alto interesse → tenere informati; basso-basso → monitorare.
- **Change control**: ogni variazione dell'ambito passa dal **Change Control Board** → si evita lo **scope creep**.
- **MoSCoW**: Must, Should, Could, Won't.

### Agile
- **Manifesto Agile (2001)**: 4 valori — individui e interazioni > processi e strumenti; software funzionante > documentazione esaustiva; collaborazione col cliente > negoziazione dei contratti; rispondere al cambiamento > seguire un piano. 12 principi.
- **Scrum (Guida 2020)**:
  - **3 responsabilità**: Product Owner (massimizza il valore, gestisce il **Product Backlog**), Scrum Master (servant leader, rimuove gli impedimenti), Developers;
  - **eventi**: Sprint (≤ 1 mese), Sprint Planning, **Daily Scrum (15 min)**, Sprint Review (prodotto, con gli stakeholder), **Retrospective** (processo, solo il team);
  - **artefatti**: Product Backlog (→ Product Goal), Sprint Backlog (→ Sprint Goal), Increment (→ **Definition of Done**).
- **Kanban**: flusso continuo, **limiti WIP**, lead time. **SAFe**: scaling agile. **Velocity** = story point per sprint. **MVP** = prodotto minimo per validare un'ipotesi.
- **ITIL 4**: Service Value System, **4 dimensioni**, **34 pratiche**. **Incident** = ripristino rapido del servizio; **Problem** = causa radice; **Change** = modifiche controllate (standard/normal/emergency). **SLA** (con il cliente), **OLA** (interno), **UC** (con il fornitore). **COBIT 2019** = governance IT.

---
## 2. Sistemi informativi, architetture ICT, reti e TLC
### Modelli e protocolli
| OSI | Livello | Esempi |
|---|---|---|
| 7 | Applicazione | HTTP, DNS, SMTP, FTP, SNMP, LDAP |
| 6 | Presentazione | codifica, cifratura (TLS si colloca tra 4 e 7) |
| 5 | Sessione | — |
| 4 | **Trasporto** | **TCP** (affidabile, connesso, **3-way handshake** SYN/SYN-ACK/ACK), **UDP** (senza connessione: DNS, VoIP, streaming) |
| 3 | **Rete** | **IP**, ICMP (ping), routing (**OSPF** link-state/Dijkstra, **RIP** distance vector max 15 hop, **BGP** tra Autonomous System) |
| 2 | Collegamento dati | **Ethernet/MAC**, switch, **VLAN 802.1Q**, Wi-Fi **802.11**, ARP (IP→MAC) |
| 1 | Fisico | cavi, fibra, segnali |
- Il **TCP/IP** ha **4 livelli** (accesso alla rete, internet, trasporto, applicazione).
- **Porte**: 20/21 FTP · **22 SSH** · 23 Telnet · **25 SMTP** · **53 DNS** · 67/68 DHCP · **80 HTTP** · 110 POP3 · 143 IMAP · 161 SNMP · 389 LDAP · **443 HTTPS** · 3389 RDP · 3306 MySQL · 5432 PostgreSQL.
- **IPv4** 32 bit; **IPv6 128 bit**. Reti private (RFC 1918): **10/8, 172.16/12, 192.168/16**. **/24 → 254 host** utilizzabili (2^(32−n) − 2).
- **DHCP** = assegnazione automatica dell'IP (DORA: Discover, Offer, Request, Ack). **NAT** = traduce IP privati in IP pubblici. **DNS** = nome→IP (record **A** IPv4, **AAAA** IPv6, **CNAME** alias, **MX** posta, **NS**, **PTR** inverso, TXT).
- **Dispositivi**: hub (L1), **switch (L2)**, **router (L3)**, **firewall** (stateful, **WAF** a L7), **load balancer** L4 (IP/porte) vs **L7** (host, path, header HTTP) ⚠️.
- **VPN** (IPsec, TLS), **MPLS**, **SD-WAN**, **SDN** (separa il piano di controllo da quello dati), **5G** (eMBB, URLLC, mMTC; *network slicing*), **FTTH** (fibra fino a casa) vs FTTC; **SPC – Sistema Pubblico di Connettività** per le PA.

### Architetture
- **Client-server**, **n-tier** (presentazione / logica / dati), **SOA** (servizi + ESB), **microservizi** (indipendenti, ognuno con il proprio DB, deploy autonomo, comunicazione via API/eventi), **event-driven** (code e broker: Kafka, RabbitMQ → **disaccoppiamento**, comunicazione asincrona), **serverless/FaaS**.
- **API gateway**: punto unico di accesso (autenticazione, rate limiting, routing). **Service mesh**: gestione del traffico tra microservizi.
- **Cloud (NIST SP 800-145)**:
  - **5 caratteristiche**: self-service on demand, ampio accesso di rete, **resource pooling**, **elasticità rapida**, servizio misurato;
  - **3 modelli di servizio**: **IaaS / PaaS / SaaS** — responsabilità condivisa: con il SaaS il fornitore gestisce di più;
  - **4 modelli di deployment**: pubblico, privato, ibrido, community.
- **Scalabilità**: **orizzontale** (scale out, più nodi) vs **verticale** (scale up, più CPU/RAM). I servizi **stateless** facilitano lo scale-out.
- **Virtualizzazione**: hypervisor di **tipo 1 (bare metal)** vs **tipo 2 (hosted)**; i **container** condividono il **kernel** dell'host (più leggeri delle VM); **Kubernetes** orchestra i container (pod, deployment, **rolling update**).
- **Continuità operativa**:
  - **RPO** = massima **perdita di dati** tollerabile; **RTO** = **tempo** massimo di ripristino;
  - backup **3-2-1** (3 copie, 2 supporti, 1 off-site) + copia **immutabile**;
  - **RAID 0** (striping, nessuna ridondanza), **1** (mirroring), **5** (parità distribuita, tollera 1 disco), **6** (doppia parità, 2 dischi), **10** (mirror + stripe).
- **Storage**: **block** (SAN, volumi), **file** (NAS, NFS/SMB, gerarchia), **object** (chiave + dati + metadati, namespace piatto, S3) ⚠️.
- **Teorema CAP**: in caso di partizione di rete si sceglie tra **consistenza** e **disponibilità**.
- **Sistemi informativi**: **ERP** (gestionale integrato), **CRM**, **DMS** (gestione documentale), **BPM**, **DSS/BI**. Il **sistema informativo** (persone, processi, dati) è più ampio del **sistema informatico** (la sola parte automatizzata).

---
## 3. Data management
- **DBMS relazionale**: tabelle, **chiave primaria** (univoca, non nulla), **chiave esterna** (integrità referenziale), chiave candidata, superchiave.
- **ACID**: **Atomicità** (tutto o niente), **Consistenza**, **Isolamento**, **Durabilità** (persistenza dopo il commit, grazie al log).
- **Normalizzazione** ⚠️:
  - **1NF**: valori atomici;
  - **2NF**: 1NF + nessuna **dipendenza parziale** da una parte della chiave composta;
  - **3NF**: 2NF + nessuna **dipendenza transitiva** (attributo non chiave → altro attributo non chiave);
  - **BCNF**: ogni determinante è una **superchiave**.
- **SQL**:
  - **DDL** (CREATE, ALTER, DROP), **DML** (SELECT, INSERT, UPDATE, DELETE), **DCL** (GRANT, REVOKE), **TCL** (COMMIT, ROLLBACK, SAVEPOINT);
  - `WHERE` filtra **le righe**, `HAVING` filtra **i gruppi** (dopo `GROUP BY`);
  - **INNER JOIN** (solo righe corrispondenti), **LEFT JOIN** (tutte quelle della tabella sinistra), FULL OUTER, CROSS (prodotto cartesiano);
  - `DELETE` (DML, con WHERE, rollback possibile) vs `TRUNCATE` (svuota la tabella) vs `DROP` (elimina la struttura);
  - **vista** = query salvata; **indice** (B-tree) velocizza le letture ma rallenta le scritture; **EXPLAIN** = piano di esecuzione.
- **Isolamento** ⚠️:
  - anomalie: **dirty read**, **non-repeatable read**, **phantom read**;
  - livelli: Read Uncommitted < **Read Committed** (no dirty read) < **Repeatable Read** < **Serializable** (equivalente a un'esecuzione seriale).
- **NoSQL** (BASE, consistenza eventuale):
  - **document** (MongoDB, JSON);
  - **key-value** (Redis);
  - **column-family** (Cassandra, HBase);
  - **graph** (Neo4j, relazioni).
- **OLTP** (transazioni, normalizzato) vs **OLAP** (analisi, **data warehouse**, denormalizzato):
  - **schema a stella** = tabella dei **fatti** (misure) + tabelle delle **dimensioni**; **snowflake** = dimensioni normalizzate;
  - operazioni OLAP: drill-down, roll-up, slice, dice;
  - **ETL** (trasforma prima del caricamento) vs **ELT** (trasforma dentro la piattaforma);
  - **data lake** (dati grezzi, *schema-on-read*) vs data warehouse (*schema-on-write*); **lakehouse**; **data mart** = DW tematico.
- **Big data — 5V**: volume, velocità, varietà, veridicità, valore. **Hadoop** (HDFS + MapReduce), **Spark** (in-memory), streaming (Kafka, Flink).
- **Data governance**:
  - **DAMA-DMBOK** (11 aree; la governance al centro);
  - ruoli: **data owner** (responsabile del dato), **data steward** (qualità operativa), data custodian (tecnico);
  - **qualità dei dati (ISO/IEC 25012)**: accuratezza, completezza, coerenza, attualità…;
  - **metadati**: descrittivi, strutturali, amministrativi; **MDM** = master data.
- **Dati della PA**:
  - **open data per default** (art. 52 CAD); **D.Lgs. 36/2006** come modificato dal D.Lgs. 200/2021, che recepisce la **Direttiva (UE) 2019/1024**;
  - **dati di elevato valore** (Reg. di esecuzione UE 2023/138);
  - modello a **5 stelle** di Berners-Lee (★ licenza aperta … ★★★★★ Linked Open Data/RDF);
  - **Data Governance Act** (Reg. UE 2022/868): riuso dei dati protetti, intermediari, altruismo dei dati; **Data Act** (Reg. UE 2023/2854): accesso ai dati IoT, switching cloud;
  - **PDND** e **ANPR** (anagrafe unica); **basi di dati di interesse nazionale** (art. 60 CAD).

---
## 4. Programmazione, sviluppo software e tecnologie web
- **OOP**: **incapsulamento**, **ereditarietà**, **polimorfismo**, **astrazione**. Classe vs oggetto (istanza); overloading (stessa firma, parametri diversi, risolto **a compile time**) vs **overriding** (ridefinizione nella sottoclasse, **a runtime**).
- **SOLID** ⚠️: Single responsibility, Open/closed (aperto all'estensione, chiuso alla modifica), Liskov substitution, Interface segregation, **Dependency inversion** (i moduli di alto livello dipendono da **astrazioni**, l'implementazione è iniettata). Obiettivo: **alta coesione, basso accoppiamento** ⚠️.
- **Design pattern (GoF)**: creazionali (**Singleton**, Factory, Builder), strutturali (Adapter, Facade, Decorator, Proxy), comportamentali (**Observer**, Strategy, Command). **MVC** = Model-View-Controller.
- **Linguaggi**: compilati (C, Go) vs interpretati (Python, JS) vs bytecode e VM (Java/JVM, C#/.NET); tipizzazione statica vs dinamica; **paradigmi** imperativo, OOP, funzionale, dichiarativo (SQL).
- **Strutture dati e complessità**:
  - **stack = LIFO**, **coda = FIFO**, lista, albero, **hash table** (accesso O(1) medio), grafo;
  - **ricerca binaria O(log n)** (su array **ordinato**); ricerca lineare O(n);
  - ordinamenti: **merge sort** O(n log n), quicksort O(n log n) medio / O(n²) caso peggiore, bubble sort O(n²).
- **Ciclo di vita del software**: **waterfall** (sequenziale), **V-model** (test speculari alle fasi), iterativo/incrementale, **agile**, **DevOps** (CI/CD).
- **Test**:
  - **unit → integration → system → acceptance (UAT)**; **regression**;
  - **test pyramid** = molti unit test, meno test di integrazione, pochi end-to-end;
  - **black-box** (funzionale) vs **white-box** (strutturale, copertura del codice); **TDD** = scrivere prima il test.
- **Git**: commit, branch, merge, rebase, pull request; **CI/CD**: build → test → analisi statica (SAST) → artefatto → deploy; **IaC** (Terraform, Ansible).
- **Web**:
  - **HTTP** è **stateless**; metodi **GET** (sicuro, idempotente), **POST** (crea, **non** idempotente), **PUT** (sostituisce, idempotente), **PATCH** (modifica parziale), **DELETE** (idempotente);
  - **codici**: 1xx informativi · **2xx successo** (200 OK, **201 Created** ⚠️, 204 No Content) · **3xx redirect** (301 permanente, 302/307 temporaneo, 304 Not Modified) · **4xx errore del client** (400, **401 non autenticato**, **403 non autorizzato**, 404, 409 conflitto, 429 troppe richieste) · **5xx errore del server** (500, 502 Bad Gateway, 503 Service Unavailable);
  - **REST**: risorse identificate da URI, stateless, rappresentazioni JSON/XML; **OpenAPI** descrive le API (obbligatorio nelle LG di interoperabilità AgID, **ModI**); SOAP (XML/WSDL); **GraphQL**;
  - **frontend**: **HTML5** (struttura), **CSS** (presentazione), **JavaScript** (comportamento; DOM; AJAX/fetch asincrono); framework React, Angular, Vue; **responsive design**;
  - **sessione**: cookie (flag **Secure**, **HttpOnly**, **SameSite**), token; **CORS** allenta in modo controllato la **Same-Origin Policy**;
  - **autenticazione**: **OAuth 2.0** = autorizzazione delegata; **OpenID Connect** = identità sopra OAuth; **JWT** ⚠️: verificare **firma + exp + iss + aud**; **SAML** (usato da SPID, che ora supporta anche OIDC).
- **Accessibilità**: **L. 4/2004 (Legge Stanca)**; **WCAG 2.1 livello AA** / EN 301 549; principi **POUR** (percepibile, utilizzabile, comprensibile, robusto); **dichiarazione di accessibilità** annuale entro il **23 settembre** su AgID (form.agid.gov.it).
- **Riuso e open source**: art. 68-69 CAD, **Developers Italia**, `publiccode.yml`; **Designers Italia** (UI kit, modelli di siti).

---
## 5. Elementi di intelligenza artificiale
- **Paradigmi**:
  - **supervisionato** (dati etichettati: **classificazione** → classi; **regressione** → valore continuo);
  - **non supervisionato** (**clustering**, k-means; riduzione della dimensionalità con **PCA**; regole associative);
  - **per rinforzo** (agente, ambiente, **ricompensa**);
  - auto-supervisionato (alla base degli LLM).
- **Problemi**:
  - **overfitting** (ottimo sul training, scarso sul test → regolarizzazione, dropout, più dati, cross-validation); **underfitting**;
  - **compromesso bias-varianza**;
  - **data leakage**: informazioni del test o del futuro entrano nel training.
- **Metriche**:
  - **matrice di confusione** (TP, FP, FN, TN);
  - **accuracy** = (TP + TN)/totale; **precision** = TP/(TP + FP); **recall** (sensibilità) = TP/(TP + FN); **F1** = media armonica di precision e recall;
  - **AUC-ROC**; per la regressione **MAE**, **RMSE**;
  - con classi sbilanciate, l'accuracy inganna.
- **Reti neurali**:
  - percettrone, layer, **backpropagation** + **discesa del gradiente**; funzioni di attivazione **ReLU** (max(0, x)), sigmoide, **softmax** (probabilità multiclasse);
  - **CNN** → immagini; **RNN/LSTM** → sequenze; **Transformer** (meccanismo di **self-attention**, *"Attention is all you need"*, 2017) → **LLM**.
- **IA generativa**:
  - **LLM**, token, **embedding** (vettori semantici), finestra di contesto, *temperature*;
  - **allucinazioni**; **RAG** = recupero di documenti + generazione, per fondare le risposte su fonti; **fine-tuning**; **prompt injection** (OWASP Top 10 LLM);
  - **IA agentica** (uso di strumenti, MCP).
- **Normativa**:
  - **AI Act — Reg. (UE) 2024/1689**:
    - in vigore il **1° agosto 2024**; divieti dal **2/2/2025**; obblighi **GPAI** (modelli per finalità generali) dal **2/8/2025**; applicazione generale dal **2/8/2026**; alto rischio dell'All. I (prodotti) dal **2/8/2027** (il *Digital Omnibus* della Commissione propone rinvii per l'alto rischio);
    - **approccio basato sul rischio**: **inaccettabile** (vietato: social scoring, manipolazione, riconoscimento delle emozioni sul lavoro e a scuola, identificazione biometrica remota in tempo reale con eccezioni) → **alto rischio** (All. III: occupazione, istruzione, servizi pubblici essenziali, giustizia, migrazione… → gestione del rischio, governance dei dati, **sorveglianza umana**, log, documentazione, **FRIA** per i deployer pubblici) → **rischio limitato** (obblighi di **trasparenza**: chatbot, deepfake) → **minimo**;
    - obbligo di **alfabetizzazione IA** (art. 4);
  - **L. 132/2025** (legge italiana sull'IA): autorità nazionali **AgID** (notifica, promozione) e **ACN** (vigilanza); nella PA l'IA è uno **strumento di supporto**, la **decisione resta alla persona** responsabile del procedimento;
  - **Strategia italiana per l'IA 2024-2026**; **Linee guida AgID** per l'adozione e lo sviluppo dell'IA nella PA (`AGID/pdf/14`, `15`);
  - **ISO/IEC 42001** = sistema di gestione dell'IA; **ISO/IEC 22989** = terminologia; NIST AI RMF.

---
## 7. Trattamento dei dati personali e sicurezza
### GDPR — Reg. (UE) 2016/679 (+ D.Lgs. 196/2003 modificato dal D.Lgs. 101/2018)
| Art. | Contenuto |
|---|---|
| 4 | Definizioni: **dato personale**, trattamento, **pseudonimizzazione** (resta un dato personale) vs **anonimizzazione** (esce dal GDPR) |
| **5** | **Principi**: liceità, correttezza e trasparenza; **limitazione della finalità**; **minimizzazione**; **esattezza**; **limitazione della conservazione**; **integrità e riservatezza**; **responsabilizzazione (accountability)** |
| **6** | **Basi giuridiche**: consenso, contratto, **obbligo legale**, interessi vitali, **compito di interesse pubblico** (tipico della PA), legittimo interesse (**non** utilizzabile dalle PA nei compiti istituzionali) |
| 9 / 10 | **Categorie particolari** (salute, biometrici, genetici, origine etnica, opinioni…) / dati giudiziari |
| 12-22 | **Diritti**: informativa (13-14), **accesso (15)**, rettifica (16), **cancellazione/oblio (17)**, limitazione (18), **portabilità (20)**, opposizione (21), no a decisioni **solo automatizzate (22)**. Risposta entro **1 mese** (prorogabile di 2) |
| 24 / **25** | Titolare; **privacy by design e by default** |
| **28** | **Responsabile del trattamento** = tratta i dati **per conto** del titolare, con contratto o atto giuridico |
| 30 | **Registro** dei trattamenti |
| **32** | **Sicurezza**: misure **adeguate al rischio** (pseudonimizzazione, cifratura, riservatezza/integrità/disponibilità/resilienza, ripristino, test periodici) |
| **33** | **Data breach**: notifica al **Garante entro 72 ore** |
| 34 | Comunicazione agli **interessati** se il rischio è **elevato** |
| **35** | **DPIA** quando il trattamento presenta un **rischio elevato** |
| **37-39** | **DPO/RPD** **obbligatorio per le autorità pubbliche** |
| 44-49 | Trasferimenti extra-UE: decisione di adeguatezza (es. **EU-US Data Privacy Framework**), **clausole contrattuali standard**, BCR |
| 83 | **Sanzioni** fino a **20 mln € o 4%** del fatturato mondiale (10 mln / 2% per le violazioni minori) |

### Sicurezza informatica
- **Triade CIA**: riservatezza, integrità, disponibilità (+ autenticità, non ripudio).
- **Crittografia**:
  - **simmetrica** (AES; problema della distribuzione delle chiavi);
  - **asimmetrica** (RSA → fattorizzazione; ECC; chiave pubblica per cifrare e verificare, **privata** per decifrare e **firmare**); **Diffie-Hellman** = scambio della chiave su un canale insicuro;
  - **hash** (SHA-256; integrità; MD5 e SHA-1 deboli); **HMAC**; **firma digitale** = hash + chiave privata;
  - **PKI** e certificati **X.509**, **CA**; **TLS 1.3**; **PQC** (algoritmi post-quantum NIST: ML-KEM, ML-DSA).
- **Autenticazione**: fattori **conoscenza / possesso / inerenza** → **MFA**; SSO; **Zero Trust** ("never trust, always verify"); **minimo privilegio**; segregazione dei compiti; **PAM** (accessi privilegiati); **RBAC/ABAC**.
- **Minacce**:
  - **phishing**/spear phishing, **ransomware**, **DDoS**, malware (virus, worm, trojan), **MITM**, **APT**, social engineering, **supply chain**, **zero-day**;
  - **OWASP Top 10 (2021)**: **A01 Broken Access Control**, A02 Cryptographic Failures, **A03 Injection** (SQL injection → **query parametrizzate**), …; **XSS** → output encoding/CSP; **CSRF** → token anti-CSRF/SameSite.
- **Difesa**:
  - firewall, **IDS** (rileva) vs **IPS** (blocca), **SIEM** (correla i log), **SOC**, **EDR/XDR**, **WAF**, **DLP**, segmentazione, patching, backup immutabili;
  - **vulnerability assessment** (individua) vs **penetration test** (**sfrutta**); **CVE** (identificativo) / **CVSS** (gravità).
- **Quadri di riferimento**:
  - **ISO/IEC 27001:2022** (SGSI, **93 controlli in 4 temi**: organizzativi, persone, fisici, tecnologici), 27002, 27005 (rischio), 27701 (privacy);
  - **NIST CSF 2.0**: **Govern**, Identify, Protect, Detect, Respond, Recover; **Framework Nazionale per la Cybersecurity e la Data Protection**;
  - **Misure minime di sicurezza ICT per le PA** (circolare AgID 2/2017: livelli minimo, standard, avanzato).
- **Normativa cyber**:
  - **ACN** (D.L. 82/2021); **Perimetro di Sicurezza Nazionale Cibernetica** (D.L. 105/2019);
  - **NIS2 — Dir. (UE) 2022/2555**, recepita con il **D.Lgs. 138/2024**: soggetti **essenziali e importanti**; pre-allarme entro **24 h**, notifica entro **72 h**, relazione finale entro **1 mese**; responsabilità degli **organi di gestione**;
  - **L. 90/2024** (cybersicurezza delle PA: referente per la cybersicurezza, notifica degli incidenti);
  - **Cyber Resilience Act** (Reg. UE 2024/2847, prodotti con elementi digitali); **DORA** (Reg. UE 2022/2554, settore finanziario);
  - **eIDAS 2 (Reg. UE 2024/1183)**: **EUDI Wallet**; la **firma elettronica qualificata** equivale alla firma autografa.
