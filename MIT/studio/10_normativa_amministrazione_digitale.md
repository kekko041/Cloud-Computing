# Materia 10 — Normativa nazionale ed europea in materia di amministrazione digitale
*Concorso MIT — Codice EPI (Specialista Informatico). Fonti: [`AGID_Sintesi_Preparazione_Concorso.md`](../../AGID_Sintesi_Preparazione_Concorso.md), [`Sintesi_CAD_e_Appalti_ICT.md`](../../Sintesi_CAD_e_Appalti_ICT.md) §2, [`Sintesi_Firma_Digitale.md`](../../Sintesi_Firma_Digitale.md), [`Sintesi_Normazione_Interoperabilita.md`](../../Sintesi_Normazione_Interoperabilita.md), `AGID/pdf/18_LG_Documento_Informatico.pdf`, `AGID/pdf/21_Regole_Tecniche_PAD_v2.pdf`, `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §12*

---

## 1. Il Codice dell'Amministrazione Digitale (CAD) — D.Lgs. 82/2005

Il CAD è la norma cardine che regola la digitalizzazione della PA italiana: non è un insieme di regole tecniche facoltative, ma sancisce **diritti soggettivi** per cittadini e imprese nei confronti della PA.

* **Art. 3 — Diritto all'uso delle tecnologie:** chiunque ha diritto di comunicare con la PA utilizzando le tecnologie dell'informazione. È un diritto azionabile, non una mera facoltà organizzativa della PA.
* **Art. 3-bis — Domicilio digitale:** indirizzo elettronico (PEC o servizio elettronico di recapito certificato qualificato) eletto dal cittadino/impresa come recapito ufficiale per le comunicazioni con la PA, con lo stesso valore legale della notifica cartacea.
* **Art. 9 — Open Data by default:** i dati pubblici (salvo eccezioni privacy/sicurezza) devono essere pubblicati in formato aperto e leggibile da dispositivi automatici.
* **Cittadinanza digitale:** **SPID**, **CIE** (Carta d'Identità Elettronica) e **CNS** (Carta Nazionale dei Servizi) sono gli **unici** strumenti di identificazione digitale previsti dal CAD per l'accesso ai servizi online della PA.
* **Artt. 68-69 — Acquisizione e riuso del software:** prima di acquistare software proprietario, la PA deve svolgere una valutazione comparativa con ordine di preferenza:
  1. Software libero/open source
  2. Software già disponibile in riuso presso altre PA
  3. Sviluppo ex novo (da rilasciare poi in riuso con licenza aperta, art. 69)
  4. Software proprietario, solo se motivato

*Sintesi per l'esame*: se un quesito chiede "prima di acquistare una licenza software, cosa deve fare la PA?", la risposta corretta cita sempre la gerarchia degli artt. 68-69, non un generico confronto di prezzo.

---

## 2. Documento informatico e firme elettroniche

Il documento informatico (rappresentazione informatica di atti, fatti o dati giuridicamente rilevanti — artt. 20-23 CAD) è **equiparato al documento cartaceo** se formato e conservato secondo le regole tecniche AGID (Linee Guida sulla formazione, gestione e conservazione dei documenti informatici, `AGID/pdf/18`).

### 2.1 I tre livelli di firma elettronica (eIDAS — Reg. UE 910/2014 + CAD)

| Tipo | Definizione | Requisiti | Valore probatorio |
|---|---|---|---|
| **FES** — Firma Elettronica Semplice | Dati elettronici allegati/connessi ad altri dati usati come metodo di identificazione (PIN, username/password, firma scansionata) | Nessun requisito di identificazione forte | Liberamente valutabile dal giudice |
| **FEA** — Firma Elettronica Avanzata | Connessa unicamente al firmatario, creata con mezzi sotto il suo controllo esclusivo, rileva modifiche successive (es. firma grafometrica) | Identificazione univoca + integrità, ma senza certificato qualificato | Se conforme ai requisiti tecnici AGID, può avere pieno valore probatorio; altrimenti presunzione intermedia |
| **FEQ / Firma Digitale** — Firma Elettronica Qualificata | FEA basata su certificato qualificato + dispositivo sicuro; in Italia la "Firma Digitale" ne è la declinazione tecnica su crittografia asimmetrica | Certificato qualificato rilasciato da prestatore di servizi fiduciari accreditato + dispositivo sicuro (smart card, token, HSM remoto) | **Piena efficacia probatoria**, equivalente alla firma autografa (art. 2702 c.c.) |

* **Obbligo di FEQ**: per atti con effetti giuridici pieni — contratti pubblici, provvedimenti amministrativi formali. Per istanze informali basta FEA/FES con identificazione via SPID/CIE.
* **Funzionamento tecnico** (in sintesi): hash del documento → cifratura dell'hash con la chiave privata del firmatario (contenuta in un dispositivo sicuro, attivato da PIN) → il destinatario verifica decifrando con la chiave pubblica del certificato e confrontando gli hash.
* **Limite importante**: la sola firma digitale **non conferisce data certa** — serve una marca temporale o l'invio tramite PEC per l'opponibilità a terzi.
* Approfondimento completo (dispositivi, formati PAdES/CAdES/XAdES/ASiC, procedura di ottenimento, crittografia post-quantum) in [`Sintesi_Firma_Digitale.md`](../../Sintesi_Firma_Digitale.md).

### 2.2 Conservazione digitale a norma

* Ogni documento informatico deve avere un **set minimo di metadati obbligatori** (identificativo univoco, data, oggetto, autore) per garantirne rintracciabilità e fascicolazione elettronica (Linee Guida `AGID/pdf/18`, allegati su metadati e protocollo AOO).
* La conservazione a norma richiede un **sistema di conservazione** conforme alle regole tecniche AGID, con un **Responsabile della conservazione** che garantisce integrità, autenticità, leggibilità e reperibilità del documento nel tempo (differente dal semplice backup: la conservazione ha valore probatorio giuridico).

*Sintesi per l'esame*: distingui sempre **backup** (copia di sicurezza, nessun valore giuridico autonomo) da **conservazione digitale a norma** (processo regolamentato con valore probatorio, tipicamente esternalizzato a un conservatore accreditato AGID).

---

## 3. Identità digitale: SPID, CIE, eIDAS

* **SPID (Sistema Pubblico di Identità Digitale)**: sistema federato di identity provider privati accreditati, con 3 livelli di sicurezza (SPID L1/L2/L3, crescenti per robustezza dell'autenticazione — L2 richiede tipicamente OTP, L3 richiede dispositivo crittografico).
* **CIE (Carta d'Identità Elettronica)**: strumento di identificazione con chip crittografico, gestito dal Ministero dell'Interno, utilizzabile anche come mezzo di autenticazione digitale (CIE-ID).
* **eIDAS (Reg. UE 910/2014)**: regolamento europeo che disciplina identità digitale e servizi fiduciari transfrontalieri, garantendo il **riconoscimento reciproco** delle identità digitali notificate tra Stati membri (uno schema di identità digitale notificato da un Paese UE deve essere accettato dagli altri per l'accesso ai servizi pubblici online).
* **OpenID Connect in SPID**: protocollo tecnico con cui SPID espone l'autenticazione federata ai service provider (linee guida AGID dedicate).

*Sintesi per l'esame*: SPID/CIE sono gli strumenti nazionali di attuazione del CAD; eIDAS è il framework europeo che li rende interoperabili a livello UE (principio "once only" cross-border) e che disciplina anche i servizi fiduciari (firme, sigilli elettronici, marche temporali, recapito certificato).

---

## 4. PEC e domicilio digitale

* **PEC (Posta Elettronica Certificata)**: sistema di posta elettronica che fornisce, tramite ricevute di accettazione e consegna, prova legale dell'invio e della consegna di un messaggio — equivalente a una raccomandata con ricevuta di ritorno.
* **Domicilio digitale (art. 3-bis CAD)**: indirizzo (PEC o servizio elettronico di recapito certificato qualificato) eletto dal cittadino/impresa come proprio recapito ufficiale verso la PA. **INAD** (Indice Nazionale dei Domicili Digitali) è il registro pubblico che raccoglie i domicili digitali di cittadini, professionisti e imprese (Linee Guida AGID dedicate, `AGID/Pubblicazioni_e_Linee_Guida_AGID.md` §12).
* **IPA (Indice delle Pubbliche Amministrazioni)**: analogo registro che raccoglie i domicili digitali (PEC) delle PA stesse, requisito di base per l'interoperabilità delle comunicazioni ufficiali PA-PA e PA-cittadino.

---

## 5. Accessibilità dei servizi digitali

* **Legge Stanca (L. 4/2004)** e successive Linee Guida AGID: obbligo per i siti/servizi digitali della PA di essere accessibili a persone con disabilità visive, motorie, cognitive.
* **WCAG 2.1 (Web Content Accessibility Guidelines)** / **EN 301 549**: standard tecnici internazionali di riferimento per l'accessibilità, richiamati anche a livello UE dalla **EAA — European Accessibility Act** (recepita con D.Lgs. 82/2022), che estende gli obblighi di accessibilità anche a determinati soggetti privati (es. e-commerce, servizi bancari).
* Principi guida: percepibilità, utilizzabilità, comprensibilità, robustezza (i "4 principi POUR" del WCAG).

*Sintesi per l'esame*: se un quesito chiede di progettare/valutare un servizio digitale pubblico, cita sempre la conformità WCAG 2.1/EN 301 549 come requisito non negoziabile, non un "nice to have".

---

## 6. Interoperabilità: ModI, PDND, principio Once Only

* **ModI (Modello di Interoperabilità)**: regole tecniche AGID per lo scambio dati tra sistemi della PA tramite **API REST e SOAP**, articolate in pattern di interazione, pattern di sicurezza, profili di interoperabilità e raccomandazioni di implementazione (`AGID/pdf/03-04`).
  * *Sicurezza*: autenticazione tramite certificati **X.509** e **mTLS** (Mutual TLS, prova "chi è" il sistema chiamante) + autorizzazione tramite **OAuth 2.0** (prova "cosa può fare") — meccanismi complementari, non alternativi (`AGID/pdf/05`).
* **PDND (Piattaforma Digitale Nazionale Dati)**: infrastruttura che realizza tecnicamente il ModI, agendo da **control-plane/broker di fiducia** (non un data lake centrale — i dati non transitano fisicamente da PDND). Concetti chiave: Catalogo E-Service, adesione degli enti, voucher (token a breve durata), scambio dati asincrono (`AGID/pdf/06`).
* **Principio Once Only**: base giuridica nell'**art. 18 della L. 241/1990** (la PA non può chiedere dati già in proprio possesso o disponibili presso altra PA); attuazione tecnica tramite PDND; attuazione settoriale tramite il **FVOE** (Fascicolo Virtuale dell'Operatore Economico) nel Codice degli Appalti (D.Lgs. 36/2023).
* **Normativa comunitaria collegata**: **Direttiva 2014/55/UE** sulla fatturazione elettronica nella PA, veicolata tramite la rete **PEPPOL**, di cui AGID è **Authority nazionale**.

---

## 7. Quadro sinottico delle fonti normative

| Livello | Norma | Oggetto |
|---|---|---|
| UE | eIDAS (Reg. UE 910/2014) | Identità digitale, servizi fiduciari, riconoscimento transfrontaliero |
| UE | Direttiva 2014/55/UE | Fatturazione elettronica PA (via PEPPOL) |
| UE | European Accessibility Act (EAA) | Accessibilità servizi digitali, anche privati |
| Italia | CAD — D.Lgs. 82/2005 | Digitalizzazione PA: diritti digitali, documento informatico, firme, domicilio digitale, riuso software |
| Italia | L. 241/1990, art. 18 | Base giuridica del principio Once Only |
| Italia | L. 4/2004 (Legge Stanca) | Accessibilità siti/servizi PA |
| Italia | D.Lgs. 82/2022 | Recepimento EAA |

---

## Domande di autoverifica

1. Una PA deve dotarsi di un nuovo software gestionale. Secondo gli artt. 68-69 CAD, quale opzione deve valutare **per prima**?
   a) Sviluppo ex novo interno
   b) Software libero/open source
   c) Software proprietario leader di mercato
   d) Software in riuso da un'altra PA
   **Risposta: b)** — l'ordine di preferenza CAD è open source → riuso → sviluppo ex novo → proprietario; l'open source precede anche il riuso nella gerarchia dell'art. 68.

2. Quale affermazione sulla Firma Elettronica Avanzata (FEA) è corretta?
   a) Richiede sempre un certificato qualificato
   b) Non richiede l'identificazione univoca del firmatario
   c) È connessa unicamente al firmatario e creata con mezzi sotto il suo controllo esclusivo, ma senza certificato qualificato
   d) Ha lo stesso funzionamento tecnico della firma digitale (crittografia asimmetrica obbligatoria)
   **Risposta: c)** — è la definizione eIDAS di FEA; il certificato qualificato è ciò che distingue la FEQ.

3. Il principio "Once Only" trova il proprio fondamento giuridico primario in:
   a) Regolamento eIDAS
   b) Art. 18 della L. 241/1990
   c) Piano Triennale per l'Informatica
   d) Regole tecniche PDND
   **Risposta: b)** — la PDND è lo strumento tecnico attuativo, ma la base giuridica è l'art. 18 L. 241/1990 (divieto di richiedere dati già in possesso della PA).

4. Nel Modello di Interoperabilità (ModI), a cosa serve il **mTLS** rispetto a **OAuth 2.0**?
   a) Sono meccanismi alternativi e intercambiabili
   b) mTLS autentica il sistema chiamante (chi è), OAuth 2.0 autorizza le operazioni (cosa può fare)
   c) OAuth 2.0 sostituisce completamente mTLS nelle nuove Linee Guida
   d) mTLS serve solo per la cifratura dei dati at-rest
   **Risposta: b)** — sono complementari: autenticazione server-to-server (mTLS) + autorizzazione granulare (OAuth 2.0).

5. Cosa manca alla sola Firma Digitale (FEQ) per garantire l'opponibilità a terzi del momento di sottoscrizione?
   a) Nulla, la FEQ garantisce già la data certa
   b) Serve una marca temporale o l'invio tramite PEC
   c) Serve una seconda firma di un notaio
   d) Serve la pubblicazione in Gazzetta Ufficiale
   **Risposta: b)** — la firma digitale garantisce integrità e provenienza, ma non la data certa in autonomia.

6. Il domicilio digitale (art. 3-bis CAD) è registrato, per i cittadini e le imprese, in quale indice pubblico?
   a) IPA (Indice delle Pubbliche Amministrazioni)
   b) INAD (Indice Nazionale dei Domicili Digitali)
   c) PDND
   d) Registro delle Imprese
   **Risposta: b)** — INAD è dedicato a cittadini/professionisti/imprese; IPA è l'indice equivalente per le PA.
