# Sintesi: CAD, Codice degli Appalti, E-Procurement ICT, Performance e Trasparenza

Questo documento fornisce una sintesi mirata dei riferimenti normativi principali per i concorsi pubblici in ambito informatico, focalizzandosi sugli aspetti chiave richiesti dal Profilo A e C di Banca d'Italia e — nelle sezioni 4 e 5 — dalle **Materie 9, 11, 12, 13** del bando AGID-01 (Ramo E della [mappa mentale del concorso](Mappa_Mentale_AGID.html)). La sezione 1 (L. 241/1990) fornisce il fondamento di diritto amministrativo generale su cui si innestano CAD e Codice Appalti.

---

## 1. La Legge sul Procedimento Amministrativo — L. 241/1990

La L. 241/1990 è la norma generale che disciplina il procedimento amministrativo e il diritto di accesso ai documenti. È il fondamento giuridico su cui si innesta la digitalizzazione prevista dal CAD (§2): il CAD non sostituisce la 241/90, ne digitalizza gli istituti (comunicazioni, accesso, conclusione del procedimento).

### Principi generali (Art. 1)
Economicità, efficacia, imparzialità, pubblicità, trasparenza + principi dell'ordinamento UE (proporzionalità, legittimo affidamento).

### Il procedimento e i suoi termini (Artt. 2-6)
*   **Art. 2:** obbligo di concludere il procedimento con **provvedimento espresso** entro un termine certo (30 giorni di default, salvo termini speciali).
*   **Art. 4-6:** **responsabile del procedimento** — unità organizzativa e persona fisica responsabili dell'istruttoria, con obbligo di comunicazione al cittadino.

### Partecipazione procedimentale (Artt. 7-13)
*   **Art. 7-8:** comunicazione di avvio del procedimento ai soggetti interessati.
*   **Art. 10:** diritto di visione degli atti e di presentare memorie/documenti.
*   **Art. 10-bis:** **preavviso di rigetto** nei procedimenti a istanza di parte — contraddittorio prima del diniego.

### Semplificazione amministrativa (Artt. 14-20)
*   **Conferenza di servizi** (art. 14-14-quinquies): coordinamento tra più amministrazioni, oggi in larga parte digitalizzata/asincrona (riforma Madia, D.Lgs. 127/2016).
*   **SCIA** (art. 19) e **silenzio-assenso** (art. 20): liberalizzazione — autocertificazione + controlli successivi al posto del regime autorizzatorio.
*   **Art. 18:** la PA non può chiedere al cittadino dati già in proprio possesso o disponibili presso altra PA — base giuridica del principio **Once Only**, poi attuato tecnicamente da PDND (v. [Sintesi_Normazione_Interoperabilita.md](Sintesi_Normazione_Interoperabilita.md)) e dal FVOE (§3).

### Efficacia e invalidità del provvedimento (Artt. 21-bis — 21-nonies)
*   **Nullità** (21-septies): mancanza di elementi essenziali, difetto assoluto di attribuzione, violazione/elusione del giudicato.
*   **Annullabilità** (21-octies): violazione di legge, eccesso di potere, incompetenza — **comma 2**: non annullabile per vizi puramente formali se il contenuto non sarebbe stato diverso.
*   **Autotutela:** annullamento d'ufficio (21-nonies) e revoca (21-quinquies) — bilanciamento tra legalità e legittimo affidamento.

### Diritto di accesso ai documenti amministrativi (Artt. 22-28)
Accesso "documentale" classico, riservato a chi ha un interesse diretto, concreto e attuale. Da non confondere con le evoluzioni successive (D.Lgs. 33/2013, §5):
*   **Accesso civico semplice** (art. 5 co. 1): su dati soggetti a obbligo di pubblicazione.
*   **Accesso civico generalizzato / FOIA** (art. 5 co. 2): chiunque, senza motivazione, salvo eccezioni (privacy, sicurezza).

### Diagramma — flusso del procedimento amministrativo

