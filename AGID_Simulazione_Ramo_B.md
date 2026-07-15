# Simulazione — Ramo B: Dati, Metadatazione & Intelligenza Artificiale
### Concorso AGID-01 · Materia 3 del bando (art. 7)

> **Formato.** Come da bando, la prova reale è composta da uno o più quesiti a risposta sintetica e uno o più casi gestionali, in 4 ore complessive su tutte le materie. Questa è una simulazione **parziale**, mirata al solo Ramo B — usala come allenamento a tempo, non come prova completa.
>
> **Timing consigliato:** 15' a quesito sintetico (30' totali) + 90' per il caso gestionale + 15-20' di autocorrezione con la griglia in fondo. ≈ 2h15 totali.
>
> **Metodo per il caso gestionale:** usa le "4 mosse" — (1) inquadramento normativo, (2) metodo progettuale, (3) soluzione tecnica, (4) rischio & budget — così come impostato nella [mappa mentale del concorso](Mappa_Mentale_AGID.html).
>
> **Fonti di riferimento:** [Sintesi_Dati_Metadatazione_ML.md](Sintesi_Dati_Metadatazione_ML.md), `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §3, `AGID/pdf/12-15` e `18`.

---

## Quesiti a risposta sintetica

### Quesito 1
> Il candidato illustri la differenza tra interoperabilità sintattica e interoperabilità semantica dei dati pubblici, indicando il ruolo di OntoPiA e dello standard DCAT-AP_IT nel garantire quest'ultima.

### Quesito 2
> Il candidato descriva il set minimo di metadati obbligatori per il documento informatico previsto dalle Linee Guida AgID, motivandone la funzione ai fini della fascicolazione elettronica e della conservazione a norma.

### Quesito 3
> Il candidato illustri i tre principi cardine richiamati dalle Linee Guida AgID per l'adozione dell'Intelligenza Artificiale nella PA (trasparenza algoritmica, non discriminazione, supervisione umana), collegandoli alla classificazione del rischio prevista dall'AI Act (Reg. UE 2024/1689).

---

## Caso gestionale

> Una Regione intende realizzare una piattaforma di **Open Data regionale** che raccolga ed esponga i dataset prodotti dai diversi assessorati (sanità, mobilità, ambiente, tributi), alcuni dei quali rientrano tra gli *High Value Datasets* individuati a livello UE. Contestualmente, la Regione valuta l'introduzione di un modulo di **assistenza automatizzata** basato su un modello di Machine Learning per smistare le istanze dei cittadini (es. richieste di contributi) verso l'ufficio competente, con possibilità in futuro di estenderlo a decisioni di prima istanza su pratiche a basso valore economico.
>
> Il candidato, assumendo il ruolo di responsabile dati e IA della Regione:
>
> **(a)** proponga un modello di catalogazione e modellazione semantica dei dataset (standard di metadatazione, uso di OntoPiA/DCAT-AP_IT), distinguendo gli obblighi rafforzati previsti per gli High Value Datasets rispetto agli altri dataset;
>
> **(b)** indichi i requisiti tecnici minimi di pubblicazione (formati aperti, machine-readable, licenza, accesso via API) e le relative implicazioni di interoperabilità con altri portali (dati.gov.it, portali di altre PA);
>
> **(c)** analizzi, per il modulo di smistamento automatizzato, il livello di rischio ai sensi dell'AI Act e le misure di trasparenza algoritmica e supervisione umana da adottare, distinguendo il caso attuale (smistamento) dall'eventuale estensione futura (decisione automatizzata su pratiche);
>
> **(d)** individui i rischi principali dell'iniziativa (qualità/bias dei dati di addestramento, governance dei dataset tra assessorati, sicurezza e privacy dei dati sanitari coinvolti) e proponga le relative misure di mitigazione, anche in ottica di budget e sostenibilità del progetto nel tempo.
>
> Si motivino le scelte e si segnalino eventuali criticità residue.

---

## Griglia di autocorrezione

Usala per punteggiare (0/1/2) ciascuna voce dopo aver scritto la tua risposta.

**Quesito 1**
- [ ] Distingue interoperabilità sintattica (stesso formato/canale tecnico) da semantica (stesso significato dei dati)
- [ ] Descrive OntoPiA come rete di ontologie/vocabolari condivisi per la rappresentazione uniforme dei concetti
- [ ] Descrive DCAT-AP_IT come profilo italiano dello standard DCAT per la catalogazione uniforme dei dataset (metadati su titolo, licenza, formato, ente titolare)

**Quesito 2**
- [ ] Cita correttamente il set minimo: identificativo univoco, data, oggetto, autore/soggetto produttore
- [ ] Collega i metadati alla fascicolazione elettronica (raggruppamento coerente dei documenti nel fascicolo informatico)
- [ ] Collega i metadati alla conservazione a norma e alla tracciabilità/rintracciabilità in caso di verifica o audit

**Quesito 3**
- [ ] Illustra i tre principi: trasparenza algoritmica, non discriminazione/assenza di bias, supervisione umana (human-in-the-loop)
- [ ] Richiama correttamente la classificazione del rischio dell'AI Act (inaccettabile/alto/limitato/minimo)
- [ ] Collega il livello di rischio alle misure richieste (es. sistemi ad alto rischio → valutazione di conformità e supervisione umana rafforzata)

**Caso gestionale**

| Punto | Cosa deve comparire nella risposta | ✓ |
|---|---|---|
| (a) Modellazione | Metadatazione DCAT-AP_IT, uso di OntoPiA per la semantica condivisa tra assessorati; obblighi rafforzati per High Value Datasets (pubblicazione gratuita, machine-readable, via API) | ☐ |
| (b) Pubblicazione | Formati aperti (CSV/JSON/RDF, non PDF scansionato), licenza aperta esplicita, accesso via API, interoperabilità con dati.gov.it e altri cataloghi regionali | ☐ |
| (c) IA e rischio | Smistamento = rischio limitato/moderato con trasparenza minima; eventuale decisione automatizzata su pratiche = rischio alto → valutazione di conformità AI Act, non esclusività della decisione algoritmica, punto di controllo umano esplicito | ☐ |
| (d) Rischi | Qualità/bias dei dati di training; governance multi-assessorato (data ownership, aggiornamento); dati sanitari → necessità di anonimizzazione/pseudonimizzazione e valutazione d'impatto privacy (GDPR); sostenibilità/budget della piattaforma nel tempo | ☐ |
| Metodo | La risposta segue le 4 mosse (norma → metodo → soluzione tecnica → rischio/budget) invece di elencare i fatti senza struttura | ☐ |

---

> **Come proseguire.** Scrivi la tua risposta al caso gestionale (anche solo per punti) e incollala in chat: te la correggo voce per voce sulla griglia sopra, segnalando cosa manca e cosa è già solido.
