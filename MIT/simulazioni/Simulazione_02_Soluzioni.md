# Soluzioni — Simulazione Prova Scritta MIT-EPI n. 2

Non leggere questo file prima di aver completato `Simulazione_02_Quiz.md` in 70 minuti.

## Come calcolare il punteggio
Risposta esatta **+0,50**, mancata **0**, errata **-0,10** (bando, art. 6, comma 9). Massimo teorico 30 punti (60 × 0,50). Soglia di ammissione all'orale: **21/30**.

---

## Risposte

| # | Materia | Risposta | Motivazione sintetica |
|---|---|---|---|
| 1 | 1. Ingegneria SW/DevOps | **a** | Il limite WIP in Kanban evita l'accumulo di lavoro oltre la capacità del team, migliorando il flusso. |
| 2 | 2. Infrastrutture cloud/on-prem | **b** | "Measured service" è la caratteristica NIST che descrive il modello pay-as-you-go. |
| 3 | 3. DB/big data | **c** | La 1NF richiede valori atomici per cella e identificabilità univoca delle righe. |
| 4 | 4. Amministrazione DB/OS | **d** | L'incrementale salva solo le modifiche dall'ultimo backup (full o incrementale): serve l'intera catena in ordine. |
| 5 | 5. Progettazione ambienti cloud | **a** | "Retain" = scelta consapevole di non migrare, mantenendo il sistema on-premise. |
| 6 | 6. ML/IoT/IA | **b** | K-means richiede di fissare k (numero di cluster) prima di eseguire l'algoritmo. |
| 7 | 7. Cybersecurity | **c** | Lo Spoofing (furto/falsificazione d'identità) viola l'Autenticazione, nella classificazione STRIDE. |
| 8 | 8. BI/data mining | **d** | Lo snowflake schema normalizza ulteriormente le dimensioni in sotto-tabelle, a costo di più JOIN. |
| 9 | 9. Tutela dati personali | **a** | "Inequivocabile" richiede un'azione positiva e chiara, senza ambiguità (no silenzio-assenso). |
| 10 | 10. Normativa amm. digitale | **b** | Art. 9 CAD: open data by default, salvo eccezioni di privacy/sicurezza. |
| 11 | 11. Trasformazione digitale PA | **c** | API-first: i servizi vanno progettati esponendo API come modalità primaria di interazione. |
| 12 | 12. NIS | **d** | La NIS2 è stata recepita in Italia con il D.Lgs. 138/2024. |
| 13 | 1. Ingegneria SW/DevOps | **a** | Liskov Substitution: le sottoclassi devono poter sostituire le classi base senza rompere la correttezza. |
| 14 | 2. Infrastrutture cloud/on-prem | **b** | Multi-cloud = più provider pubblici (anti lock-in); hybrid cloud = combinazione pubblico+privato/on-prem. |
| 15 | 3. DB/big data | **c** | Leftmost prefix: un indice composito è pienamente efficace solo se la query parte dalla colonna più a sinistra. |
| 16 | 4. Amministrazione DB/OS | **d** | RBAC assegna i permessi a ruoli, non utente per utente. |
| 17 | 5. Progettazione ambienti cloud | **a** | Il rolling update aggiorna le repliche progressivamente, senza downtime, con rollback automatico in caso di errore. |
| 18 | 6. ML/IoT/IA | **b** | La PCA riduce la dimensionalità mantenendo la maggior parte della varianza informativa. |
| 19 | 7. Cybersecurity | **c** | DMARC/SPF/DKIM sono contromisure anti-spoofing del mittente email, cioè anti-phishing. |
| 20 | 8. BI/data mining | **d** | Il pivot scambia gli assi di visualizzazione del cubo OLAP. |
| 21 | 9. Tutela dati personali | **a** | L'art. 18 sospende il trattamento (non cancella i dati), es. in caso di contestazione dell'esattezza. |
| 22 | 10. Normativa amm. digitale | **b** | La FES non richiede identificazione forte né certificato qualificato; valore probatorio liberamente valutabile. |
| 23 | 11. Trasformazione digitale PA | **c** | Il DTD è interno alla PCM, senza personalità giuridica propria: nessun bilancio autonomo. |
| 24 | 12. NIS | **d** | Soglia dimensionale generale NIS2: medie/grandi imprese (≥50 dipendenti o ≥10 M€ di fatturato). |
| 25 | 1. Ingegneria SW/DevOps | **a** | GraphQL permette query mirate che riducono over-fetching/under-fetching rispetto a REST. |
| 26 | 2. Infrastrutture cloud/on-prem | **b** | In Active-Passive il nodo di backup resta inattivo finché non subentra per un guasto del primario. |
| 27 | 3. DB/big data | **c** | HDFS garantisce tolleranza ai guasti tramite la replica dei blocchi su più nodi. |
| 28 | 4. Amministrazione DB/OS | **d** | SIGKILL termina forzatamente e subito; SIGTERM chiede una terminazione controllata gestibile dal processo. |
| 29 | 5. Progettazione ambienti cloud | **a** | Il Namespace K8s isola logicamente ambienti/team/progetti all'interno dello stesso cluster. |
| 30 | 6. ML/IoT/IA | **b** | Il dropout è una tecnica di regolarizzazione che disattiva neuroni casualmente per ridurre l'overfitting. |
| 31 | 7. Cybersecurity | **c** | ASLR randomizza lo spazio di indirizzamento, contromisura tipica contro il buffer overflow. |
| 32 | 8. BI/data mining | **d** | Il data mining è la fase centrale del processo KDD (Knowledge Discovery in Databases). |
| 33 | 9. Tutela dati personali | **a** | Art. 22 GDPR: diritto a non essere sottoposti a decisioni basate unicamente su trattamento automatizzato/profilazione. |
| 34 | 10. Normativa amm. digitale | **b** | La PDND è un control-plane/broker di fiducia, non un data lake fisico centrale. |
| 35 | 11. Trasformazione digitale PA | **c** | Il PSN è concesso al consorzio TIM-CDP Equity-Sogei-Leonardo (PSN S.p.A.). |
| 36 | 12. NIS | **d** | L'art. 21 NIS2 richiede requisiti di sicurezza nei contratti con i fornitori, incluso il rischio dei sub-fornitori. |
| 37 | 1. Ingegneria SW/DevOps | **a** | gRPC si basa su HTTP/2 e Protocol Buffers (formato binario), per comunicazioni interne a bassa latenza. |
| 38 | 2. Infrastrutture cloud/on-prem | **b** | Direct Connect/ExpressRoute collegano on-premise e cloud senza passare da Internet pubblico. |
| 39 | 3. DB/big data | **c** | Spark elabora in-memory, evitando scritture su disco intermedie tipiche di MapReduce puro. |
| 40 | 4. Amministrazione DB/OS | **d** | Un albero AD raggruppa domini correlati; una foresta raggruppa uno o più alberi (livello gerarchico più ampio). |
| 41 | 5. Progettazione ambienti cloud | **a** | Nell'event-driven, un consumer non disponibile non blocca il producer, grazie al disaccoppiamento. |
| 42 | 6. ML/IoT/IA | **b** | RNN/LSTM sono specializzate su dati sequenziali/temporali, come le serie storiche IoT. |
| 43 | 7. Cybersecurity | **c** | La CA verifica l'identità e firma il certificato che lega una chiave pubblica a un'identità. |
| 44 | 8. BI/data mining | **d** | La coerenza (consistency) misura l'assenza di contraddizioni tra sistemi diversi sullo stesso dato. |
| 45 | 9. Tutela dati personali | **a** | Art. 34 GDPR: comunicazione agli interessati dovuta solo in caso di rischio elevato, salvo misure come la cifratura. |
| 46 | 10. Normativa amm. digitale | **b** | La fatturazione elettronica PA viaggia sulla rete PEPPOL, di cui AGID è Authority nazionale. |
| 47 | 11. Trasformazione digitale PA | **c** | I pareri di congruità sono vincolanti per gli acquisti tramite Consip/soggetti aggregatori su beni strategici. |
| 48 | 12. NIS | **d** | Il CVCN valuta/certifica la sicurezza di beni/servizi ICT critici prima del loro acquisto nel perimetro PSNC. |
| 49 | 1. Ingegneria SW/DevOps | **a** | Il DAST testa l'applicazione in esecuzione, in modalità black-box, a differenza del SAST sul codice sorgente. |
| 50 | 2. Infrastrutture cloud/on-prem | **b** | Nel modello di responsabilità condivisa, la sicurezza fisica dei data center resta sempre del provider. |
| 51 | 3. DB/big data | **c** | I graph database sono ottimizzati per relazioni complesse tra entità, come reti di frode. |
| 52 | 4. Amministrazione DB/OS | **d** | L'application pool di IIS isola i processi di app web diverse, contenendo i crash. |
| 53 | 5. Progettazione ambienti cloud | **a** | Credenziali/chiavi API vanno gestite in un vault dedicato, mai hardcoded nel codice o nelle immagini. |
| 54 | 6. ML/IoT/IA | **b** | La sorveglianza biometrica di massa in tempo reale in spazi pubblici è vietata (rischio inaccettabile, AI Act). |
| 55 | 7. Cybersecurity | **c** | "Recover" nel NIST CSF riguarda il ripristino dei servizi dopo un incidente, con lezioni apprese. |
| 56 | 8. BI/data mining | **d** | Il data steward è il responsabile operativo della qualità/gestione di uno specifico dominio di dati. |
| 57 | 9. Tutela dati personali | **a** | Il Codice Privacy resta in vigore soprattutto per le sanzioni penali in materia di trattamento illecito. |
| 58 | 10. Normativa amm. digitale | **b** | I 4 principi POUR: Percepibilità, Utilizzabilità, Comprensibilità, Robustezza. |
| 59 | 11. Trasformazione digitale PA | **c** | Designers Italia definisce linee guida di design per l'omogeneità dei servizi digitali pubblici. |
| 60 | 12. NIS | **d** | Dopo 24h e 72h, la NIS2 richiede una relazione finale entro un mese dall'incidente. |

---

## Riepilogo per materia

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

Dato il tuo risultato nella Simulazione 1 (20,4/30, punti deboli su Tutela dati personali, DB/big data, BI/data mining), presta particolare attenzione alle domande 3, 8, 9, 15, 20, 21, 27, 32, 33, 44, 45, 51, 56, 57 in questa simulazione: coprono gli stessi argomenti da un'angolazione diversa.
