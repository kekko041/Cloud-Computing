# Soluzioni — Simulazione Prova Scritta MIT-EPI n. 1

Non leggere questo file prima di aver completato `Simulazione_01_Quiz.md` in 70 minuti.

## Come calcolare il punteggio
Per ogni domanda: **risposta esatta = +0,50**, **mancata = 0**, **errata = -0,10** (regola del bando, art. 6, comma 9). Somma i punti su tutte le 60 domande: il massimo teorico è 30 (60 × 0,50). La soglia di ammissione alla prova orale è **21/30**, cioè devi totalizzare almeno 21 punti netti.

Esempio: 50 esatte, 5 errate, 5 non date → (50×0,50) + (5×-0,10) + (5×0) = 25 − 0,5 = **24,5/30** → superata.

| Esatte | Errate | Non date | Punteggio |
|---|---|---|---|
| 42 | 0 | 18 | 21,0 (soglia minima con zero errori) |
| 45 | 5 | 10 | 22,0 |
| 50 | 5 | 5 | 24,5 |
| 55 | 5 | 0 | 27,0 |

*Nota*: rispondere "a caso" ha valore atteso leggermente negativo (25% di probabilità di +0,50, 75% di -0,10 → E = 0,125 − 0,075 = +0,05 per domanda), quindi nel dubbio tra 2 opzioni conviene rispondere; se sei completamente all'oscuro su tutte e 4, meglio lasciare in bianco solo se hai già il punteggio di sicurezza.

---

## Risposte

