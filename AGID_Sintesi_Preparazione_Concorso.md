# Sintesi Preparazione Concorso (Profilo AGID-01)
*Basata sulle Linee Guida, Piano Triennale e Documentazione AGID/ACN*

Questa sintesi organizza organicamente il materiale ufficiale scaricato per facilitare il ripasso strutturato delle materie d'esame. È concepita con un taglio da "Systems Engineer e ICT Consultant", privilegiando architetture, sicurezza e aderenza normativa.

---

## 1. Interoperabilità e Piattaforme (ModI & PDND)
L'obiettivo della digitalizzazione è superare la logica dei "silos" informatici, permettendo ai sistemi della PA di comunicare tra loro.
*   **Modello di Interoperabilità (ModI):** Definisce le regole tecniche per lo scambio dati tramite **API** (REST e SOAP).
    *   *Sicurezza:* Impone l'autenticazione tramite certificati X.509, integrità del payload, e pattern di sicurezza come **OAuth 2.0** (per l'autorizzazione) e **mTLS** (Mutual TLS per l'autenticazione server-to-server).
*   **PDND (Piattaforma Digitale Nazionale Dati):** È l'infrastruttura tecnologica che realizza il ModI. Permette alle PA di esporre (E-Service) e fruire di dati tramite un Catalogo API centrale.
    *   *Principio Chiave:* **Once Only**. Il cittadino non deve fornire dati che un'altra PA possiede già; le PA se li scambiano tramite PDND.

## 2. Cloud, Architetture e Migrazione
La PA adotta il principio **Cloud First**: le nuove iniziative e gli aggiornamenti infrastrutturali devono prediligere soluzioni Cloud (SaaS > PaaS > IaaS) per ridurre i costi, aumentare la scalabilità e garantire resilienza.
*   **Strategia Cloud Italia:** Classifica i dati della PA in tre livelli: *Ordinari*, *Critici* e *Strategici*. I dati Critici e Strategici devono risiedere su infrastrutture ad altissima affidabilità (come il **Polo Strategico Nazionale - PSN**).
*   **Percorsi di Migrazione:** Il Manuale AGID prevede tre approcci principali:
    1.  *Rehost (Lift & Shift):* Spostamento delle VM senza modifiche (IaaS).
    2.  *Replatform:* Uso di piattaforme gestite (es. DBaaS) con minime modifiche al codice.
    3.  *Rearchitect / Refactor:* Riprogettazione cloud-native (microservizi, container, serverless), per sfruttare appieno i benefici del cloud (massimo effort, massima resa).
*   **Qualificazione ACN/AGID:** I Cloud Service Provider (CSP) devono essere accreditati tramite un processo rigido di valutazione della sicurezza e inseriti in un marketplace dedicato.

## 3. Sviluppo Software: Acquisizione, Riuso e Sicurezza
Le metriche del software per la PA non si limitano alle prestazioni, ma includono sicurezza nativa e riusabilità.
*   **Acquisizione (Artt. 68-69 CAD):** Prima di acquistare un software proprietario, una PA deve eseguire una valutazione comparativa. L'ordine di preferenza è:
    1.  Software Open Source.
    2.  Software in riuso (già sviluppato da altra PA).
    3.  Sviluppo ex novo (che dovrà poi essere messo in riuso con licenza aperta).
    4.  Software proprietario (solo se strettamente necessario e motivato).
*   **Sviluppo Sicuro (Secure by Design):** Il ciclo di vita del software (SDLC) deve integrare la sicurezza dalla fase di design. 
    *   *Modellazione delle Minacce (Threat Modeling):* Identificare i rischi architetturali prima di scrivere il codice.
    *   *Controlli:* SAST (Static Application Security Testing) e DAST (Dynamic) continui (DevSecOps).
    *   *Linee guida OWASP:* Prevenzione di Injection, Broken Authentication e vulnerabilità note.

## 4. Dati: Documento Informatico, Open Data e IA
La gestione del patrimonio informativo (modellazione e metadatazione) è al centro della *data-driven administration*.
*   **Documento Informatico:** Equiparato alla carta, se formato e conservato secondo le regole tecniche.
    *   *Firme (eIDAS):* FES (semplice), FEA (avanzata) e FEQ (qualificata/digitale, garantisce non ripudio e integrità).
    *   *Metadatazione:* Ogni documento informatico deve avere un set minimo di metadati obbligatori (es. identificativo, data, oggetto, autore) per garantirne la rintracciabilità e fascicolazione elettronica.
*   **Open Data:** I dati pubblici (non soggetti a privacy) devono essere pubblicati in formati aperti, machine-readable (es. CSV, JSON) e descritti da ontologie (come *OntoPiA*) per garantirne la semantica condivisa.
    *   *Licenze aperte:* in coerenza col principio "open by default" del CAD e con la direttiva UE Open Data (2019/1024), i dataset pubblici vanno rilasciati con licenze aperte come **CC BY 4.0** (Creative Commons Attribution — consente riuso, modifica e uso commerciale col solo obbligo di attribuzione della fonte) o l'equivalente italiana **IODL 2.0**.
*   **Intelligenza Artificiale:** L'impiego del Machine Learning nella PA deve rispettare l'**AI Act** europeo (trasparenza algoritmica, assenza di bias, supervisione umana per decisioni critiche).

## 5. Programmazione, Budget e Governo IT
L'azione della PA deve essere programmata, misurabile e finanziariamente sostenibile.
*   **Piano Triennale per l'Informatica:** È lo strumento di governance strategica (attualmente 2024-2026). Definisce i target di trasformazione digitale (es. percentuale di servizi migrati in cloud, adozione SPID).
*   **Formazione del Budget:** La spesa ICT non è più vista come "centro di costo", ma come "investimento". Si basa su logiche di TCO (Total Cost of Ownership), tenendo conto anche dei costi di lock-in, formazione ed energy saving (Green IT).
*   **Gestione Progettuale:** Si raccomanda l'uso di framework strutturati (PRINCE2, PMP, o framework Agile) con KPI chiari e misurabili, essenziali per la rendicontazione dei fondi PNRR.

## 6. Appalti e Trasparenza 
L'infrastruttura amministrativa che permette la realizzazione tecnica dei progetti.
*   **Codice degli Appalti (D.Lgs. 36/2023):** Tutto il ciclo di gara (ICT e non) è interamente digitale (e-Procurement, Fascicolo Virtuale Operatore Economico). Acquisti IT gestiti tramite Consip/MePA. Liberalizzato (ma attenzionato lato cyber) il subappalto.
*   **Performance e Trasparenza:** 
    *   *Accessibilità:* I servizi digitali (Web/App) devono seguire le linee guida **WCAG 2.1** (Legge Stanca), garantendo usabilità a persone con disabilità visive, motorie o cognitive.
    *   *Design:* Coerenza visiva e centralità dell'utente (UX/UI standardizzate da *Designers Italia*).
    *   *Amministrazione Trasparente:* Obbligo di pubblicazione sui portali istituzionali dei dati relativi a bandi, appalti, bilanci e performance dirigenziali (D.Lgs. 33/2013).

## 7. Architettura Istituzionale e Gerarchia (PCM, DTD, AgID, ACN)
Tutti questi enti gravitano attorno alla **Presidenza del Consiglio dei Ministri (PCM)**, ma con ruoli ben distinti (fondamentale per le domande di Governance):
*   **DTD (Dipartimento per la Trasformazione Digitale):** Incardinato direttamente nella PCM, definisce la **strategia politica** e gestisce le risorse finanziarie strategiche (es. fondi digitali del PNRR).
*   **AgID (Agenzia per l'Italia Digitale):** È il **braccio tecnico-operativo**, sottoposto all'indirizzo politico del DTD/PCM. Redige materialmente il Piano Triennale ed emana le Linee Guida tecniche vincolanti per tutte le PA (es. ModI, SPID, Cloud).
*   **ACN (Agenzia per la Cybersicurezza Nazionale):** Autorità nazionale per la cybersicurezza, sotto il **controllo diretto** della PCM per via della delicatezza del suo mandato (sicurezza nazionale). Gestisce il Perimetro di Sicurezza Nazionale Cibernetica (PSNC), la vigilanza sulla NIS2, certifica la sicurezza del Cloud per la PA e gestisce lo CSIRT Italia.

*Sintesi pratica per l'esame (Separation of Duties)*: Il **DTD** decide la strategia e stanzia i fondi, l'**AgID** scrive le regole tecniche su come le PA devono attuare la strategia, l'**ACN** vigila che l'infrastruttura sia difesa dagli attacchi informatici.

### 7.1 Dipartimento vs Agenzia (differenza istituzionale)
La distinzione tra DTD (dipartimento) e AgID/ACN (agenzie) non è solo funzionale ma **giuridico-organizzativa**:
*   **Dipartimento** (es. DTD): struttura **interna** alla PCM, priva di personalità giuridica propria; il personale e il budget rientrano nel bilancio della PCM stessa (nessuna autonomia finanziaria); è diretto da un Capo Dipartimento di nomina politico-fiduciaria, in rapporto **gerarchico diretto** col vertice politico; svolge funzioni di indirizzo e programmazione, non eroga direttamente servizi tecnici.
*   **Agenzia** (es. AgID, ACN): **ente pubblico autonomo** con personalità giuridica propria, istituito con legge/decreto e sottoposto a **vigilanza** (non gerarchia) da parte della PCM; ha autonomia organizzativa, tecnica e di bilancio (budget proprio, personale con procedure proprie); è diretta da un Direttore Generale/vertice tecnico con mandato a termine; svolge funzioni tecnico-operative ed esecutive (linee guida, qualificazioni, gestione infrastrutture) con maggiore continuità rispetto al ciclo politico.

| | Dipartimento | Agenzia |
|---|---|---|
| Personalità giuridica | No (parte della PCM) | Sì (ente autonomo) |
| Funzione | Indirizzo politico-strategico | Attuazione tecnico-operativa |
| Rapporto con PCM | Interno, gerarchico | Esterno, vigilanza |
| Bilancio | Nel bilancio PCM | Bilancio proprio |

*Analogia utile per l'esame*: è la stessa logica che distingue in un'organizzazione la funzione di *governance/strategy* (Dipartimento) da quella di *execution/operations* (Agenzia), con la vigilanza della PCM che sostituisce il controllo gerarchico diretto con un controllo di indirizzo e verifica dei risultati.

## 8. Strategia Cloud Italia (Classificazione e PSN)
La strategia impone il paradigma **Cloud First**, ma regolamentato da rigidi criteri di sicurezza e sovranità del dato.
*   **Classificazione dei Dati (Regolamento ACN):** 
    *   *Ordinari:* Dati la cui compromissione non reca danni significativi (es. portale turistico istituzionale).
    *   *Critici:* Dati la cui compromissione causa danni rilevanti a funzioni istituzionali (es. anagrafe, sanità).
    *   *Strategici:* Dati essenziali per la sicurezza nazionale e funzioni core dello Stato.
*   **Qualificazione e PSN:**
    *   I dati Ordinari possono andare su Public Cloud qualificati (CSP iscritti al Marketplace ACN).
    *   I dati Critici e Strategici devono migrare sul **Polo Strategico Nazionale (PSN)** (o cloud privati/ibridi ad altissima sicurezza gestiti da in-house), garantendo che i dati e le chiavi di cifratura restino sotto giurisdizione italiana o UE.

*Sintesi per l'esame*: Se ti chiedono di progettare l'architettura di un servizio critico (es. Fascicolo Sanitario), specifica esplicitamente "deployment su infrastruttura qualificata PSN per garantire la sovranità e la protezione dei dati in linea con la Strategia Cloud".

## 9. Direttiva NIS2 e Resilienza Cibernetica
La **NIS2** (recepita con D.Lgs. 138/2024) innalza e uniforma il livello di sicurezza cibernetica nell'UE, con sanzioni severe per i vertici (management) in caso di inadempienza.
*   **Ampliamento del Perimetro:** Si applica capillarmente a PA centrali e locali, sanità, energia, trasporti e provider digitali (Soggetti "Essenziali" o "Importanti"). Affianca il **PSNC** (Perimetro di Sicurezza Nazionale Cibernetica, riservato alle infrastrutture iper-critiche dello Stato).
*   **Obblighi Chiave:**
    *   *Incident Reporting:* Obbligo di notifica precoce degli incidenti gravi al **CSIRT Italia (ACN)** entro **24 ore**, notifica completa entro 72 ore.
    *   *Supply Chain Security:* Le PA devono includere requisiti cyber rigorosi nei contratti con i fornitori (valutazione del rischio della catena di approvvigionamento ICT).
    *   *Controlli Tecnici:* Obbligo di cifratura end-to-end, MFA (Multi-Factor Authentication), backup immutabili e adozione di policy Zero Trust.

*Sintesi per l'esame*: Cita sempre la NIS2 quando parli di **Incident Response Plan** o di requisiti nei capitolati di gara ICT (Supply Chain). Ricorda il doppio binario in caso di attacco ransomware: la PA deve notificare sia l'ACN/CSIRT (obbligo NIS2 per impatto sui servizi) sia il Garante Privacy (obbligo GDPR se i dati personali sono esfiltrati).

## 10. Regolamento DORA (Digital Operational Resilience Act)
Cruciale in particolare per i concorsi in ambito finanziario (es. Banca d'Italia). DORA sposta il focus dalla pura solidità patrimoniale alla **resilienza operativa digitale** del settore finanziario europeo.
*   **Pilastri Fondamentali:**
    1.  *Gestione del rischio ICT:* Creazione di un solido framework di governance (responsabilità diretta del Management).
    2.  *Incident Reporting:* Armonizzazione delle tempistiche di segnalazione degli incidenti gravi alle autorità (Banca d'Italia, Consob, IVASS).
    3.  *Test di Resilienza:* Obbligo di eseguire vulnerability assessment continui e, per le entità maggiori, test di penetrazione avanzati (TLPT - Threat-Led Penetration Testing).
    4.  *Gestione del rischio terze parti (TPRM):* Controllo rigoroso sui fornitori ICT (inclusi i Cloud Provider), che ricadono sotto la vigilanza diretta delle autorità europee.

*Sintesi per l'esame*: In un caso pratico su un'infrastruttura bancaria o di pagamento, cita DORA per giustificare la necessità di contratti vincolanti con i cloud provider (audit rights, exit strategy) e la previsione di test di sicurezza continui (TLPT).

## 11. AI Act (Regolamento sull'Intelligenza Artificiale)
Primo framework normativo europeo per l'IA, basato su un approccio **Risk-Based** (proporzionale al rischio per i diritti fondamentali).
*   **Classificazione del Rischio:**
    *   *Inaccettabile:* Sistemi vietati (es. social scoring governativo, sorveglianza biometrica di massa).
    *   *Alto:* Sistemi soggetti a requisiti rigorosi prima del go-live (es. IA per recruiting o infrastrutture critiche). Richiedono tracciabilità (log), trasparenza e **supervisione umana (Human-in-the-loop)**.
    *   *Limitato:* Obblighi di trasparenza (es. i chatbot devono dichiarare la loro natura artificiale; i deepfake vanno etichettati).
    *   *Minimo:* Libero utilizzo (es. filtri antispam).

*Sintesi per l'esame*: Se il tema riguarda l'adozione del Machine Learning/GenAI, la soluzione deve includere la mitigazione dei "bias" nei dataset e l'obbligo di supervisione umana per non delegare decisioni impattanti a "scatole nere" algoritmiche.

## 12. GDPR (General Data Protection Regulation) e Privacy
Il fondamento normativo per la protezione dei dati personali. Non è solo compliance legale, ma un vincolo architetturale IT.
*   **Principi Architetturali:**
    *   *Privacy by Design:* La protezione dei dati integrata fin dalla progettazione del software (es. pseudonimizzazione, cifratura dei DB).
    *   *Privacy by Default:* Raccolta del solo dato strettamente necessario e impostazioni predefinite restrittive (*Data Minimization*).
*   **Obblighi in progetti ICT:**
    *   *DPIA (Data Protection Impact Assessment):* Valutazione preventiva obbligatoria (da fare col DPO) se un nuovo progetto presenta rischi elevati per i diritti delle persone (es. videosorveglianza, profilazione, dati sanitari).
    *   *Data Breach Notification:* Obbligo di notificare le violazioni al Garante Privacy entro **72 ore**.

*Sintesi per l'esame*: Qualsiasi sistema che tratti dati di cittadini o dipendenti deve prevedere cifratura (at-rest e in-transit), RBAC (Role-Based Access Control) rigoroso, audit log immutabili degli accessi e l'esecuzione di una DPIA in fase di startup del progetto.

---
> [!TIP] 
> **Come usare questo riassunto per la prova scritta (Profilo A/C)**
> Quando affronti un **caso pratico gestionale** (es. "Progettare la migrazione di un database on-premise"), usa una struttura logica che tocchi questi punti:
> 1. **Architettura:** Migrazione Replatform sul Cloud PSN (Punto 2).
> 2. **Sicurezza:** Cifratura at-rest e in-transit, Threat modeling (Punto 3).
> 3. **Acquisizione:** Uso di MePA/Consip (Punto 6) e preferenza Open Source (Punto 3).
> 4. **Integrazione:** Esposizione API REST tramite PDND (Punto 1).
