# Soluzioni — Simulazione Ramo B: Dati, Metadatazione & Intelligenza Artificiale

> Risposte modello alla [simulazione Ramo B](AGID_Simulazione_Ramo_B.md), redatte per coprire tutte le voci della griglia di autocorrezione.

---

## Quesito 1 — Interoperabilità sintattica vs semantica

L'**interoperabilità sintattica** riguarda la capacità di due sistemi di scambiarsi dati usando lo stesso formato e lo stesso canale tecnico (es. entrambi in JSON via HTTPS): i dati "si aprono" correttamente, ma il loro significato non è garantito essere interpretato allo stesso modo dai due sistemi. L'**interoperabilità semantica** va oltre: garantisce che lo stesso dato abbia lo **stesso significato** per il sistema che lo produce e per quello che lo consuma, evitando ambiguità (es. un campo "stato" che in un sistema indica lo stato civile e in un altro lo stato del procedimento).

**OntoPiA** è la rete di ontologie e vocabolari controllati condivisi dalla PA italiana, che fornisce una rappresentazione uniforme dei concetti di dominio (persona, luogo, organizzazione, ecc.), evitando che ogni amministrazione modelli gli stessi concetti in modo diverso. **DCAT-AP_IT** è il profilo italiano dello standard europeo DCAT (Data Catalog Vocabulary), che definisce un set uniforme di metadati per la catalogazione dei dataset (titolo, licenza, formato, ente titolare, ecc.), garantendo che i cataloghi open data delle diverse PA siano interrogabili e confrontabili in modo omogeneo. Insieme, OntoPiA (semantica dei concetti) e DCAT-AP_IT (metadatazione dei dataset) sono gli strumenti con cui si realizza concretamente l'interoperabilità semantica dei dati pubblici.

---

## Quesito 2 — Metadati minimi del documento informatico

Le Linee Guida AgID individuano un set minimo di metadati obbligatori per ogni documento informatico: **identificativo univoco** del documento, **data** di formazione, **oggetto** (il contenuto/argomento del documento) e **autore/soggetto produttore** (chi lo ha formato o inviato).

Questi metadati sono funzionali a due esigenze distinte. Ai fini della **fascicolazione elettronica**, consentono di raggruppare in modo coerente e automatizzabile i documenti appartenenti allo stesso procedimento nel fascicolo informatico (identificativo e oggetto permettono di collegare atti correlati). Ai fini della **conservazione a norma**, garantiscono la tracciabilità e la rintracciabilità del documento nel tempo: in caso di verifica, audit o contenzioso, è possibile ricostruire con certezza chi ha prodotto il documento, quando, e a quale procedimento appartiene — requisito indispensabile per il valore probatorio del documento conservato.

---

## Quesito 3 — Principi AGID per l'IA e classificazione del rischio AI Act

Le Linee Guida AgID sull'adozione dell'IA nella PA richiamano tre principi cardine: la **trasparenza algoritmica** (l'interessato deve poter conoscere l'esistenza e la logica di un processo decisionale automatizzato che lo riguarda), la **non discriminazione** (assenza di bias nei dati di addestramento e nei modelli, che non devono produrre esiti discriminatori verso categorie di persone) e la **supervisione umana** (human-in-the-loop: una decisione con effetti giuridici non può essere interamente demandata a un sistema automatizzato senza un punto di controllo umano effettivo).