```mermaid
flowchart TD
    A[Avvio del procedimento<br/>art. 7-8] --> B[Individuazione del<br/>responsabile del procedimento<br/>art. 4-6]
    B --> C[Istruttoria:<br/>acquisizione dati e documenti<br/>art. 18 - divieto di richiedere<br/>dati già in possesso della PA]
    C --> D{Esito favorevole<br/>all'istante?}
    D -- No, provvedimento negativo --> E[Preavviso di rigetto<br/>art. 10-bis]
    E --> F[Osservazioni<br/>dell'interessato]
    F --> G[Provvedimento finale<br/>entro il termine, art. 2]
    D -- Sì --> G
    G --> H[Comunicazione ed efficacia<br/>del provvedimento]
    H --> I{Vizio riscontrato<br/>successivamente?}
    I -- Nullità --art. 21-septies--> L[Provvedimento nullo]
    I -- Illegittimità --art. 21-octies--> M[Annullabile:<br/>autotutela art. 21-nonies]
    I -- Nessun vizio --> N[Provvedimento efficace<br/>e stabile]
```

---

## 2. Il Codice dell'Amministrazione Digitale (CAD) - D.Lgs. 82/2005 e s.m.i.

Il CAD è il corpo normativo che regola il processo di digitalizzazione della Pubblica Amministrazione italiana. Non si limita a definire regole tecniche, ma sancisce veri e propri diritti per cittadini e imprese.

