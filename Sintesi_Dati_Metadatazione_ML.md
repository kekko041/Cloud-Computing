# Sintesi: Modellazione Dati, Metadatazione e Machine Learning

Sintesi mirata alla **Materia 3** del bando AGID-01 (art. 7) — corrispondente al **Ramo B** della [mappa mentale del concorso](Mappa_Mentale_AGID.html). Fonti: `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §3, `AGID/pdf/12-15` e `18`, Piano Triennale 2024-2026 Cap. 5 (`AGID/pdf/01`).

---

## 1. Modellazione Semantica dei Dati

La *data-driven administration* richiede che i dati pubblici non siano solo digitali, ma **semanticamente interoperabili** tra amministrazioni diverse.

*   **OntoPiA**: la rete di ontologie e vocabolari controllati della PA italiana. Fornisce classi e proprietà condivise (es. Persona, Organizzazione, Luogo) affinché sistemi diversi rappresentino gli stessi concetti nello stesso modo, evitando ambiguità semantica nell'interscambio dati. Richiamata anche dalle Linee Guida sull'interoperabilità tecnica (materia 2).
*   **DCAT-AP_IT**: profilo italiano dello standard europeo DCAT (Data Catalog Vocabulary), usato per **catalogare** i dataset pubblici (metadati su titolo, licenza, formato, ente titolare) in modo uniforme, abilitando la ricercabilità cross-portale (es. dati.gov.it e i cataloghi regionali).

> **Perché rilevante**: senza un modello semantico condiviso, l'interoperabilità "sintattica" (stesso formato file) non basta — serve un'interoperabilità "semantica" (stesso significato dei campi). È il ponte concettuale tra questa materia e la materia 2 (modelli di interoperabilità).

---

## 2. Metadatazione

La metadatazione è l'insieme minimo di informazioni descrittive che rende un dato/documento **tracciabile, fascicolabile e riutilizzabile**.

*   **Documento informatico** (Linee Guida sul documento informatico, `AGID/pdf/18`): ogni documento informatico deve avere un set minimo di metadati obbligatori — **identificativo univoco, data, oggetto, autore/soggetto produttore** — per garantirne la rintracciabilità nel fascicolo informatico e la corretta conservazione a norma. Collega direttamente al CAD (materia 12) e al concetto di *fascicolazione elettronica*.
*   **Repertorio Nazionale dei Dati Territoriali (RNDT)**: catalogo nazionale specifico per i dati territoriali/geografici della PA, con proprie regole di metadatazione (conformi a standard INSPIRE), alimentato dalle amministrazioni titolari.

> **Trade-off da Solutions Architect**: metadati troppo scarni compromettono ricercabilità e conformità (es. mancata tracciabilità in caso di audit); metadati eccessivi aumentano l'onere di data entry e il rischio di incoerenza tra sistemi. La soluzione architetturale tipica è l'estrazione automatica dei metadati minimi a livello di pipeline di ingestion, non di inserimento manuale.

---

## 3. Open Data

*   **Linee Guida su regole tecniche per l'apertura dei dati e riutilizzo PSI** (`AGID/pdf/12`): i dati pubblici non soggetti a restrizioni di privacy/sicurezza devono essere pubblicati in **formati aperti e machine-readable** (CSV, JSON, RDF — non PDF scansionato), con licenza aperta esplicita, per consentirne il riutilizzo da parte di terzi (cittadini, imprese, altre PA). Attua l'Art. 9 del CAD (Open Data, vedi `Sintesi_CAD_e_Appalti_ICT.md`).
*   **High Value Datasets / Dataset di elevato valore** (`AGID/pdf/13`): categoria di dataset a impatto socio-economico particolarmente rilevante (es. dati geospaziali, osservazione della terra, meteorologici, statistici, societari, mobilità), individuata a livello UE (Regolamento di esecuzione 2023/138 sugli Open Data), per cui vigono **obblighi rafforzati di pubblicazione gratuita, machine-readable e via API**.

> **Collegamento con l'interoperabilità**: gli Open Data pubblicati senza metadatazione DCAT-AP_IT e senza modello semantico OntoPiA restano "aperti" ma difficilmente interoperabili — i tre concetti (§1-2-3) vanno letti come un'unica catena: modellare → descrivere → pubblicare.

---

## 4. Intelligenza Artificiale e Machine Learning nella PA

*   **Piano Triennale 2024-2026, Cap. 5 — "Dati e Intelligenza Artificiale"**: inquadra l'IA come componente tecnologica trasversale del Piano, non come ambito isolato.
*   **Strategia Italiana per l'Intelligenza Artificiale 2024-2026**: quattro macro-aree — **Ricerca, PA, Impresa, Formazione** — con l'obiettivo di un'adozione dell'IA responsabile e sovrana (infrastrutture e competenze nazionali).
*   **Bozza Linee Guida per l'adozione dell'IA nella PA** (`AGID/pdf/14`, delibera 17/2025, in consultazione pubblica): regole per le PA che *utilizzano* sistemi di IA (non necessariamente sviluppati internamente) — governance, valutazione del rischio, supervisione umana.
*   **Bozza Linee Guida per lo sviluppo di sistemi di IA nella PA** (`AGID/pdf/15`, 2026): copre il ciclo di vita di sviluppo di sistemi di IA *in house o affidati a fornitori*, incluso il procurement IA — collegandosi alla materia 9 (gare pubbliche ICT).
*   **Cornice normativa**:
    *   **AI Act (Reg. UE 2024/1689)**: classificazione dei sistemi IA per livello di rischio (inaccettabile/alto/limitato/minimo); per la PA rilevano soprattutto i sistemi ad **alto rischio** (es. accesso a servizi pubblici essenziali), che richiedono valutazione di conformità, trasparenza algoritmica e **supervisione umana** (*human-in-the-loop*).
    *   **Legge 132/2023**: approccio nazionale *human-centered* all'IA, principio di non esclusività della decisione algoritmica (già richiamato anche dal Codice Appalti, art. 30, per l'uso di IA nelle gare — vedi `Sintesi_CAD_e_Appalti_ICT.md` §Digitalizzazione).

> **I tre pilastri ricorrenti nelle Linee Guida IA della PA** (utili per rispondere a un quesito sintetico):
> 1. **Trasparenza algoritmica** — l'amministrato deve poter comprendere la logica della decisione automatizzata.
> 2. **Non discriminazione / assenza di bias** — verifica dei dataset di addestramento e degli output.
> 3. **Supervisione umana** — nessuna decisione con effetti giuridici su un individuo può essere interamente automatizzata senza un punto di controllo umano.

---

## Mappa dei collegamenti con le altre materie del bando

| Materia 3 (questo documento) | Collegata a |
|---|---|
| OntoPiA, DCAT-AP_IT | Materia 2 — Modelli di interoperabilità |
| Metadatazione documento informatico | Materia 12 — CAD (fascicolazione elettronica) |
| Procurement di sistemi IA | Materia 9 — Gare pubbliche ICT (non esclusività della decisione algoritmica, art. 30 Codice Appalti) |
| Governance dati e IA nel Piano Triennale | Materia 7 — Interventi di programmazione e innovazione ICT |