| # | Materia | Risposta | Motivazione sintetica |
|---|---|---|---|
| 1 | 1. Ingegneria SW/DevOps | **a** | Il Product Owner gestisce il Product Backlog e le priorità; lo Scrum Master facilita il processo. |
| 2 | 2. Infrastrutture cloud/on-prem | **b** | CapEx = spesa in conto capitale (hardware acquistato); OpEx è la spesa operativa ricorrente tipica del cloud. |
| 3 | 3. DB/big data | **c** | Read Uncommitted è l'unico livello che permette la lettura di dati non ancora confermati (dirty read). |
| 4 | 4. Amministrazione DB/OS | **d** | Regola 3-2-1: 3 copie, 2 supporti diversi, 1 copia offsite. |
| 5 | 5. Progettazione ambienti cloud | **a** | Repurchase = sostituzione con un prodotto SaaS equivalente, diversamente da Rehost (spostamento as-is). |
| 6 | 6. ML/IoT/IA | **b** | La presenza/assenza di etichette nel dataset è la distinzione fondamentale tra supervisionato e non supervisionato. |
| 7 | 7. Cybersecurity | **c** | La lettura non autorizzata di un dato viola la Confidenzialità (uno dei tre pilastri CIA). |
| 8 | 8. BI/data mining | **d** | La fact table contiene le misure quantitative e le FK verso le dimensioni; le dimension table contengono gli attributi descrittivi. |
| 9 | 9. Tutela dati personali | **a** | Art. 20 GDPR: la portabilità si applica solo a trattamenti basati su consenso/contratto ed effettuati con mezzi automatizzati. |
| 10 | 10. Normativa amm. digitale | **b** | SPID prevede 3 livelli di sicurezza crescente (L1, L2, L3). |
| 11 | 11. Trasformazione digitale PA | **c** | Il Piano Triennale è strutturato in Strategia, Tecnologie (componenti), Strumenti. |
| 12 | 12. NIS | **d** | I Soggetti Essenziali hanno vigilanza ex ante (proattiva), gli Importanti prevalentemente ex post. |
| 13 | 1. Ingegneria SW/DevOps | **a** | Singleton: pattern creazionale, istanza unica con punto di accesso globale. |
| 14 | 2. Infrastrutture cloud/on-prem | **b** | 0,1% di 8760 ore/anno ≈ 8,76 ore di downtime massimo tollerato. |
| 15 | 3. DB/big data | **c** | La Foreign Key referenzia la Primary Key di un'altra tabella, garantendo l'integrità referenziale. |
| 16 | 4. Amministrazione DB/OS | **d** | La replica sincrona attende l'ack di tutte le repliche prima di confermare la scrittura: più sicura ma più lenta. |
| 17 | 5. Progettazione ambienti cloud | **a** | Il Service fornisce un endpoint di rete stabile per Pod che cambiano IP nel tempo. |
| 18 | 6. ML/IoT/IA | **b** | Random Forest = bagging, ensemble di alberi su sottoinsiemi casuali di dati/feature, per ridurre la varianza. |
| 19 | 7. Cybersecurity | **c** | La chiave privata (segreta, solo del firmatario) firma l'hash; la verifica con la chiave pubblica non richiede di condividere segreti. |
| 20 | 8. BI/data mining | **d** | Roll-up = aggregazione, riduzione del dettaglio (es. da regione a nazione); il drill-down fa l'opposto. |
| 21 | 9. Tutela dati personali | **a** | I dati sanitari sono "categorie particolari" ex art. 9 GDPR, con condizioni di trattamento più stringenti. |
| 22 | 10. Normativa amm. digitale | **b** | Art. 3 CAD: diritto all'uso delle tecnologie, diritto soggettivo azionabile verso la PA. |
| 23 | 11. Trasformazione digitale PA | **c** | Il principio "servizi progettati sull'utente" è lo user-centered design tra i 10 principi del Piano Triennale. |
| 24 | 12. NIS | **d** | Art. 20 NIS2: responsabilità personale del management per negligenza grave nella supervisione della cybersicurezza. |
| 25 | 1. Ingegneria SW/DevOps | **a** | PUT è idempotente e sostituisce interamente una risorsa; POST crea e non è idempotente. |
| 26 | 2. Infrastrutture cloud/on-prem | **b** | Una Region raggruppa più AZ (data center separati con alimentazione/rete indipendenti) in un'area geografica. |
| 27 | 3. DB/big data | **c** | Column-family (es. Cassandra/HBase) è ottimizzata per scritture massive di dati time-series come i log IoT. |
| 28 | 4. Amministrazione DB/OS | **d** | `systemctl start <servizio>` è il comando standard di systemd per avviare un servizio. |
| 29 | 5. Progettazione ambienti cloud | **a** | Orizzontale = numero di repliche di Pod; verticale = risorse (CPU/memoria) assegnate a un singolo Pod. |
| 30 | 6. ML/IoT/IA | **b** | CoAP è pensato per microcontrollori a risorse limitate, su UDP, con semantica REST-like. |
| 31 | 7. Cybersecurity | **c** | Il CVSS esprime la gravità di una vulnerabilità su una scala da 0 a 10. |
| 32 | 8. BI/data mining | **d** | La confidenza misura l'affidabilità della regola (probabilità di B dato A); il supporto misura la frequenza della combinazione. |
| 33 | 9. Tutela dati personali | **a** | Il DPO è sempre obbligatorio per le autorità pubbliche, a prescindere dalla natura dei dati trattati. |
| 34 | 10. Normativa amm. digitale | **b** | La PEC, per le ricevute di accettazione/consegna, ha valore equivalente a una raccomandata con ricevuta di ritorno. |
| 35 | 11. Trasformazione digitale PA | **c** | Dal 2023 la qualificazione di sicurezza dei CSP per la PA è passata ad ACN. |
| 36 | 12. NIS | **d** | Il CSIRT Italia è incardinato presso ACN, punto di contatto unico per le notifiche NIS2. |
| 37 | 1. Ingegneria SW/DevOps | **a** | Ansible è agentless, basato su SSH e playbook YAML; Terraform è dichiarativo ma per il provisioning infrastrutturale. |
| 38 | 2. Infrastrutture cloud/on-prem | **b** | Il WAF filtra specificamente il traffico applicativo HTTP/S (SQLi, XSS); un firewall generico lavora a livello di rete/porte. |
| 39 | 3. DB/big data | **c** | La fase Reduce aggrega i risultati parziali prodotti dalla fase Map. |
| 40 | 4. Amministrazione DB/OS | **d** | `sudo` lascia una traccia di audit (chi, cosa, quando), a differenza del login diretto come root. |
| 41 | 5. Progettazione ambienti cloud | **a** | Il configuration drift è il disallineamento causato da modifiche manuali non versionate, che l'IaC previene. |
| 42 | 6. ML/IoT/IA | **b** | Il fog computing è un livello intermedio tra edge e cloud, su nodi di rete come router/gateway locali. |
| 43 | 7. Cybersecurity | **c** | "Detect" nel NIST CSF è la funzione dedicata al monitoraggio per l'individuazione tempestiva degli incidenti. |
| 44 | 8. BI/data mining | **d** | SMART: Specific, Measurable, Achievable, Relevant, Time-bound. |
| 45 | 9. Tutela dati personali | **a** | Art. 32 GDPR richiede esplicitamente riservatezza, integrità, disponibilità e resilienza dei sistemi di trattamento. |
| 46 | 10. Normativa amm. digitale | **b** | IPA = domicili digitali (PEC) delle PA; INAD = domicili digitali di cittadini/professionisti/imprese. |
| 47 | 11. Trasformazione digitale PA | **c** | Il TCO comprende manutenzione, formazione, rischio di lock-in e consumo energetico, oltre al prezzo d'acquisto. |
| 48 | 12. NIS | **d** | Le sanzioni NIS2 per i Soggetti Essenziali arrivano fino a 10 milioni di euro o il 2% del fatturato globale. |
| 49 | 1. Ingegneria SW/DevOps | **a** | SQL Injection rientra nella categoria OWASP "Injection". |
| 50 | 2. Infrastrutture cloud/on-prem | **b** | Il vendor lock-in è la dipendenza tecnica/contrattuale che rende costosa la migrazione verso un altro provider. |
| 51 | 3. DB/big data | **c** | Rifiutare di rispondere pur di non dare dati non aggiornati = privilegiare Consistency + Partition tolerance (CP). |
| 52 | 4. Amministrazione DB/OS | **d** | I cmdlet PowerShell seguono la convenzione Verbo-Sostantivo (es. Get-Process). |
| 53 | 5. Progettazione ambienti cloud | **a** | Le immagini Docker sono distribuite tramite registry (Docker Hub o registry privati). |
| 54 | 6. ML/IoT/IA | **b** | Un chatbot che deve dichiarare la propria natura artificiale rientra nel rischio "limitato" (obblighi di trasparenza) dell'AI Act. |
| 55 | 7. Cybersecurity | **c** | Il non ripudio impedisce a un soggetto di negare un'azione compiuta, tipicamente tramite log protetti e firme digitali. |
| 56 | 8. BI/data mining | **d** | Slice fissa un valore su una dimensione; dice filtra su più dimensioni contemporaneamente. |
| 57 | 9. Tutela dati personali | **a** | Art. 21 GDPR: il diritto di opposizione riguarda i trattamenti basati su legittimo interesse o interesse pubblico. |
| 58 | 10. Normativa amm. digitale | **b** | eIDAS garantisce il riconoscimento reciproco transfrontaliero degli schemi di identità digitale notificati. |
| 59 | 11. Trasformazione digitale PA | **c** | Il D.Lgs. 33/2013 disciplina gli obblighi di pubblicazione proattiva ("Amministrazione Trasparente"). |
| 60 | 12. NIS | **d** | DORA rende il TLPT un obbligo mandatorio specifico per il settore finanziario; la NIS2 non ha uno standard altrettanto vincolante. |

