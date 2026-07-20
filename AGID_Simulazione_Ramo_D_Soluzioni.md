# Soluzioni — Simulazione Ramo D: Governo IT — Programmazione, Progetti & Budget

> Risposte modello alla [simulazione Ramo D](AGID_Simulazione_Ramo_D.md), redatte per coprire tutte le voci della griglia di autocorrezione.

---

## Quesito 1 — PRINCE2/PMBOK vs Agile e ruolo dell'RTD

La scelta tra un approccio strutturato (PRINCE2/PMBOK) e un approccio Agile dipende principalmente dalla **stabilità dei requisiti** e dal **formalismo richiesto** dal contesto del progetto. Quando i requisiti sono stabili, ben definiti fin dall'inizio e il progetto richiede un forte controllo documentale/di governance (es. grandi opere infrastrutturali IT con vincoli contrattuali rigidi), un approccio strutturato come PRINCE2 o PMBOK è più adeguato, perché fornisce un impianto di pianificazione, controllo dei costi e reportistica formale. Quando invece i requisiti sono in evoluzione, il valore va rilasciato in modo incrementale e il feedback dell'utente finale è centrale (tipico di molti progetti di digitalizzazione di servizi pubblici), l'approccio **Agile** è preferibile, perché permette di adattare il prodotto durante il percorso tramite iterazioni brevi (sprint) e rilasci frequenti.

Il **Responsabile della Transizione Digitale (RTD)**, figura prevista dal CAD in ogni amministrazione, ha tra i propri compiti anche il **rafforzamento delle competenze di project management** all'interno dell'ente, promuovendo l'adozione di metodologie adeguate e collegando le pratiche di PM al monitoraggio dell'esecuzione contrattuale (contract monitoring) con i fornitori, in modo che le best practice di project management non restino confinate al singolo progetto ma diventino patrimonio organizzativo dell'ente.

---

## Quesito 2 — I 10 principi guida del Piano Triennale 2024-2026

Il Piano Triennale per l'Informatica nella PA individua dieci principi guida: **Digital & mobile first**, **Cloud first**, **API-first**, **Once Only**, **Data driven**, **Agile**, **servizi progettati sull'utente**, **security & privacy by design**, **riuso**, **codice aperto**.

Tre esempi applicativi:
- **Cloud first**: un'amministrazione che deve realizzare un nuovo servizio digitale valuta prioritariamente soluzioni cloud (PSN per servizi Critici/Strategici, cloud pubblico qualificato per gli altri) prima di considerare infrastrutture on-premise dedicate.
- **Once Only**: un Comune che deve erogare un contributo economico recupera i dati reddituali già in possesso di un'altra PA (es. tramite PDND) invece di richiederli nuovamente al cittadino.
- **Servizi progettati sull'utente**: la progettazione dell'interfaccia di un procedimento online parte da test di usabilità con utenti reali, non dalla mera trasposizione digitale del modulo cartaceo preesistente.

Questi principi costituiscono la cornice programmatoria del Piano Triennale 2024-2026, a cui ogni progetto ICT della PA dovrebbe potersi ricondurre esplicitamente in fase di programmazione.

---

## Quesito 3 — TCO e parere di congruità tecnico-economica (art. 14-bis CAD)

Il **TCO (Total Cost of Ownership)** applicato alla spesa ICT pubblica impone di valutare non il solo prezzo d'acquisto iniziale, ma il **costo totale** lungo l'intero ciclo di vita della soluzione: manutenzione, formazione del personale, eventuale lock-in verso il fornitore, costi energetici/di esercizio (energy saving). Una soluzione apparentemente più economica in fase di acquisto può risultare più costosa nel tempo se genera costi ricorrenti elevati o dipendenza esclusiva da un fornitore.

Il **parere di congruità tecnico-economica** (art. 14-bis CAD) è lo strumento con cui AGID valuta se un progetto/acquisto ICT della PA sia coerente sotto il profilo tecnico ed economico. È **non vincolante** per i contratti generici sopra soglia (indicativamente 1-2 milioni di euro), dove svolge una funzione di indirizzo/segnalazione di eventuali criticità senza bloccare l'amministrazione; diventa invece **vincolante** quando l'acquisto riguarda beni/servizi strategici tramite **Consip o altri soggetti aggregatori**, dove il parere condiziona effettivamente la possibilità di procedere.

