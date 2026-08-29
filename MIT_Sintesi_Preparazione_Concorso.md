# Sintesi Preparazione Concorso MIT — Codice EPI (Specialista Informatico)
*Basata su `MIT/documentazione/Bando Ministero delle infrastrutture e dei trasporti - EP-1.pdf` e sul decreto di nomina commissione (5 agosto 2026)*

Concorso pubblico, per titoli ed esami, per il reclutamento di **105 unità** nell'Area delle Elevate Professionalità (EP) del Ministero delle Infrastrutture e dei Trasporti. Questa sintesi copre il codice **EPI** (7 posti, famiglia professionale tecnica in ambito informatico, posizione *Specialista informatico*), per il quale la commissione esaminatrice è già stata nominata — segnale che la prova scritta è prossima.

---

## 0. Logistica e regole del concorso (dati da ricordare)

| Elemento | Dettaglio |
|---|---|
| Codice concorso | **EPI** — 7 posti, famiglia tecnica in ambito informatico, *Specialista informatico* |
| Commissione (D.D. 5/8/2026) | Presidente: Prof. Giovanni Michele Pinna; Componenti: Ing. Giorgio Agrifoglio, Ing. Daniele Lazzaretti; Supplente: Ing. Giovanni Improta; Segretario: Dott. Carlo Annunziato Garufi |
| Struttura prova | Scritto (art. 6) → Orale (art. 7, per chi supera lo scritto) → Valutazione titoli (art. 8, per chi supera l'orale) |
| Prova scritta | **60 quesiti a risposta multipla in 70 minuti**, su piattaforma informatica; sedi anche decentrate/sessioni multiple |
| Punteggio scritto | Risposta esatta **+0,50**; mancata risposta **0**; risposta errata **-0,10**. Soglia ammissione orale: **≥ 21/30** |
| Prova orale | Colloquio interdisciplinare sulle materie dello scritto + verifica inglese (≥B2) + competenze digitali/ICT. Soglia: **≥ 21/30** |
| Valutazione titoli | Max **10 punti**: dottorato attinente 3, diploma specializzazione 2, master II livello 2, master I livello 1, altra laurea magistrale 1, abilitazione attinente 1 |
| Requisiti ammissione EPI | ≥3 anni esperienza specialistica/di responsabilità nel settore informatico (pubblico, privato o autonomo) **oppure** dottorato attinente (esonera dall'esperienza); laurea tra LM-18, LM-31, LM-32, LM-66, LM-91, LM-28, LM-29, LM-27, LM-DATA; più master/diploma di specializzazione/dottorato/abilitazione attinenti; inglese certificato ≥B2 |
| Riserve | 30% volontari FF.AA., 15% servizio civile universale, 25% dipendenti MIT — cumulabili nel limite del 50% dei posti per codice |

**Materie della prova scritta EPI** (dal bando, art. 6 comma 10):
1. Ingegneria del software: analisi, progettazione sistemi informatici; sviluppo componenti software, web application e mobile, API e integrazione sistemi, framework sui principali linguaggi di programmazione; ciclo di vita **DevOps**, **Security & Privacy by Design**
2. Infrastrutture ICT on-premise e cloud
3. Database, data analysis e big data
4. Amministrazione di database e sistemi operativi Unix/Windows Server
5. Progettazione e sviluppo ambienti cloud
6. Machine learning, IoT, intelligenza artificiale (IA)
7. Cybersecurity, analisi delle vulnerabilità, implementazione soluzioni crittografiche
8. Meccanismi di business intelligence e data mining
9. Tutela dei dati personali
10. Normativa nazionale ed europea in materia di amministrazione digitale
11. Trasformazione digitale della pubblica amministrazione
12. Disciplina nazionale ed europea NIS (Network and Information Security)

## Materiale di studio completo per materia

Per ogni materia dello scritto è disponibile un file di approfondimento autosufficiente in [`MIT/studio/`](MIT/studio/), con definizioni, confronti, tabelle, diagrammi e domande di autoverifica in stile esame:

| # | Materia | File di studio |
|---|---|---|
| 1 | Ingegneria del software, DevOps, Security & Privacy by Design | [`MIT/studio/01_ingegneria_software_devops.md`](MIT/studio/01_ingegneria_software_devops.md) |
| 2 | Infrastrutture ICT on-premise e cloud | [`MIT/studio/02_infrastrutture_cloud_onpremise.md`](MIT/studio/02_infrastrutture_cloud_onpremise.md) |
| 3 | Database, data analysis e big data | [`MIT/studio/03_database_data_analysis_bigdata.md`](MIT/studio/03_database_data_analysis_bigdata.md) |
| 4 | Amministrazione DB e sistemi operativi Unix/Windows Server | [`MIT/studio/04_amministrazione_db_sistemi_operativi.md`](MIT/studio/04_amministrazione_db_sistemi_operativi.md) |
| 5 | Progettazione e sviluppo ambienti cloud | [`MIT/studio/05_progettazione_ambienti_cloud.md`](MIT/studio/05_progettazione_ambienti_cloud.md) |
| 6 | Machine learning, IoT, intelligenza artificiale | [`MIT/studio/06_machine_learning_iot_ia.md`](MIT/studio/06_machine_learning_iot_ia.md) |
| 7 | Cybersecurity, vulnerabilità, crittografia | [`MIT/studio/07_cybersecurity_crittografia.md`](MIT/studio/07_cybersecurity_crittografia.md) |
| 8 | Business intelligence e data mining | [`MIT/studio/08_business_intelligence_data_mining.md`](MIT/studio/08_business_intelligence_data_mining.md) |
| 9 | Tutela dei dati personali | [`MIT/studio/09_tutela_dati_personali.md`](MIT/studio/09_tutela_dati_personali.md) |
| 10 | Normativa nazionale ed europea in materia di amministrazione digitale | [`MIT/studio/10_normativa_amministrazione_digitale.md`](MIT/studio/10_normativa_amministrazione_digitale.md) |
| 11 | Trasformazione digitale della pubblica amministrazione | [`MIT/studio/11_trasformazione_digitale_pa.md`](MIT/studio/11_trasformazione_digitale_pa.md) |
| 12 | Disciplina nazionale ed europea NIS | [`MIT/studio/12_nis_network_information_security.md`](MIT/studio/12_nis_network_information_security.md) |

Le sezioni 1-7 qui sotto restano come **ripasso rapido/indice mnemonico**; per lo studio effettivo usa i file collegati sopra, più approfonditi e con domande di autoverifica.

---

## 1. Ingegneria del software: ciclo di vita e DevSecOps
* **SDLC (Software Development Life Cycle):** Requisiti → Design → Sviluppo → Test → Rilascio → Manutenzione. I modelli agili (Scrum, Kanban) sostituiscono il waterfall nella PA moderna per iterazioni brevi e feedback continuo, richiesto anche dal PNRR per rendicontazione a milestone.
* **DevOps:** integra sviluppo (Dev) e operations (Ops) in una pipeline continua:
  * **CI (Continuous Integration):** merge frequenti + build/test automatici (evita "integration hell").
  * **CD (Continuous Delivery/Deployment):** rilascio automatizzato e ripetibile, spesso con containerizzazione (Docker) e orchestrazione (Kubernetes/OCI-compliant runtime).
  * **IaC (Infrastructure as Code):** Terraform/Ansible per provisioning riproducibile e versionato (coerente con le linee guida AGID su automazione infrastrutturale).
* **DevSecOps / Security & Privacy by Design:** la sicurezza e la protezione dati non sono un livello aggiunto a fine progetto, ma requisiti architetturali fin dalla fase di design (coerente con art. 25 GDPR — *Data Protection by Design and by Default*):
  * **SAST** (Static Application Security Testing) su codice sorgente; **DAST** (Dynamic) su applicazione in esecuzione; **SCA** (Software Composition Analysis) per vulnerabilità nelle dipendenze/librerie open source.
  * **Threat Modeling** (es. STRIDE) in fase di design, prima di scrivere codice — vedi Linee Guida AGID su Modellazione delle Minacce.
  * **OWASP Top 10**: prevenzione di Injection, Broken Access Control, vulnerabilità crittografiche.
* **API e integrazione di sistemi:** REST (stateless, risorse via URI, verbi HTTP) vs SOAP (protocollo strutturato, WSDL, maggiore overhead ma contratti rigidi — ancora usato in sistemi legacy PA). Sicurezza: OAuth 2.0/OIDC per autorizzazione, mTLS per autenticazione server-to-server (vedi ModI/PDND in `AGID_Sintesi_Preparazione_Concorso.md` §1).
* **Sviluppo web/mobile:** architetture a microservizi vs monolitiche; pattern MVC; frontend SPA (Single Page Application) che consumano API backend; considerazioni su accessibilità (WCAG 2.1) per applicazioni PA.

## 2. Infrastrutture ICT on-premise e cloud
* **On-premise:** infrastruttura fisica gestita internamente (data center proprietari). Vantaggi: controllo diretto, nessuna dipendenza da terzi; svantaggi: costi CapEx elevati, scalabilità limitata, responsabilità piena su continuità e disaster recovery.
* **Modelli cloud:** IaaS (infrastruttura virtualizzata, es. VM), PaaS (piattaforma gestita, es. DB-as-a-Service), SaaS (applicazione completa). Il principio **Cloud First** della PA italiana privilegia SaaS > PaaS > IaaS quando possibile (vedi §2 di `AGID_Sintesi_Preparazione_Concorso.md`).
* **Architetture ibride:** combinano on-premise/cloud privato (per dati critici/strategici, vedi PSN) con cloud pubblico qualificato (per carichi ordinari), bilanciando sovranità del dato e elasticità.
* **Alta disponibilità e disaster recovery:** ridondanza (N+1, multi-AZ), RTO (Recovery Time Objective) e RPO (Recovery Point Objective) come metriche chiave per il dimensionamento delle soluzioni di continuità operativa — tema centrale anche per la resilienza richiesta da NIS2/DORA.

## 3. Database, data analysis e big data
* **Modelli di dati:** relazionale (RDBMS — PostgreSQL, Oracle, SQL Server; ACID, normalizzazione) vs NoSQL (document store come MongoDB, key-value come Redis, column-family come Cassandra; privilegiano scalabilità orizzontale e schema flessibile, spesso a scapito della piena coerenza — teorema **CAP**: Consistency, Availability, Partition tolerance, se ne possono garantire solo due su tre in caso di partizione di rete).
* **Big Data — i "V":** Volume, Velocity, Variety (talvolta anche Veracity, Value). Architetture di riferimento: **Data Lake** (dati grezzi, schema-on-read) vs **Data Warehouse** (dati strutturati, schema-on-write, ottimizzati per query analitiche/OLAP).
* **Elaborazione:** batch processing (es. Hadoop/Spark per grandi volumi non real-time) vs stream processing (es. Kafka per dati in tempo reale, IoT, monitoraggio infrastrutture).
* **Data analysis:** pipeline ETL/ELT (Extract-Transform-Load) per portare dati grezzi in forma analizzabile; data quality e data governance come prerequisiti per analisi affidabili.

## 4. Amministrazione di database e sistemi operativi Unix/Windows Server
* **Amministrazione DB:** backup (full/incrementale/differenziale), tuning delle query (indici, query plan), gestione utenze e permessi (principio del privilegio minimo), replica (master-slave/multi-master) per HA e load balancing in lettura.
* **Unix/Linux Server:** gestione processi, filesystem, permessi (rwx, utente/gruppo/altri), shell scripting per automazione, gestione pacchetti (apt/yum), systemd per servizi, logging centralizzato (syslog).
* **Windows Server:** Active Directory (autenticazione centralizzata, Group Policy), IIS come web server, PowerShell per amministrazione scriptata, gestione ruoli/feature via Server Manager.
* **Hardening:** disattivazione servizi non necessari, patch management, segmentazione di rete, logging e auditing degli accessi — collegamento diretto con i requisiti di sicurezza NIS2 (vedi §9 di `AGID_Sintesi_Preparazione_Concorso.md`).

## 5. Progettazione e sviluppo ambienti cloud
* **Containerizzazione:** Docker (immagini immutabili, isolamento a livello di processo) e orchestrazione con Kubernetes (pod, service, deployment, auto-scaling, self-healing) — architettura di riferimento per applicazioni cloud-native nella PA.
* **Serverless/FaaS:** funzioni event-driven senza gestione diretta dei server, utili per carichi variabili o task episodici.
* **Percorsi di migrazione** (Rehost/Replatform/Rearchitect) e classificazione dati (Ordinari/Critici/Strategici) con relativo obbligo di PSN per i dati critici/strategici: vedi §2 e §8 di `AGID_Sintesi_Preparazione_Concorso.md` per il dettaglio completo — argomento ad alta probabilità d'esame anche qui, data la specificità MIT su infrastrutture critiche (trasporti, dighe, ferrovie).
* **Qualificazione CSP:** solo Cloud Service Provider accreditati ACN/AGID possono ospitare workload della PA.

## 6. Machine Learning, IoT, Intelligenza Artificiale
* **ML — tipologie:** supervisionato (classificazione/regressione su dati etichettati), non supervisionato (clustering, riduzione dimensionalità), per rinforzo (agente che apprende da reward/penalty in un ambiente). Applicazioni tipiche in ambito MIT: manutenzione predittiva su infrastrutture (ponti, ferrovie), analisi del traffico.
* **IoT (Internet of Things):** sensori distribuiti che raccolgono dati da infrastrutture fisiche (es. monitoraggio strutturale di ponti/dighe — rilevante per i profili EPT-01/EPT-02 ma anche per l'architettura dati EPI); protocolli leggeri (MQTT, CoAP) per comunicazione a basso consumo/banda.
* **IA nella PA:** normata dall'**AI Act** (approccio risk-based) — vedi §11 di `AGID_Sintesi_Preparazione_Concorso.md`. Per un sistema ML che supporta decisioni su infrastrutture critiche, ricordare i requisiti di sistema "ad alto rischio": tracciabilità, trasparenza, supervisione umana (human-in-the-loop).

## 7. Business Intelligence e Data Mining
* **BI (Business Intelligence):** strumenti per trasformare dati grezzi in informazioni decisionali — dashboard, cruscotti KPI, reportistica direzionale. Nella PA supporta il monitoraggio degli investimenti pubblici e la rendicontazione PNRR.
* **Data mining — tecniche principali:** clustering (segmentazione), association rule mining (pattern ricorrenti), anomaly detection (rilevamento frodi/anomalie, rilevante anche per cybersecurity e audit).
* **OLAP vs OLTP:** OLTP (Online Transaction Processing) ottimizzato per transazioni frequenti e piccole (sistemi operativi gestionali); OLAP (Online Analytical Processing) ottimizzato per query complesse su grandi volumi storici (data warehouse, cubi multidimensionali).

---

## 8. Raccordo con le fonti normative già presenti nel repository

I file di studio in `MIT/studio/` per le materie 9-12 (normative) sono costruiti citando esplicitamente e restando coerenti con le fonti già presenti nel repository, che restano utili per un ulteriore approfondimento:

| Materia del bando EPI | Fonti di raccordo nel repository |
|---|---|
| Cybersecurity, vulnerabilità, crittografia | `AGID_Sintesi_Preparazione_Concorso.md` §9 (NIS2), `AGID/pdf/` (Sicurezza API, Sviluppo Sicuro, Modellazione delle Minacce), `Sintesi_Firma_Digitale.md` |
| Tutela dei dati personali | `AGID_Sintesi_Preparazione_Concorso.md` §4 (GDPR/eIDAS), `Sintesi_Firma_Digitale.md` |
| Normativa amministrazione digitale (CAD) | `AGID_Sintesi_Preparazione_Concorso.md` §4, §6, `Sintesi_CAD_e_Appalti_ICT.md`, `Sintesi_Normazione_Interoperabilita.md` |
| Trasformazione digitale della PA | `AGID_Sintesi_Preparazione_Concorso.md` §5 (Piano Triennale), §7 (Governance DTD/AGID/ACN), `Sintesi_PM_Programmazione_Budget.md`, `Sintesi_Architetture_Qualita_Migrazione.md` |
| Disciplina NIS | `AGID_Sintesi_Preparazione_Concorso.md` §9, `Sintesi_ACN_Cybersicurezza_PMI.md`, `Guida Tecnica ai Framework di Governance IA e Resilienza Digitale UE.md`, `fonti_banca_italia/` (DORA, TIBER-IT) |
| Cloud (classificazione, PSN, qualificazione) | `AGID_Sintesi_Preparazione_Concorso.md` §2, §8 |

*Sintesi per l'esame*: la sovrapposizione con le materie AGID non è casuale — entrambi i concorsi valutano lo stesso corpus normativo-tecnico della trasformazione digitale della PA italiana. Prepara un'unica base di conoscenza su GDPR/NIS2/Cloud/AI Act e integrala con le competenze più "hard" (DevOps, DB, ML) specifiche del profilo EPI trattate nei file di studio.