---

## Riepilogo per materia (per capire dove concentrare il ripasso)

| Materia | Domande | File di studio |
|---|---|---|
| 1. Ingegneria software/DevOps | 1, 13, 25, 37, 49 | [`MIT/studio/01_ingegneria_software_devops.md`](../studio/01_ingegneria_software_devops.md) |
| 2. Infrastrutture cloud/on-premise | 2, 14, 26, 38, 50 | [`MIT/studio/02_infrastrutture_cloud_onpremise.md`](../studio/02_infrastrutture_cloud_onpremise.md) |
| 3. Database/big data | 3, 15, 27, 39, 51 | [`MIT/studio/03_database_data_analysis_bigdata.md`](../studio/03_database_data_analysis_bigdata.md) |
| 4. Amministrazione DB/OS | 4, 16, 28, 40, 52 | [`MIT/studio/04_amministrazione_db_sistemi_operativi.md`](../studio/04_amministrazione_db_sistemi_operativi.md) |
| 5. Progettazione ambienti cloud | 5, 17, 29, 41, 53 | [`MIT/studio/05_progettazione_ambienti_cloud.md`](../studio/05_progettazione_ambienti_cloud.md) |
| 6. ML/IoT/IA | 6, 18, 30, 42, 54 | [`MIT/studio/06_machine_learning_iot_ia.md`](../studio/06_machine_learning_iot_ia.md) |
| 7. Cybersecurity | 7, 19, 31, 43, 55 | [`MIT/studio/07_cybersecurity_crittografia.md`](../studio/07_cybersecurity_crittografia.md) |
| 8. BI/data mining | 8, 20, 32, 44, 56 | [`MIT/studio/08_business_intelligence_data_mining.md`](../studio/08_business_intelligence_data_mining.md) |
| 9. Tutela dati personali | 9, 21, 33, 45, 57 | [`MIT/studio/09_tutela_dati_personali.md`](../studio/09_tutela_dati_personali.md) |
| 10. Normativa amm. digitale | 10, 22, 34, 46, 58 | [`MIT/studio/10_normativa_amministrazione_digitale.md`](../studio/10_normativa_amministrazione_digitale.md) |
| 11. Trasformazione digitale PA | 11, 23, 35, 47, 59 | [`MIT/studio/11_trasformazione_digitale_pa.md`](../studio/11_trasformazione_digitale_pa.md) |
| 12. NIS | 12, 24, 36, 48, 60 | [`MIT/studio/12_nis_network_information_security.md`](../studio/12_nis_network_information_security.md) |

Se sbagli 3+ domande sulla stessa materia, torna al file di studio corrispondente prima di passare alla prossima simulazione.
