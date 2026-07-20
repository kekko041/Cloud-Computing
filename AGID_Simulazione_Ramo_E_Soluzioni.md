# Soluzioni — Simulazione Ramo E: CAD, Appalti ICT & Trasparenza

> Risposte modello alla [simulazione Ramo E](AGID_Simulazione_Ramo_E.md), redatte per coprire tutte le voci della griglia di autocorrezione.

---

## Quesito 1 — FES, FEA, FEQ ed eIDAS

Il **Regolamento eIDAS (UE 910/2014)**, recepito e attuato a livello nazionale dal CAD, distingue tre livelli di firma elettronica. La **firma elettronica semplice (FES)** non richiede alcun requisito particolare di identificazione del firmatario (es. una firma via checkbox/click, o una firma scannerizzata): ha il valore probatorio più debole. La **firma elettronica avanzata (FEA)** richiede l'identificazione univoca del firmatario e garantisce l'integrità del documento sottoscritto, ma senza l'uso di un certificato qualificato rilasciato da un prestatore accreditato. La **firma elettronica qualificata (FEQ)** si basa su un certificato qualificato e un dispositivo sicuro di firma, ed è l'unica ad avere, per legge, un'efficacia probatoria **equivalente alla firma autografa**.

Un'amministrazione è tenuta a richiedere la **FEQ** quando l'atto produce **effetti giuridici pieni** e richiede valore probatorio pieno e non ripudio: tipicamente per la sottoscrizione di contratti pubblici e provvedimenti amministrativi formali, non per una semplice richiesta informale o un'istanza a basso impatto, per cui può bastare una FEA o, in alcuni casi, anche solo un'identificazione tramite SPID/CIE con FES.

---

## Quesito 2 — Obblighi di pubblicazione D.Lgs. 33/2013 e FVOE

Il **D.Lgs. 33/2013** ("Amministrazione Trasparente") impone, per ogni procedura di affidamento (incluse quelle ICT), la pubblicazione di dati minimi: **struttura proponente**, **oggetto** dell'affidamento, **importo**, **aggiudicatario**, **tempi di completamento** e **importi liquidati**. Questi dati devono essere pubblicati in formato aperto e aggiornati periodicamente per l'intera durata del contratto.

Il **Fascicolo Virtuale dell'Operatore Economico (FVOE)**, introdotto dal D.Lgs. 36/2023, è un fascicolo digitale che raccoglie in modo centralizzato la documentazione comprovante i requisiti dell'operatore economico (es. iscrizione camerale, DURC, casellario), riducendo l'onere per le imprese di ripresentare gli stessi documenti a ogni gara a cui partecipano: applica quindi la logica **Once Only** al procurement pubblico.

I due obblighi sono collegati: gli obblighi di trasparenza sull'esito della gara riusano dati già strutturati e disponibili nella Piattaforma di Approvvigionamento Digitale (PAD) e nel FVOE, evitando una duplicazione manuale delle informazioni tra sistemi di gara e portali di trasparenza.

---

## Quesito 3 — Affidamento diretto (D.Lgs. 36/2023)

L'**affidamento diretto**, ai sensi del D.Lgs. 36/2023 (Codice dei Contratti Pubblici), consente alla PA di acquistare forniture e servizi — incluso l'ICT — **sotto una soglia di 140.000 €**, senza il ricorso a una procedura di gara competitiva ordinaria.

L'istituto risponde principalmente al **Principio del Risultato** (tempestività dell'acquisto e miglior rapporto qualità/prezzo, senza gli oneri procedurali di una gara formale per importi limitati) e al **Principio dell'Accesso al mercato** (garantire comunque una concorrenza minima anche negli affidamenti diretti).

Anche sotto soglia, la PA deve comunque rispettare alcune garanzie procedurali: la **rotazione degli affidatari** (per evitare la concentrazione ripetuta degli acquisti sullo stesso fornitore), la **motivazione/congruità del prezzo** offerto, la **tracciabilità digitale** dell'acquisto (tramite BDNCP e, per gli aspetti di qualificazione del fornitore, il FVOE) e, salvo eccezioni motivate, l'obbligo di veicolare l'acquisto tramite **Consip o il MePA**.

---

## Quesito 4 — Ciclo della performance (D.Lgs. 150/2009) applicato a un progetto ICT

Il ciclo della performance previsto dal **D.Lgs. 150/2009** si articola in fasi sequenziali: **definizione degli obiettivi** (formalizzata nel Piano della Performance), **misurazione e monitoraggio** in corso d'anno rispetto agli obiettivi definiti, **valutazione finale** del grado di raggiungimento, e **rendicontazione** tramite la Relazione sulla Performance.