---

## Caso gestionale

*Metodo (4 mosse): (1) inquadramento normativo, (2) metodo progettuale, (3) soluzione tecnica, (4) rischio & budget.*

**Contesto.** Un'amministrazione centrale ha un finanziamento PNRR di 3,5 M€ per digitalizzare un procedimento cartaceo, con milestone di rendicontazione **semestrali** e nessuna esperienza pregressa in Agile.

### (a) Approccio metodologico e KPI

Dato il vincolo delle milestone semestrali PNRR e la scadenza rigida di rendicontazione, un approccio Agile "puro" senza alcuna struttura di controllo sarebbe rischioso; un approccio **ibrido** è la scelta più coerente: **Scrum** per la gestione dello sviluppo (sprint brevi, backlog prioritizzato, revisione continua), incorniciato in un impianto di governance più strutturato per allineare gli **sprint** alle scadenze di rendicontazione semestrale (ogni semestre corrisponde a un incremento di più sprint, con una milestone di rendicontazione a fine periodo che richiede un deliverable dimostrabile).

KPI minimi da monitorare: **avanzamento percentuale rispetto alla milestone** (burn-down/burn-up a livello di programma, non solo di singolo sprint), **tasso di completamento delle attività formative** previste per il personale, **tempi di collaudo** dell'applicativo rispetto al piano.

### (b) Principi del Piano Triennale applicabili

I principi più rilevanti per questo progetto sono: **Cloud first**, per l'acquisizione dei servizi di hosting (coerente con quanto già previsto dal progetto); **Once Only**, se il procedimento oggi cartaceo recupera dati già in possesso di altre PA (da verificare in fase di analisi, con eventuale integrazione via PDND); **servizi progettati sull'utente**, per l'interfaccia del procedimento, che deve sostituire in modo realmente usabile — non solo trasporre — il modulo cartaceo; **security & privacy by design**, da applicare fin dalla progettazione dell'applicativo, data la natura di dati personali trattati in un procedimento amministrativo.

### (c) Budget secondo la logica TCO e parere di congruità

Il budget di 3,5 M€ non va allocato solo sullo sviluppo iniziale dell'applicativo: vanno previste esplicitamente le voci **ricorrenti** — canone dei servizi cloud di hosting, manutenzione evolutiva/correttiva dell'applicativo, costi di formazione del personale (non solo iniziale, ma di aggiornamento nel tempo) — secondo la logica TCO vista nel quesito 3.

Sul **parere di congruità tecnico-economica**: se l'acquisizione dei servizi cloud/sviluppo avviene tramite **Consip o un soggetto aggregatore** su un bene classificato come strategico, il parere è **vincolante** e va richiesto prima di procedere; se invece l'amministrazione procede con un affidamento diretto sul mercato non tramite centrale di committenza, il parere resta **non vincolante** (pur restando comunque opportuno richiederlo, dato l'importo rilevante di 3,5 M€, come strumento di validazione tecnica).

### (d) Rischi e mitigazioni

- **Mancato rispetto delle milestone**: mitigato con sprint review frequenti e un monitoraggio di avanzamento a cadenza più stretta del semestre (es. mensile), per intercettare scostamenti in tempo utile a correggere la rotta prima della scadenza di rendicontazione;
- **Sottostima dei costi ricorrenti**: mitigata programmando il budget secondo la logica TCO fin dalla fase di pianificazione, non aggiungendo le voci ricorrenti "a consuntivo";
- **Resistenza al cambiamento metodologico** (prima esperienza Agile dell'amministrazione): mitigata con formazione mirata del team di progetto e un percorso di change management che accompagni gradualmente l'organizzazione, evitando di imporre l'Agile in modo just-in-time sotto la pressione della prima milestone.

**Criticità residue.** La combinazione di un vincolo di rendicontazione rigido (PNRR) con la prima adozione di Agile nell'ente resta un fattore di rischio organizzativo che va gestito con un accompagnamento dedicato, non solo con la scelta metodologica in sé.