Questi principi si collegano direttamente alla **classificazione del rischio** prevista dall'AI Act (Regolamento UE 2024/1689), che distingue quattro livelli: **rischio inaccettabile** (pratiche vietate, es. social scoring); **rischio alto** (es. sistemi usati per decisioni su prestazioni sociali essenziali o accesso a servizi pubblici, tipicamente il caso di molti sistemi IA nella PA), soggetti a obblighi stringenti di valutazione di conformità, documentazione tecnica e supervisione umana rafforzata; **rischio limitato**, con obblighi di trasparenza minima (es. informare l'utente che sta interagendo con un chatbot); **rischio minimo**, senza obblighi specifici. Più il sistema si colloca in alto nella scala di rischio, più i tre principi AGID si traducono in obblighi normativi concreti e verificabili (es. valutazione d'impatto, audit del modello, log delle decisioni).

---

## Caso gestionale

*Metodo (4 mosse): (1) inquadramento normativo, (2) metodo progettuale, (3) soluzione tecnica, (4) rischio & budget.*

**Contesto.** Una Regione vuole realizzare una piattaforma di Open Data che raccolga dataset di più assessorati (alcuni High Value Datasets) e valuta un modulo ML di smistamento automatico delle istanze dei cittadini, con possibile futura estensione a decisioni di prima istanza.

### (a) Catalogazione e modellazione semantica

Tutti i dataset regionali vanno catalogati secondo **DCAT-AP_IT**, con metadatazione uniforme (titolo, licenza, formato, ente titolare, data di aggiornamento) e uso di **OntoPiA** per garantire che concetti condivisi tra assessorati (es. "unità territoriale", "struttura sanitaria") siano rappresentati semanticamente in modo coerente, evitando ambiguità tra i domini sanità/mobilità/ambiente/tributi.

Per i dataset classificati come **High Value Datasets** (individuati a livello UE) si applicano obblighi rafforzati rispetto agli altri: pubblicazione gratuita, in formati machine-readable, con accesso reso disponibile anche tramite API — non è sufficiente una pubblicazione statica in portale.

### (b) Requisiti tecnici minimi di pubblicazione

I dataset devono essere pubblicati in **formati aperti e machine-readable** (CSV, JSON, RDF — non PDF scansionato o formati proprietari), con **licenza aperta** esplicitamente dichiarata e, per i dataset ad alto valore, **accesso via API**. Questo garantisce interoperabilità con il portale nazionale **dati.gov.it** e con i cataloghi di altre PA, che tipicamente aggregano (harvesting) i metadati DCAT-AP_IT esposti localmente: un dataset non conforme allo standard di metadatazione semplicemente non verrebbe recepito correttamente dagli harvester esterni.

### (c) Modulo di smistamento e AI Act

Il caso attuale — smistamento automatico delle istanze verso l'ufficio competente — non incide su diritti o obblighi del cittadino in modo determinante: si tratta di un'attività di instradamento, classificabile come **rischio limitato/moderato**, per cui sono sufficienti misure di trasparenza minima (es. informare che lo smistamento è automatizzato) e un monitoraggio ordinario delle prestazioni del modello.

L'eventuale **estensione futura** a decisioni di prima istanza su pratiche a basso valore economico cambia radicalmente la classificazione: si tratterebbe di un sistema che incide su un diritto/accesso a una prestazione, riconducibile a **rischio alto** ai sensi dell'AI Act. In tal caso occorrerebbe: una valutazione di conformità prima della messa in produzione, documentazione tecnica del modello, **non esclusività della decisione algoritmica** (il cittadino deve poter ottenere revisione umana) e un punto di **supervisione umana** esplicito e non meramente formale prima che la decisione produca effetti.

### (d) Rischi e mitigazioni

- **Qualità/bias dei dati di addestramento**: rischio che il modello di smistamento (e, a maggior ragione, un futuro modello decisionale) rifletta squilibri storici nei dati → mitigazione con validazione periodica del dataset di training e monitoraggio degli esiti per sottogruppi;
- **Governance multi-assessorato**: dataset di proprietà di assessorati diversi, con responsabilità e cicli di aggiornamento non allineati → serve un modello di data ownership chiaro (data steward per assessorato) e un processo di aggiornamento concordato;
- **Dati sanitari**: il dataset sanità richiede particolare attenzione — anonimizzazione o pseudonimizzazione prima della pubblicazione open data, e una valutazione d'impatto sulla protezione dei dati (DPIA) ai sensi del GDPR prima di qualunque trattamento aggiuntivo;
- **Sostenibilità/budget**: la piattaforma richiede un costo ricorrente di manutenzione (aggiornamento dataset, hosting, evoluzione del modello ML) da programmare fin dall'inizio in ottica di TCO, non solo come costo di sviluppo iniziale.

**Criticità residue.** L'estensione futura a decisioni automatizzate andrebbe pianificata solo dopo aver validato il modello di smistamento sul campo e aver messo in piedi la governance dei dati necessaria a sostenere un sistema ad alto rischio.