Applicato a un progetto ICT concreto, questo ciclo si traduce in KPI di progetto/servizio: ad esempio i **tempi di completamento** delle fasi progettuali rispetto al piano, o indicatori di **qualità del servizio digitale** erogato (es. tempo di risposta, tasso di errore, soddisfazione dell'utente) misurati periodicamente e confluiti nella valutazione annuale.

È importante distinguere questo ciclo dagli obblighi del **D.Lgs. 33/2013**: il D.Lgs. 150/2009 riguarda la **misurazione e valutazione della performance** (organizzativa e individuale, con effetti anche su retribuzione/carriera dei dirigenti), mentre il D.Lgs. 33/2013 riguarda gli **obblighi di pubblicazione proattiva** dei dati (compresi, tra gli altri, i dati sugli affidamenti e sulla performance dirigenziale stessa) — sono quindi due strumenti complementari ma con finalità distinte: valutazione interna vs trasparenza verso l'esterno.

---

## Quesito 5 — L. 241/1990, CAD e principio Once Only

La **L. 241/1990** prevede istituti a garanzia della partecipazione al procedimento: la **comunicazione di avvio del procedimento** (artt. 7-8), che informa l'interessato dell'avvio di un procedimento che lo riguarda, e il **preavviso di rigetto** (art. 10-bis), che garantisce il contraddittorio prima di un'eventuale decisione sfavorevole, dando all'interessato la possibilità di presentare osservazioni.

L'**art. 18** della stessa legge sancisce il divieto per la PA di richiedere all'interessato dati o documenti già in proprio possesso o disponibili presso un'altra amministrazione: è questa la **base giuridica generale del principio Once Only**, ben prima che il CAD ne fornisse l'attuazione tecnologica.

Il CAD non introduce infatti una normativa alternativa o sostitutiva rispetto alla L. 241/1990, ma ne costituisce l'**attuazione digitale**: identità digitale (per l'identificazione certa dell'interessato nel procedimento telematico), domicilio digitale (per le comunicazioni previste dagli artt. 7-8) e conservazione documentale a norma (per il fascicolo del procedimento) sono gli strumenti tecnologici con cui gli istituti della 241/90 vengono realizzati nel procedimento amministrativo informatico.

Un'attuazione tecnica concreta dell'art. 18 nel mondo AGID è la **PDND**, che realizza l'interoperabilità dei dati tra PA senza richiederli nuovamente al cittadino, e il **FVOE**, che applica lo stesso principio ai dati delle imprese partecipanti a una gara pubblica.

---

## Caso gestionale

*Metodo (4 mosse): (1) inquadramento normativo, (2) metodo progettuale, (3) soluzione tecnica, (4) rischio & budget.*

**Contesto.** Un Comune capoluogo deve sostituire un portale legacy monolitico dei servizi al cittadino (anagrafe, tributi, pratiche edilizie) tramite gara pubblica ICT, garantendo identità digitale, firma e conservazione a norma, trasparenza sull'affidamento e gestione consapevole del rischio subappalto.

### (a) Procedura di affidamento

Per componenti standardizzate (es. infrastruttura cloud, licenze software commerciali) è preferibile un **accordo quadro Consip/MePA**, più rapido e già collaudato sotto il profilo della qualificazione tecnico-economica; per lo sviluppo/integrazione della nuova piattaforma, che richiede una soluzione specifica per il Comune, è più adeguata una **procedura aperta ai sensi del D.Lgs. 36/2023**.

Il **RUP** (Responsabile Unico di Progetto) coordina l'intera procedura, dalla programmazione alla verifica di esecuzione. I passaggi e-procurement obbligatori includono la raccolta del **DGUE** (Documento di Gara Unico Europeo) da ciascun operatore economico partecipante e la consultazione del **FVOE** per la verifica dei requisiti, riducendo gli oneri documentali ripetuti.

### (b) Requisiti CAD del nuovo portale

Il CAD impone: accesso tramite **identità digitale** (SPID/CIE, eventualmente tramite OpenID Connect nel caso di SPID); **domicilio digitale** del cittadino tramite **INAD** per le comunicazioni relative ai procedimenti (anagrafe, tributi, edilizia); un livello di **firma elettronica qualificata (FEQ)** per la sottoscrizione del contratto con il fornitore e dei provvedimenti amministrativi con effetti giuridici pieni prodotti dal nuovo sistema; **conservazione documentale a norma** degli atti prodotti, con il set minimo di metadati (identificativo, data, oggetto, autore) e fascicolazione elettronica coerente per procedimento.

### (c) Trasparenza e performance

Durante e dopo l'affidamento vanno rispettati gli obblighi di pubblicazione del **D.Lgs. 33/2013** (struttura proponente, oggetto, importo, aggiudicatario, tempi, importi liquidati dell'affidamento). In parallelo va attivato il **monitoraggio dell'esecuzione contrattuale** (project management sul fornitore, v. Ramo D) e il **ciclo della performance** (D.Lgs. 150/2009), con indicatori di performance del progetto (tempi di rilascio, qualità del servizio digitale erogato ai cittadini) distinti — ma coordinati — dagli obblighi di trasparenza proattiva.

### (d) Rischi e mitigazioni

- **Subappalto**: liberalizzato dal Codice, ma "attenzionato" sul piano cyber quando riguarda componenti critiche del portale (es. gestione dell'identità digitale o dei dati anagrafici) → mitigazione con verifiche rafforzate sul subappaltatore (requisiti di sicurezza equivalenti al contraente principale, clausole contrattuali esplicite, audit periodici, SLA di sicurezza estesi anche al subappaltatore);
- **Superamento soglia e parere di congruità**: se il valore dell'affidamento supera le soglie rilevanti e l'acquisto avviene tramite Consip/soggetto aggregatore su un bene strategico, il **parere di congruità tecnico-economica** (art. 14-bis CAD) diventa **vincolante**; se l'affidamento avviene fuori da questi canali, resta **non vincolante** pur restando opportuno richiederlo dato l'impatto del progetto.

**Criticità residue.** La coesistenza di componenti acquisite tramite canali diversi (accordo quadro per l'infrastruttura, procedura aperta per lo sviluppo) richiede un coordinamento contrattuale esplicito per evitare zone grigie di responsabilità tra i fornitori in caso di malfunzionamento del portale integrato.
