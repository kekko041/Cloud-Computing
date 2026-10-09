# Domande Aperte per l'Orale — Concorso MIT-EPI (Specialista Informatico)
*36 domande aperte (3 per ciascuna delle 12 materie), in stile colloquio. Per ognuna: la domanda e i punti chiave da toccare nella risposta (non una risposta scritta da imparare a memoria — usa lo schema in 5 punti di [`00_metodo_e_struttura_colloquio.md`](00_metodo_e_struttura_colloquio.md) e allenati a esporla a voce).*

---

## 1. Ingegneria del software, DevOps, Security & Privacy by Design
*(ripasso: [`MIT/studio/01_ingegneria_software_devops.md`](../studio/01_ingegneria_software_devops.md))*

**1.1** — Progetta ad alto livello un sistema per la gestione digitale delle pratiche di un ufficio del MIT (es. autorizzazioni per interventi su infrastrutture). Monolite o microservizi? Perché?
- Parti dai requisiti: dimensione del team, complessità del dominio, necessità di scalare parti specifiche.
- Se il dominio è semplice/team piccolo → monolite (minore complessità operativa iniziale); se serve scalabilità selettiva e isolamento dei guasti su un dominio complesso → microservizi.
- Nomina esplicitamente il trade-off: scalabilità/isolamento vs complessità di orchestrazione.
- Aggiungi un cenno a sicurezza (API Gateway, autenticazione) e, se containerizzato, a CI/CD.