### Principi e Diritti Fondamentali (Artt. 1-11)
*   **Diritto all'uso delle tecnologie (Art. 3):** Chiunque ha il diritto di usare le soluzioni e gli strumenti digitali per comunicare con la PA.
*   **Cittadinanza Digitale:** SPID (Sistema Pubblico di Identità Digitale), CIE (Carta d'Identità Elettronica) e CNS (Carta Nazionale dei Servizi) sono gli unici strumenti di identificazione previsti.
*   **Domicilio Digitale (Art. 3-bis):** Indirizzo elettronico eletto presso un servizio di PEC (Posta Elettronica Certificata) o un servizio elettronico di recapito certificato qualificato, valido per le comunicazioni ufficiali con la PA.
*   **Open Data (Art. 9):** I dati pubblici devono essere formati e resi disponibili in formato aperto (leggibile da dispositivi automatici, gratuito).

### Il Documento Informatico e le Firme (Artt. 20-23)
*   **Documento informatico:** Rappresentazione informatica di atti, fatti o dati giuridicamente rilevanti. 
*   **Firme Elettroniche (in conformità al Regolamento eIDAS):**
    *   *Firma Elettronica Semplice (FES):* Dati in forma elettronica allegati o connessi tramite associazione logica ad altri dati elettronici (es. pin, username/password). Valore probatorio valutabile dal giudice.
    *   *Firma Elettronica Avanzata (FEA):* Connessa unicamente al firmatario, ne consente l'identificazione, creata con mezzi sotto il controllo esclusivo del firmatario (es. firma grafometrica su tablet).
    *   *Firma Elettronica Qualificata (FEQ) / Firma Digitale:* Un particolare tipo di FEA basata su un sistema di chiavi crittografiche asimmetriche (pubblica/privata) e un certificato qualificato rilasciato da un prestatore di servizi fiduciari. Ha l'efficacia della scrittura privata (Art. 2702 c.c.).

### Acquisizione, Riuso e Open Source (Artt. 68-69)
*   **Art. 68 (Valutazione comparativa):** Le PA devono acquisire software tramite valutazione comparativa tecnica ed economica tra: software libero/open source, software a riuso, software proprietario. Il software open source e il riuso hanno priorità.
*   **Art. 69 (Riuso):** Le PA che sono titolari di programmi informatici realizzati su loro specifiche devono renderli disponibili (rilasciando il codice sorgente) in licenza aperta ad altre PA.

---

## 3. Il Codice degli Appalti - D.Lgs. 36/2023 (Focus ICT)

Il nuovo Codice degli Appalti (entrato in vigore nel 2023) introduce principi volti a snellire le procedure di gara, un aspetto cruciale per l'acquisizione di beni e servizi ICT, settori caratterizzati da rapida obsolescenza.

### Principi Guida (Libro I, Artt. 1-3)
*   **Principio del Risultato:** L'affidamento e l'esecuzione del contratto devono avvenire con la massima tempestività e il miglior rapporto qualità/prezzo, nel rispetto della legalità.
*   **Principio della Fiducia:** Si presume la legittimità e la correttezza dell'azione dei funzionari pubblici.
*   **Principio dell'Accesso al mercato:** Favorire la concorrenza, la partecipazione delle PMI e l'innovazione.

### Digitalizzazione del Ciclo di Vita dei Contratti Pubblici (Artt. 19-36)
Questa è la vera novità del Codice 36/2023 per l'ICT:
*   Tutto il ciclo (programmazione, progettazione, gara, esecuzione) deve essere nativamente digitale.
*   **Fascicolo Virtuale dell'Operatore Economico (FVOE):** Gestito dall'ANAC, permette alle PA di verificare i requisiti delle aziende partecipanti in tempo reale, senza chiedere loro di caricare documenti già in possesso dello Stato (principio del *Once Only*).
*   **Banca Dati Nazionale dei Contratti Pubblici (BDNCP):** L'ecosistema centrale per l'interoperabilità dei dati sugli appalti.
*   **Uso di Intelligenza Artificiale e algoritmi:** Ammesso per l'analisi dei dati di gara, ma sempre soggetto al principio di trasparenza, non esclusività della decisione algoritmica (deve esserci un operatore umano) e non discriminazione.

### Strumenti di acquisto ICT (Consip e MePA)
*   Per l'ICT, le PA sono obbligate (salvo rare eccezioni motivate) ad approvvigionarsi tramite gli strumenti messi a disposizione da **Consip** (Convenzioni, Accordi Quadro) o tramite il **MePA** (Mercato Elettronico della PA) per acquisti sotto la soglia comunitaria.

### Tipi di Procedure (Sopra e Sotto Soglia)
*   **Affidamento diretto:** Previsto per importi inferiori a 140.000€ per forniture e servizi (incluso l'ICT). Molto usato per acquisti agili di licenze o sviluppo software di piccola entità.
*   **Procedura Negoziata senza bando:** Usata consultando un numero minimo di operatori per importi tra i 140.000€ e le soglie di rilevanza europea (aggiornate periodicamente, es. dal 2024 sono 143.000€ per le amministrazioni centrali e 221.000€ per quelle sub-centrali).
*   **Procedure Aperte o Ristrette:** Obbligatorie per i grandi appalti ICT (es. sviluppo grandi piattaforme o datacenter) al di sopra delle soglie europee.

#### Focus: l'Affidamento Diretto
La stazione appaltante individua direttamente l'operatore economico senza gara formale, nel limite dei 140.000€. È la procedura più snella e coerente con il *Principio del Risultato* (tempestività), ma resta soggetta a garanzie procedurali:
*   **Rotazione degli affidatari:** va evitata la concentrazione sistematica degli affidamenti sullo stesso fornitore, a tutela della concorrenza (Principio dell'Accesso al mercato).
*   **Motivazione e congruità del prezzo:** anche senza gara, la scelta va documentata (tipicamente tramite indagine di mercato informale o confronto preventivi).
*   **Tracciabilità digitale:** rientra comunque nel ciclo di vita nativamente digitale del contratto (artt. 19-36) e transita per BDNCP e, se applicabile, per il FVOE gestito da ANAC.
*   **Obbligo Consip/MePA:** per l'ICT va comunque veicolato tramite gli strumenti di e-procurement (Convenzioni, Accordi Quadro, MePA), salvo eccezioni motivate — non è un affidamento libero sul mercato aperto.

### Il Subappalto (ICT e Sicurezza)
Il nuovo codice liberalizza il subappalto, rimuovendo i limiti percentuali rigidi (es. il vecchio limite del 30%), a patto che non vi sia intermediazione fittizia. Nel settore ICT, la PA deve valutare molto attentamente l'autorizzazione al subappalto, specialmente se comporta il trattamento di dati sensibili o l'accesso a sistemi critici, per mantenere la conformità al GDPR e alle normative sulla cybersicurezza (es. DORA o Perimetro di Sicurezza Nazionale Cibernetica).

---

## 4. Disciplina Normativa delle Gare Pubbliche di ICT — E-Procurement (Materia 9)

Questa materia riguarda l'attuazione **tecnica** del Codice Appalti (§3) alle gare ICT, tramite gli strumenti digitali di e-procurement definiti da AGID.

*   **Regole Tecniche delle Piattaforme di Approvvigionamento Digitale (PAD) v2** (`AGID/pdf/21`): standard tecnico che disciplina le piattaforme telematiche su cui si svolgono le gare pubbliche digitali (modelli di interoperabilità, checklist di conformità, quadro normativo-tecnico di riferimento).
*   **DGUE (Documento di Gara Unico Europeo)**: autodichiarazione standardizzata a livello UE con cui l'operatore economico attesta il possesso dei requisiti di partecipazione, integrata nel ciclo digitale della gara insieme al FVOE (§3).
*   **Circolare AGID n. 3/2016**: regole tecniche storiche di interoperabilità per l'e-procurement, tuttora richiamate come base del sistema.
*   **AGID come PEPPOL Authority nazionale**: AGID coordina l'adesione italiana alla rete PEPPOL per la fatturazione elettronica e lo scambio di documenti di gara in formato standardizzato a livello europeo (collegamento con la materia 1 — Direttiva 2014/55/UE).
*   **Ordine di preferenza nell'acquisizione software (artt. 68-69 CAD)** (`AGID/pdf/07`): anche nella fase di gara ICT, la PA deve seguire la gerarchia — **open source → riuso → sviluppo ex novo → software proprietario** — motivando l'eventuale scelta di un'opzione meno prioritaria (vedi §1, Acquisizione, Riuso e Open Source).
*   **Acquisti IT via Consip/MePA**: canale obbligatorio (salvo eccezioni motivate) anche per gli affidamenti diretti sotto soglia (§3, Focus Affidamento Diretto).

> **Perché è una materia distinta dal Codice Appalti generale (§3/§5 sotto)**: la materia 9 verifica la conoscenza degli **strumenti e delle piattaforme digitali specifiche per l'ICT** (PAD, DGUE, PEPPOL), non solo delle procedure di affidamento in astratto — è il punto di raccordo tra normativa sugli appalti e competenza tecnica AGID.

---

## 5. Performance e Trasparenza Amministrativa (Materia 11)

*   **Amministrazione Trasparente (D.Lgs. 33/2013)**: impone alle PA l'obbligo di pubblicazione proattiva di una serie di dati, tra cui — per quanto riguarda gli affidamenti ICT — struttura proponente, oggetto del bando, importo, aggiudicatario, tempi di completamento e importi liquidati. Il mancato rispetto di questi obblighi è sanzionabile e vigilato da ANAC (vedi risposta precedente su ANAC).
*   **Ciclo della Performance (D.Lgs. 150/2009)**: disciplina il sistema di misurazione e valutazione della performance organizzativa e individuale nella PA, articolato in fasi: (1) definizione degli obiettivi (Piano della Performance), (2) misurazione e monitoraggio in corso d'anno, (3) valutazione finale, (4) rendicontazione (Relazione sulla Performance). Per un progetto ICT, questo si traduce nella definizione di **KPI di progetto/servizio** coerenti con gli obiettivi strategici dell'amministrazione (collegamento con la materia 6 — KPI di project management, specialmente per la rendicontazione PNRR).
*   **Amministrazione Trasparente di AGID** (`trasparenza.agid.gov.it`): la sezione dedicata sul sito istituzionale AGID è citata come **modello applicativo di riferimento** degli obblighi di trasparenza — utile da menzionare in un caso gestionale come esempio di buona pratica concreta.
*   **Collegamento con l'e-procurement digitale (§3)**: la trasparenza sull'esito di una gara ICT riusa i dati già strutturati nelle piattaforme di approvvigionamento digitale (PAD) e nel FVOE, secondo la logica "pubblica una volta, riusa ovunque" coerente con il principio Once Only.

> **Attenzione**: D.Lgs. 33/2013 e D.Lgs. 150/2009 sono normativa primaria **generale**, non emanata da AGID — AGID ne è un soggetto attuatore (come ogni PA) e fornisce un buon caso di studio applicativo, ma per il testo normativo pieno va integrata la consultazione con `fonti/`.