**1.2** — Differenza tra Continuous Delivery e Continuous Deployment: quale preferiresti in un contesto PA e perché?
- Definizioni precise (approvazione manuale vs rilascio automatico).
- In un contesto PA regolamentato, spesso si preferisce Continuous Delivery (controllo/responsabilità sull'ultimo step) ma automatizzando il più possibile a monte (build, test, SAST, controlli di sicurezza) prima della promozione — cita la sequenza corretta della pipeline CI.

**1.3** — Come applicheresti il principio di Security by Design nello sviluppo di una API che espone dati sullo stato di un'infrastruttura critica (es. un ponte)?
- Sicurezza incorporata fin dal design, non aggiunta dopo (art. 25 GDPR, Privacy by Design/Default).
- Threat modeling (STRIDE) prima di scrivere codice.
- Autenticazione/autorizzazione (OAuth2/OIDC, mTLS per server-to-server), minimizzazione dei dati esposti, rate limiting via API Gateway, logging/audit.
- Collegamento a NIS2 se l'infrastruttura è critica.

---

## 2. Infrastrutture ICT on-premise e cloud
*(ripasso: [`MIT/studio/02_infrastrutture_cloud_onpremise.md`](../studio/02_infrastrutture_cloud_onpremise.md))*

**2.1** — Il MIT deve scegliere dove ospitare un nuovo sistema di monitoraggio in tempo reale del traffico autostradale: on-premise, cloud pubblico o ibrido?
- Parti dalla classificazione del dato/servizio (Ordinario/Critico/Strategico, Strategia Cloud Italia).
- Se critico → PSN o infrastruttura ibrida; componenti meno sensibili (es. dashboard pubblica) → cloud pubblico qualificato.
- Cita i vantaggi di elasticità del cloud per gestire picchi di traffico dati, e la qualificazione CSP come prerequisito.

**2.2** — Cos'è il modello di "responsabilità condivisa" nel cloud, e come cambia tra IaaS, PaaS e SaaS?
- Spiega la ripartizione provider/cliente con un esempio concreto (es. il patching del sistema operativo è a carico del cliente in IaaS, del provider in PaaS/SaaS).
- Collega alla responsabilità di audit/compliance: il Titolare resta comunque responsabile anche se delega l'infrastruttura.

**2.3** — Come progetteresti l'alta disponibilità di un servizio critico della PA con RTO/RPO molto stretti?
- Definisci RTO e RPO distintamente.
- Architetture multi-AZ/multi-regione, replica sincrona (RPO~0, più costosa/lenta) vs asincrona.
- Load balancing con health check, test di disaster recovery periodici.
- Trade-off: RTO/RPO vicini a zero costano molto di più — va giustificata la scelta in base alla criticità reale del servizio.

---

## 3. Database, data analysis e big data
*(ripasso: [`MIT/studio/03_database_data_analysis_bigdata.md`](../studio/03_database_data_analysis_bigdata.md))*

**3.1** — Quando sceglieresti un database NoSQL invece di uno relazionale per raccogliere dati da migliaia di sensori IoT su ponti e viadotti?
- Volume/velocità di scrittura molto elevati → column-family (es. Cassandra) ottimizzato per time-series.
- Se invece serve integrità referenziale forte (es. anagrafica delle strutture monitorate) → relazionale.
- Menziona il teorema CAP e la possibilità di un'architettura ibrida (polyglot persistence).

**3.2** — Spiega la normalizzazione di un database e quando invece sceglieresti di denormalizzare.
- 1NF/2NF/3NF in breve, con l'obiettivo (ridurre ridondanza e anomalie).
- Denormalizzazione controllata nei data warehouse per velocizzare le letture analitiche.
- Trade-off esplicito: integrità/spazio vs numero di JOIN e performance in lettura.

**3.3** — Cos'è il teorema CAP e come lo applicheresti in un sistema distribuito del MIT che deve restare disponibile anche con problemi di rete tra data center?
- Definisci C, A, P e il vincolo (solo 2 su 3 in presenza di partizione).
- Scelta pratica: un sistema di autorizzazioni/pagamenti vorrà CP (coerenza prima di tutto); un sistema di dashboard/monitoraggio potrà preferire AP (disponibilità, eventual consistency accettabile).

---

## 4. Amministrazione di database e sistemi operativi Unix/Windows Server
*(ripasso: [`MIT/studio/04_amministrazione_db_sistemi_operativi.md`](../studio/04_amministrazione_db_sistemi_operativi.md))*

**4.1** — Descrivi una strategia di backup e disaster recovery per un sistema critico del MIT, considerando anche il rischio ransomware.
- Regola 3-2-1, backup **immutabili** (WORM) come contromisura specifica contro ransomware.
- Test di restore periodici (un backup non testato non è affidabile).
- RTO/RPO coerenti con la criticità del sistema.

**4.2** — Come applicheresti il principio del privilegio minimo nella gestione degli accessi a un sistema Linux con dati sensibili della PA?
- RBAC invece di permessi utente-per-utente.
- `sudo` con audit log invece del login diretto come root.
- Permessi file/directory (rwx) e uso consapevole dei bit speciali (SetUID solo dove necessario).
- Collegamento a NIS2/GDPR per la tracciabilità degli accessi privilegiati.

**4.3** — Un servizio deve ripartire automaticamente a ogni riavvio del server e deve poter essere aggiornato senza downtime prolungato. Che strumenti useresti?
- `systemctl enable` (persistenza al boot) distinto da `start` (avvio immediato one-shot).
- Se containerizzato/orchestrato: rolling update con health check (liveness/readiness probe).
- Eventuale uso di LVM per operazioni di storage senza fermare il servizio.

---

## 5. Progettazione e sviluppo di ambienti cloud
*(ripasso: [`MIT/studio/05_progettazione_ambienti_cloud.md`](../studio/05_progettazione_ambienti_cloud.md))*

**5.1** — Il MIT vuole migrare un'applicazione legacy per le pratiche edilizie verso il cloud. Che percorso di migrazione proporresti?
- Valuta rehost/replatform/rearchitect in base a vincoli di tempo, budget e rischio.
- Possibile strategia incrementale: rehost rapido per ridurre il rischio iniziale, poi evoluzione verso replatform/rearchitect se i benefici lo giustificano.

**5.2** — Vantaggi e svantaggi della containerizzazione rispetto alle macchine virtuali per un'applicazione della PA?
- Leggerezza, densità, portabilità, avvio rapido vs isolamento più debole (kernel condiviso).
- Mitigazioni: immagini minimali, scanning delle vulnerabilità, esecuzione senza privilegi root nel container.

**5.3** — Come garantiresti sicurezza e governance in un cluster Kubernetes che ospita applicazioni di più uffici del MIT?
- Namespace per isolamento logico tra team/progetti.
- Network Policy per limitare il traffico tra Pod/namespace.
- RBAC Kubernetes e IAM con privilegio minimo.
- Secrets management tramite vault dedicato, mai credenziali hardcoded.

---

## 6. Machine learning, IoT, intelligenza artificiale
*(ripasso: [`MIT/studio/06_machine_learning_iot_ia.md`](../studio/06_machine_learning_iot_ia.md))*

**6.1** — Il MIT vuole un modello ML per prevedere il rischio di cedimento strutturale di un ponte da dati di sensori. Come affronteresti il progetto, con quali responsabilità normative?
- Tipo di apprendimento (supervisionato, classificazione/regressione), importanza della qualità/bilanciamento dei dati.
- Validazione tramite cross-validation, attenzione a overfitting e data leakage.
- AI Act: un sistema così è quasi certamente "ad alto rischio" → supervisione umana obbligatoria, tracciabilità delle decisioni, nessuna chiusura automatica senza controllo umano.

**6.2** — Differenza tra edge e cloud computing: quando useresti l'uno o l'altro per un sistema IoT di monitoraggio infrastrutturale?
- Edge: elaborazione vicino al sensore, bassa latenza, resilienza a connettività instabile — utile per allarmi immediati su anomalie.
- Cloud: potenza di calcolo per analisi storiche/addestramento di modelli su grandi volumi aggregati.
- Possibile architettura a livelli (edge → fog → cloud).

**6.3** — Cos'è l'overfitting e come lo eviteresti in un modello predittivo per il MIT?
- Definizione (ottime prestazioni su training, scarse su test) e legame col bias-variance trade-off.
- Tecniche: cross-validation, regolarizzazione (L1/L2, dropout), aumento dei dati, semplificazione del modello.

---

## 7. Cybersecurity, analisi delle vulnerabilità, crittografia
*(ripasso: [`MIT/studio/07_cybersecurity_crittografia.md`](../studio/07_cybersecurity_crittografia.md))*

**7.1** — Come progetteresti la sicurezza di un'API con cui altre PA accedono, tramite PDND, a dati del MIT?
- mTLS (autenticazione server-to-server) + OAuth 2.0 (autorizzazione granulare), coerente col modello ModI.
- Privilegio minimo sugli scope, rate limiting via API Gateway, cifratura in transito, logging/audit.
- Threat modeling preventivo (STRIDE).

**7.2** — Differenza tra Vulnerability Assessment e Penetration Test: quando useresti l'uno o l'altro?
- VA: scansione automatizzata/passiva, individua vulnerabilità note senza sfruttarle.
- PT: sfruttamento attivo per valutare l'impatto reale, più approfondito e mirato, spesso a valle di un'analisi STRIDE/DREAD.
- Uso complementare nel ciclo di sicurezza, non alternativo.

**7.3** — Un attacco ransomware colpisce un sistema del MIT e coinvolge anche dati personali. Quali notifiche scatterebbero, e in che tempi?
- Doppio binario: CSIRT Italia/ACN (NIS2: 24h preliminare, 72h aggiornamento, 1 mese relazione finale) **e** Garante Privacy (GDPR: 72h) — obblighi paralleli, non alternativi.
- Contromisura preventiva: backup immutabili, Zero Trust, MFA.

---

## 8. Business intelligence e data mining
*(ripasso: [`MIT/studio/08_business_intelligence_data_mining.md`](../studio/08_business_intelligence_data_mining.md))*

**8.1** — Come costruiresti un sistema di BI per monitorare l'avanzamento dei progetti PNRR nel settore trasporti?
- Pipeline ETL da sistemi sorgente OLTP verso un data warehouse/data mart.
- Cubi OLAP per analisi multidimensionale (tempo, territorio, tipo di intervento).
- Dashboard con KPI SMART, collegati esplicitamente a milestone/target PNRR (rendicontazione a tranche).

**8.2** — Quale tecnica di data mining useresti per individuare pattern di spesa anomali in una gara d'appalto?
- Anomaly detection (approcci statistici, basati su clustering, o modelli ML supervisionati/non supervisionati).
- Distinzione netta da classification (che richiede classi note a priori) — qui le anomalie non sono note in anticipo.

**8.3** — Un collega osserva una forte correlazione tra due variabili e conclude che una causa l'altra. Come risponderesti?
- Correlazione non implica causalità: possibili variabili confondenti, causalità inversa, coincidenza.
- Servono disegni di analisi adeguati (esperimenti controllati, tecniche di inferenza causale) per affermare un nesso causale.

---

## 9. Tutela dei dati personali
*(ripasso: [`MIT/studio/09_tutela_dati_personali.md`](../studio/09_tutela_dati_personali.md))*

**9.1** — Il MIT vuole un sistema di videosorveglianza con riconoscimento targhe su un tratto autostradale. Quali adempimenti privacy considereresti?
- DPIA obbligatoria (sorveglianza sistematica su larga scala di area accessibile al pubblico).
- Base giuridica: esecuzione di un compito di interesse pubblico.
- Minimizzazione dei dati, Privacy by Design/Default, consultazione del DPO, eventuale consultazione preventiva del Garante se il rischio residuo resta elevato.

**9.2** — Differenza tra Titolare e Responsabile del trattamento: come si traduce in un contratto con un fornitore cloud del MIT?
- Titolare: decide finalità e mezzi (il MIT). Responsabile: tratta per conto del Titolare (il CSP), su atto giuridico ex art. 28 GDPR.
- Nel contratto: istruzioni documentate, obblighi di sicurezza, notifica di data breach al Titolare, divieto di sub-responsabili non autorizzati.

**9.3** — Scopri un data breach che coinvolge dati di dipendenti del MIT un venerdì pomeriggio. Come procederesti?
- Valutazione immediata del rischio per gli interessati.
- Notifica al Garante entro 72h se c'è rischio (il weekend non sospende il termine).
- Comunicazione diretta agli interessati se il rischio è elevato, salvo misure (es. cifratura) che lo escludano.
- Documentazione interna sempre, anche se si decide di non notificare; eventuale doppio binario NIS2 se coinvolto un servizio essenziale.

---

## 10. Normativa nazionale ed europea in materia di amministrazione digitale
*(ripasso: [`MIT/studio/10_normativa_amministrazione_digitale.md`](../studio/10_normativa_amministrazione_digitale.md))*

**10.1** — Un cittadino firma un'istanza al MIT con Firma Elettronica Avanzata (FEA). È sufficiente, o serve la Firma Digitale (FEQ)?
- Dipende dalla natura dell'atto: per istanze informali basta FEA/FES con identificazione SPID/CIE; per atti con effetti giuridici pieni (contratti pubblici, provvedimenti formali) serve la FEQ (art. 25 par. 2 eIDAS, Reg. UE 910/2014 come aggiornato dal Reg. UE 2024/1183).

**10.2** — Quali passaggi prevede il CAD prima che il MIT possa acquistare un software gestionale proprietario?
- Gerarchia artt. 68-69: valutazione comparativa open source → riuso da altra PA → sviluppo ex novo (poi da rilasciare in riuso) → proprietario, solo se motivato.

**10.3** — Spiega il principio "Once Only" e la sua attuazione tecnica nella PA italiana.
- Base giuridica: art. 18 L. 241/1990 (la PA non può chiedere dati già in proprio possesso).
- Attuazione tecnica: PDND come broker di fiducia; esempio settoriale: FVOE nel Codice degli Appalti.

---

## 11. Trasformazione digitale della pubblica amministrazione
*(ripasso: [`MIT/studio/11_trasformazione_digitale_pa.md`](../studio/11_trasformazione_digitale_pa.md))*

**11.1** — Descrivi la governance della trasformazione digitale italiana: chi fa cosa tra DTD, AGID e ACN?
- DTD: indirizzo politico-strategico e fondi (interno alla PCM, nessun bilancio proprio).
- AGID: braccio tecnico-operativo, scrive le Linee Guida attuative.
- ACN: vigilanza sulla sicurezza (NIS2, qualificazione cloud dal 2023), gestisce CSIRT Italia.
- Porta un esempio di progetto che attraversa tutti e tre i livelli.

**11.2** — Il MIT vuole migrare un servizio critico al cloud. Che percorso decisionale seguiresti rispetto alla Strategia Cloud Italia?
- Classificazione del dato/servizio (Ordinario/Critico/Strategico); per Critico/Strategico, obbligo di infrastrutture come il PSN.
- Solo CSP qualificati ACN/AGID possono ospitare workload PA; poi scelta del percorso di migrazione (rehost/replatform/rearchitect).

**11.3** — Come si collega il principio "Cloud First" alla sostenibilità economica (TCO) di un progetto ICT pubblico?
- Cloud First privilegia SaaS>PaaS>IaaS per minimizzare l'onere gestionale interno.
- Il TCO va oltre il prezzo d'acquisto: manutenzione, formazione, rischio di vendor lock-in, consumo energetico (Green IT).

---

## 12. Disciplina nazionale ed europea NIS (Network and Information Security)
*(ripasso: [`MIT/studio/12_nis_network_information_security.md`](../studio/12_nis_network_information_security.md))*

**12.1** — Il MIT rientra nel perimetro NIS2? In quale categoria, e con quali obblighi principali?
- Il settore trasporti/PA centrale rientra tipicamente tra i Soggetti Essenziali (Allegato I) → vigilanza ex ante.
- Obblighi: incident reporting (24h/72h/1 mese al CSIRT Italia), misure tecniche minime (MFA, cifratura, backup immutabili, Zero Trust), supply chain security sui fornitori ICT.

**12.2** — Differenza tra NIS2 e PSNC: un ente può rientrare in entrambi?
- NIS2: perimetro ampio, multisettoriale, per categoria/dimensione.
- PSNC: riservato ai beni ICT di rilevanza strategica nazionale (es. sistemi di comando/controllo di infrastrutture iper-critiche), con il CVCN per la certificazione degli acquisti critici.
- Sì, sono cumulabili: un ente può rientrare in entrambi i perimetri con obblighi che si sommano.

**12.3** — In caso di incidente cyber sul sistema che gestisce il traffico ferroviario, quali notifiche andrebbero fatte e perché è un caso delicato per il MIT?
- Settore trasporti ferroviari = infrastruttura critica (Allegato I NIS2), possibile anche rilevanza PSNC se i sistemi di comando/controllo sono strategici.
- Notifica CSIRT Italia/ACN nei tempi NIS2; se coinvolti dati personali, doppio binario con il Garante.
- Delicatezza specifica: impatto diretto su sicurezza pubblica/incolumità, non solo su continuità del servizio — eleva la priorità e la visibilità istituzionale dell'incidente.
